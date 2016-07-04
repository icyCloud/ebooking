# -*- coding: utf-8 -*-
import re
from tornado import gen

from tornado.escape import json_encode
from models.merchant import MerchantModel
from models.user_hotel_mapping import UserHotelMappingModel
from views.api.hotel_cooped import HotelCoopedAPIHandler

from views.base import BtwBaseHandler
from tools.auth import auth_login
from tools.auth import auth_permission
from constants import PERMISSIONS
from tools.request_tools import get_and_valid_arguments

from models.user import UserModel


class UserAPIHandler(BtwBaseHandler):
    @auth_login()
    def get(self):
        self.finish_json(result=dict(
            user=self.current_user.todict(),
        ))


class UserManageAPIHandler(BtwBaseHandler):
    @auth_login()
    @auth_permission(PERMISSIONS.admin)
    def get(self):
        users = UserModel.get_users_by_merchant_id(self.db, self.current_user.merchant_id)
        mappings = UserHotelMappingModel.get_hotel_by_id(self.db, None, self.current_user.merchant_id)
        if mappings:
            map_ids = {map.user_id: map.hotel_id for map in mappings}
            for user in users:
                user.hotel_id = map_ids.get(user.id)
        self.finish_json(
            0, u'成功', json_encode([user.todict() for user in users]))

    @auth_login(json=True)
    @auth_permission(PERMISSIONS.admin, json=True)
    def put(self):
        args = self.get_json_arguments()
        merchant_id, username, department, mobile, authority, is_valid = \
            get_and_valid_arguments(
                args, 'merchant_id', 'username', 'department', 'mobile', 'authority', 'is_valid')

        hotel_id = None
        if 'hotel_id' in args:
            hotel_id = args['hotel_id']
            try:
                authority = None
                hotel_id = int(hotel_id)
            except Exception:
                self.finish_json('1', u'不合法的酒店')
                return
        if 'email' in args:
            email = args['email']
        else:
            email = None

        if 'password' in args:
            password = args['password']
        else:
            password = None

        if not self.mobile_check(mobile):
            self.finish_json(1, u'请填写正确手机号')
            return

        if not department:
            self.finish_json(1, u'请填写部门')
            return

        if self.current_user.merchant_id != merchant_id:
            self.finish_json(1, u'您只能管理自己的酒店')
            return

        ''' 可以管理用户 '''
        UserModel.update_user(self.db, merchant_id, username,
                              password, department, mobile, email, is_valid, authority, hotel_id)

        ''' 修改了自己的密码 '''
        if self.current_user.username == username and password:
            self.clear_cookie('username')
            self.clear_cookie('merchant_id')
            self.finish_json(301, self.get_login_url())
            return

        self.finish_json(0, u'成功')

    @auth_login(json=True)
    @auth_permission(PERMISSIONS.admin, json=True)
    def post(self):
        args = self.get_json_arguments()
        merchant_id, username, password, re_password, department, mobile, authority, is_valid = \
            get_and_valid_arguments(
                args, 'merchant_id', 'username', 'password', 're_password', 'department', 'mobile',
                'authority', 'is_valid')

        hotel_id = None
        if 'hotel_id' in args:
            hotel_id = args['hotel_id']
            try:
                hotel_id = int(hotel_id)
                authority = 0
                authority += PERMISSIONS.update_order
                authority += PERMISSIONS.view_cooperated_hotel
                authority += PERMISSIONS.view_order
                authority += PERMISSIONS.inventory
                authority += PERMISSIONS.pricing
                authority += PERMISSIONS.update_password
            except Exception:
                self.finish_json('1', u'不合法的酒店')
                return

        if merchant_id != self.current_user.merchant_id:
            self.finish_json(1, u'您只能管理自己的酒店')
            return
        if not username:
            self.finish_json(1, u'请填写用户名')
            return
        if (not password) or (not re_password):
            self.finish_json(1, u'请输入密码')
            return
        if password != re_password:
            self.finish_json(1, u'两次密码不一致')
            return
        if not department:
            self.finish_json(1, u'请输入部门')
            return
        if not mobile:
            self.finish_json(1, u'请输入手机号')
            return
        if authority & PERMISSIONS.admin or authority & PERMISSIONS.root:
            self.finish_json(1, u'不允许添加管理员用户')
            return

        user = UserModel.get_user_by_merchantid_username(
            self.db, merchant_id, username)

        if user:
            self.finish_json(1, u'用户名已被使用')
        else:
            UserModel.add_user(self.db, merchant_id, username,
                               password, department, mobile, authority, is_valid, hotel_id)
            self.finish_json(0, u'添加成功')

    @staticmethod
    def mobile_check(mobile):
        checker = re.compile(r"^1\d{10}$")
        if checker.match(mobile):
            return True
        return False


class MerchantCoopedHotelAPIHandler(HotelCoopedAPIHandler):
    @gen.coroutine
    @auth_login(json=True)
    @auth_permission(PERMISSIONS.admin, json=True)
    def get(self):
        if self.merchant.type == MerchantModel.TYPE_TRAVEL_AGENCY:
            start = 0
            limit = 500
            hotels = []
            hotels_, total = yield self.get_cooped_hotels(self.current_user.merchant_id, start, limit,
                                                          None, None, None, None, None)
            hotels.extend(hotels_)
            while start + limit < total and len(hotels_) in range(1, limit + 1):
                start += limit
                hotels_, total = yield self.get_cooped_hotels(self.current_user.merchant_id, start, limit,
                                                              None, None, None, None, None)
                hotels.extend(hotels_)
            self.finish_json(result=dict(hotels=hotels))
        else:
            self.finish_json(result=dict(hotels=[]))