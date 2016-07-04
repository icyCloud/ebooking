# -*- coding: utf-8 -*-
import json
import urllib

from tornado import gen
from tornado.escape import json_decode
from tornado.httpclient import AsyncHTTPClient
from config import API

from models.rate_plan import RatePlanModel
from models.room_rate import RoomRateModel
from models.cooperate_roomtype import CooperateRoomTypeModel
from models.inventory import InventoryModel

from utils.stock_push.rateplan import RatePlanPusher
from utils.stock_push.hotel import HotelPusher


class CooperateMixin(object):
    @gen.coroutine
    def delete_rateplan(self, rateplan):
        r = self._delete_rateplans([rateplan])
        raise gen.Return(r)

    @gen.coroutine
    def delete_hotel(self, hotel):
        if not hotel:
            raise gen.Return(True)
        r = yield self._delete_hotels([hotel])
        raise gen.Return(r)

    @gen.coroutine
    def delete_roomtype(self, roomtype):
        r = yield self._delete_roomtypes([roomtype])
        raise gen.Return(r)

    @gen.coroutine
    def _delete_hotels(self, hotels):
        if not hotels:
            gen.Return(True)

        for hotel in hotels:
            r = yield self._delete_roomtypes_by_hotel(hotel)
            if r:
                r = yield self._delete_poi_hotel(hotel.id)
                if r:
                    hotel.is_delete = 1
                    r = yield HotelPusher(self.db).push_hotel(hotel)
                    if not r:
                        raise gen.Return(False)
                else:
                    raise gen.Return(False)
            else:
                raise gen.Return(False)
        else:
            raise gen.Return(True)

    @gen.coroutine
    def _delete_roomtypes_by_hotel(self, hotel):
        roomtypes = CooperateRoomTypeModel.get_by_hotel_id(self.db, hotel.id)
        r = yield self._delete_roomtypes(roomtypes, notify_stock=False)
        raise gen.Return(r)

    @gen.coroutine
    def _delete_roomtypes(self, roomtypes, notify_stock=True):
        if not roomtypes:
            raise gen.Return(True)
        for roomtype in roomtypes:
            r = yield self._delete_rateplan_by_roomtype(roomtype)
            if not r:
                raise gen.Return(False)
            self._clear_inventoris_by_roomtype(roomtype)
            r = yield self._delete_poi_room(roomtype.hotel_id, roomtype.id)
            if not r:
                raise gen.Return(False)

        # delete roomtypes:
        for roomtype in roomtypes:
            roomtype.is_delete = 1

        if notify_stock:
            r = yield HotelPusher(self.db).push_hotel_by_id(roomtypes[0].hotel_id)
            if r:
                raise gen.Return(True)
            else:
                raise gen.Return(False)
        else:
            raise gen.Return(True)

    @gen.coroutine
    def _delete_rateplan_by_roomtype(self, roomtype):
        rateplans = RatePlanModel.get_by_roomtype(self.db, roomtype.id)
        r = yield self._delete_rateplans(rateplans)
        raise gen.Return(r)

    @gen.coroutine
    def _delete_rateplans(self, rateplans):
        if not rateplans:
            raise gen.Return(True)
        rateplan_ids = [rateplan.id for rateplan in rateplans]
        roomrates = RoomRateModel.get_by_rateplans(self.db, rateplan_ids)

        for rateplan in rateplans:
            rateplan.is_delete = 1
        for roomrate in roomrates:
            roomrate.is_delete = 1

        r = yield RatePlanPusher(self.db).update_rateplans_valid_status(rateplan_ids)
        raise gen.Return(r)

    def _clear_inventoris_by_roomtype(self, roomtype):
        InventoryModel.delete_by_roomtype_id(self.db, roomtype.id, commit=False)

    @gen.coroutine
    def _delete_poi_room(self, hotel_id, roomtype_id):
        data = {
            'chain_hotel_id': str(hotel_id),
            'chain_roomtype_id': str(roomtype_id)
        }
        resp = yield AsyncHTTPClient().fetch(API['POI'] + '/api/delete/ebooking/room/', headers={"Content-Type": "application/json"}, method='POST',
                                             body=json.dumps(data))
        r = json_decode(resp.body)

        if r and r['errcode'] == 0:
            raise gen.Return(True)
        else:
            raise gen.Return(False)

    @gen.coroutine
    def _delete_poi_hotel(self, hotel_id):
        data = {
            'chain_hotel_id': str(hotel_id)
        }
        resp = yield AsyncHTTPClient().fetch(API['POI'] + '/api/delete/ebooking/hotel/', headers={"Content-Type": "application/json"}, method='POST',
                                             body=json.dumps(data))
        r = json_decode(resp.body)

        if r and r['errcode'] == 0:
            raise gen.Return(True)
        else:
            raise gen.Return(False)