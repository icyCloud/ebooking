# -*- coding: utf-8 -*-

from base import BtwBaseHandler
from tornado.escape import json_encode
from models.user_hotel_mapping import UserHotelMappingModel
from tools.auth import auth_login, auth_permission
from constants import PERMISSIONS
from models.user import UserModel

class UserManageHandler(BtwBaseHandler):

    @auth_login()
    @auth_permission(PERMISSIONS.admin)
    def get(self):
        users = UserModel.get_users_by_merchant_id(self.db, self.current_user.merchant_id)
        mappings = UserHotelMappingModel.get_hotel_by_id(self.db, None, self.current_user.merchant_id)
        if mappings:
            map_ids = {map.user_id: map.hotel_id for map in mappings}
            for user in users:
                user.hotel_id = map_ids.get(user.id)
        self.render("userManage.html", users=json_encode([user.todict() for user in users]))