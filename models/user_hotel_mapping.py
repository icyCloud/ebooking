# -*- coding: utf-8 -*-

from tornado.util import ObjectDict

from models import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIT, INTEGER, VARCHAR, BIGINT, TINYINT
from tools.auth import md5_password
from constants import PERMISSIONS


class UserHotelMappingModel(Base):
    __tablename__ = 'user_hotel_mapping'
    __table_args__ = {
        'mysql_charset': 'utf8', 'mysql_engine': 'InnoDB'}

    id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    merchant_id = Column(INTEGER(11), nullable=False, default=0)
    user_id = Column(INTEGER(10), nullable=False, default=0)
    hotel_id = Column(INTEGER(11), nullable=False, default=0)

    @classmethod
    def get_hotel_by_id(cls, session, user_id=None, merchant_id=None, hotel_id=None):
        query = session.query(UserHotelMappingModel)
        if user_id:
            query = query.filter(UserHotelMappingModel.user_id == user_id)
        if merchant_id:
            query = query.filter(UserHotelMappingModel.merchant_id == merchant_id)
        if hotel_id:
            query = query.filter(UserHotelMappingModel.hotel_id == hotel_id)
        return query.all()

    def todict(self):
        return ObjectDict(
            id=self.id,
            merchant_id=self.merchant_id,
            user_id=self.uer_id,
            hotel_id=self.hotel_id,
        )
