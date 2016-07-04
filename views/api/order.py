# -*- coding: utf-8 -*-
import StringIO
import time
import urllib
import json
import datetime

from tornado import gen
from tornado.httpclient import AsyncHTTPClient
import xlwt
import tcelery

from models.user import UserModel
from tools.auth import auth_login, auth_permission
from tools.request_tools import get_and_valid_arguments
from views.base import BtwBaseHandler
from exception.json_exception import JsonException
from exception.celery_exception import CeleryException
from tasks.order import cancel_order_in_queue as Cancel
from constants import PERMISSIONS, BED_TYPE, ORDER_STATUS
from models.order import OrderModel
from models.order_history import OrderHistoryModel
from config import API
from tools.log import Log

tcelery.setup_nonblocking_producer()


class OrderWaitingAPIHandler(BtwBaseHandler):
    @auth_login(json=True)
    @auth_permission(PERMISSIONS.admin | PERMISSIONS.update_order, json=True)
    def get(self):
        merchant_id = self.current_user.merchant_id
        start = self.get_query_argument('start', 0)
        limit = self.get_query_argument('limit', 20)

        orders, total = OrderModel.get_waiting_orders(self.db, merchant_id, start, limit, self.current_user.hotel_id)

        self.finish_json(result={
            'orders': [order.todict() for order in orders],
            'total': total,
            'start': start,
            'limit': limit,
        })


class OrderWaitingCountAPIHandler(BtwBaseHandler):
    @auth_login(json=True)
    @auth_permission(PERMISSIONS.admin | PERMISSIONS.update_order | PERMISSIONS.view_order, json=True)
    def get(self):
        merchant_id = self.current_user.merchant_id
        total = OrderModel.get_waiting_orders_count(self.db, merchant_id, self.current_user.hotel_id)

        self.finish_json(result={
            'total': total,
        })


class OrderInfoAPIHandler(BtwBaseHandler):
    @auth_login(json=True)
    @auth_permission(PERMISSIONS.admin | PERMISSIONS.update_order | PERMISSIONS.view_order, json=True)
    def get(self, order_id):
        merchant_id = self.current_user.merchant_id
        order = OrderModel.get_by_merchant_and_id(self.db, merchant_id, order_id, self.current_user.hotel_id)

        self.finish_json(result={
            'order': order.todict() if order else None,
        })


class OrderUserConfirmAPIHandler(BtwBaseHandler):
    @gen.coroutine
    @auth_login(json=True)
    @auth_permission(PERMISSIONS.admin | PERMISSIONS.update_order, json=True)
    def post(self, order_id):

        order = OrderModel.get_by_id(self.db, order_id)
        pre_status = order.status
        if order.merchant_id != self.merchant.id:
            raise JsonException(100, 'merchant not valid')
        if order.status != 100:
            raise JsonException(200, 'illegal status')
        if self.current_user.type == UserModel.TYPE_SUB and order.hotel_id != self.current_user.hotel_id:
            raise JsonException(500, 'illegal hotel')

        if (yield self.callback_order_server(order)):
            order.confirm_by_user(self.db)
            if order.status != pre_status:
                OrderHistoryModel.set_order_status_by_user(
                    self.db, self.current_user, order, pre_status, order.status)
        else:
            raise JsonException(1000, 'callback order server fail')

        self.finish_json(result=dict(
            order=order.todict(),
        ))

    @gen.coroutine
    def callback_order_server(self, order):
        url = API['ORDER'] + '/order/ebooking/update'
        params = {'orderId': order.id, 'msgType': 0, 'success': True,
                  'btwOrderId': order.main_order_id,
                  'trackId': self.generate_track_id(order.id)}
        r = yield AsyncHTTPClient().fetch(url, method='POST',
                                          body=urllib.urlencode(params)
        )
        Log.info(r.body)
        resp = json.loads(r.body)

        if resp and resp['errcode'] == 0:
            raise gen.Return(True)
        raise gen.Return(False)

    def generate_track_id(self, order_id):
        return "{}|{}".format(order_id, time.time())


class OrderUserCancelAPIHandler(BtwBaseHandler):
    @gen.coroutine
    @auth_login(json=True)
    @auth_permission(PERMISSIONS.admin | PERMISSIONS.update_order, json=True)
    def post(self, order_id):
        merchant_id = self.current_user.merchant_id
        args = self.get_json_arguments()
        reason, = get_and_valid_arguments(args, 'reason')
        if not reason:
            raise JsonException(200, 'invalid reason')

        order = OrderModel.get_by_id(self.db, order_id)

        pre_status = order.status

        if order.merchant_id != merchant_id:
            raise JsonException(300, 'merchant invalid')
        if order.status not in [0, 100]:
            raise JsonException(400, 'illegal status')
        if self.current_user.type == UserModel.TYPE_SUB and order.hotel_id != self.current_user.hotel_id:
            raise JsonException(500, 'illegal hotel')

        if not (yield self.callback_order_server(order)):
            raise JsonException(1000, 'callback order server error')

        task = yield gen.Task(Cancel.cancel_order_by_user.apply_async,
                              args=[order_id, reason])

        if task.status == 'SUCCESS':
            order = task.result
            if order.status != pre_status:
                OrderHistoryModel.set_order_status_by_user(
                    self.db, self.current_user, order, pre_status, order.status)
            self.finish_json(result=dict(
                order=order.todict(),
            ))
        else:
            if isinstance(task.result, CeleryException):
                raise JsonException(1000, task.result.errmsg)
            else:
                raise JsonException(1000, 'network error')

    @gen.coroutine
    def callback_order_server(self, order):
        url = API['ORDER'] + '/order/ebooking/update'
        params = {'orderId': order.id, 'msgType': 0, 'success': False,
                  'btwOrderId': order.main_order_id,
                  'trackId': self.generate_track_id(order.id)}
        r = yield AsyncHTTPClient().fetch(url, method='POST',
                                          body=urllib.urlencode(params)
        )
        Log.info(r.body)
        resp = json.loads(r.body)

        if resp and resp['errcode'] == 0:
            raise gen.Return(True)
        raise gen.Return(False)

    def generate_track_id(self, order_id):
        return "{}|{}".format(order_id, time.time())


class OrderTodayBookListAPIHandler(BtwBaseHandler):
    @auth_permission(PERMISSIONS.admin | PERMISSIONS.view_order, json=True)
    @auth_login(json=True)
    def get(self):
        merchant_id = self.current_user.merchant_id
        start = self.get_query_argument('start', 0)
        limit = self.get_query_argument('limit', 20)

        orders, total = OrderModel.get_today_book_orders(self.db, merchant_id, start, limit, self.current_user.hotel_id)
        self.finish_json(result={
            'total': total,
            'start': start,
            'limit': limit,
            'orders': [order.todict() for order in orders],
        })


class OrderTodayCheckinListAPIHandler(BtwBaseHandler):
    @auth_login(json=True)
    @auth_permission(PERMISSIONS.admin | PERMISSIONS.view_order, json=True)
    def get(self):
        merchant_id = self.current_user.merchant_id
        start = self.get_query_argument('start', 0)
        limit = self.get_query_argument('limit', 20)

        orders, total = OrderModel.get_today_checkin_orders(
            self.db, merchant_id, start, limit, self.current_user.hotel_id)
        self.finish_json(result={
            'orders': [order.todict() for order in orders],
            'total': total,
            'start': start,
            'limit': limit,
        })


class OrderSearchAPIHandler(BtwBaseHandler):
    @auth_login(json=True)
    @auth_permission(PERMISSIONS.admin | PERMISSIONS.view_order, json=True)
    def get(self):
        merchant_id = self.current_user.merchant_id

        order_id = self.get_query_argument('order_id', None)
        hotel_name = self.get_query_argument('hotel_name', None)
        checkin_date_start = self.get_query_argument(
            'checkin_date_start', None)
        checkin_date_end = self.get_query_argument('checkin_date_end', None)
        customer = self.get_query_argument('customer', None)
        order_status = self.get_query_argument('order_status', None)
        create_time_start = self.get_query_argument('create_time_start', None)
        create_time_end = self.get_query_argument('create_time_end', None)
        start = self.get_query_argument('start', 0)
        limit = self.get_query_argument('limit', 20)

        if order_status:
            order_status = order_status.split(',')

        orders, total = OrderModel.search(self.db,
                                          merchant_id, self.current_user.hotel_id, order_id, hotel_name,
                                          checkin_date_start, checkin_date_end, customer, order_status,
                                          create_time_start, create_time_end, start, limit)

        self.finish_json(result={
            'orders': [order.todict() for order in orders],
            'total': total,
            'start': start,
            'limit': limit,
        })


class OrderSwitchSearchAPIHandler(BtwBaseHandler):
    def post(self):
        merchant_id = self.get_argument('merchant_id', None)
        if not merchant_id:
            raise JsonException(-1, "缺少merchant_id")

        update_time = self.get_argument('update_time', None)
        start = int(self.get_argument('start', 0))
        limit = int(self.get_argument('limit', 20))
        order_id = self.get_argument('order_id', None)
        status = self.get_argument('status', None)
        try:
            limit = 100 if limit > 100 else limit
            orders, total = OrderModel.search_switch(self.db, merchant_id, update_time, start, limit, order_id, status)
        except Exception, e:
            raise JsonException(-1, e.message)

        self.finish_json(result={
            'orders': [order.todict() for order in orders],
            'total': total,
            'start': start,
            'limit': limit,
        })


class OrderSwitchConfirmAPIHandler(BtwBaseHandler):
    def post(self):
        order_id = self.get_argument('order_id', None)
        status = self.get_argument('status', None)
        if not order_id:
            raise JsonException(-1, 'params : id not exists')
        if not status or int(status) not in [300, 500]:
            raise JsonException(-1, 'params: status is not validate')
        order = OrderModel.get_by_main_order_id(self.db, order_id)
        if not order:
            raise JsonException(1, 'order not exist')

        pre_status = order.status

        OrderModel.change_order_status_by_main_order_id(self.db, order_id, status)
        OrderHistoryModel.set_order_status_by_server(self.db, order, pre_status, status)
        self.finish_json()


class OrderExportExceAPiHandler(BtwBaseHandler):
    @auth_permission(PERMISSIONS.admin | PERMISSIONS.view_order)
    def get(self):
        merchant_id = self.current_user.merchant_id

        order_id = self.get_query_argument('order_id', None)
        hotel_name = self.get_query_argument('hotel_name', None)
        checkin_date_start = self.get_query_argument(
            'checkin_date_start', None)
        checkin_date_end = self.get_query_argument('checkin_date_end', None)
        customer = self.get_query_argument('customer', None)
        order_status = self.get_query_argument('order_status', None)
        create_time_start = self.get_query_argument('create_time_start', None)
        create_time_end = self.get_query_argument('create_time_end', None)

        order_ids = self.get_query_argument('order_ids', None)
        if order_ids:
            order_ids = [int(order_id_) for order_id_ in order_ids.split(',')]
        if order_status:
            order_status = order_status.split(',')

        orders, total = OrderModel.search_export_orders(self.db,
                                                        merchant_id, self.current_user.hotel_id, order_id, hotel_name,
                                                        checkin_date_start, checkin_date_end, customer, order_status,
                                                        create_time_start, create_time_end, order_ids)
        wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = wbk.add_sheet('EBooking订单列表')
        row = 0
        sheet.write(row, 0, '订单确认号')
        sheet.write(row, 1, '酒店名称')
        sheet.write(row, 2, '房型')
        sheet.write(row, 3, '床型')
        sheet.write(row, 4, '房间数')
        sheet.write(row, 5, '入店日期')
        sheet.write(row, 6, '离店日期')
        sheet.write(row, 7, '预约时间')
        sheet.write(row, 8, '入住人')
        sheet.write(row, 9, '确认类型')
        sheet.write(row, 10, '每日价格')
        sheet.write(row, 11, '总价')
        sheet.write(row, 12, '订单状态')

        for order in orders:
            row += 1
            self.write_one_row(sheet, row, order)
        export_time = datetime.datetime.now()
        file_name = 'orders_{}.xls'.format(export_time.strftime('%Y-%m-%d %H:%M:%S'))
        self.set_header('Content-type', 'application/vnd.ms-excel')
        self.set_header('Content-Disposition', 'attachment; filename="' + file_name + '"')
        sio = StringIO.StringIO()
        wbk.save(sio)
        self.write(sio.getvalue())

    def write_one_row(self, sheet, row, order):
        sheet.write(row, 0, order.id)
        sheet.write(row, 1, order.hotel_name)
        sheet.write(row, 2, order.roomtype_name)
        sheet.write(row, 3, BED_TYPE.get(order.bed_type) or '')
        sheet.write(row, 4, order.room_num)
        sheet.write(row, 5, order.checkin_date.strftime('%Y-%m-%d'))
        sheet.write(row, 6, order.checkout_date.strftime('%Y-%m-%d'))
        sheet.write(row, 7, order.create_time.strftime('%Y-%m-%d'))
        sheet.write(row, 8, ','.join(self.get_customer_info(order.customer_info)))
        sheet.write(row, 9, '自动确认' if order.confirm_type == 1 else '人工确认')
        sheet.write(row, 10, ','.join([str(float(price) / 100) for price in order.everyday_price.split(',')]))
        sheet.write(row, 11, float(order.total_price) / 100)
        sheet.write(row, 12, ORDER_STATUS.get(order.status) or '')

    def get_customer_info(self, customer_info):
        res = []
        if customer_info:
            for c in json.loads(customer_info):
                res.append(c['name'])
        return res