# -*- coding: utf-8 -*-

from tornado.util import ObjectDict

from models import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIT, INTEGER, VARCHAR, BIGINT, TINYINT
from models.user_hotel_mapping import UserHotelMappingModel
from tools.auth import md5_password
from constants import PERMISSIONS
from tools.log import Log


class UserModel(Base):
    __tablename__ = 'user'
    __table_args__ = {
        'mysql_charset': 'utf8', 'mysql_engine': 'InnoDB'}

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    merchant_id = Column("merchantId", INTEGER, nullable=False, default=0)
    username = Column(VARCHAR(50), nullable=False)
    nickname = Column(VARCHAR(50), nullable=False, default='')
    password = Column(VARCHAR(50), nullable=False)
    department = Column(VARCHAR(50), nullable=False, default='')
    mobile = Column(VARCHAR(50), nullable=False, default='')
    email = Column(VARCHAR(50), nullable=False, default='')
    authority = Column(BIGINT, nullable=False, default=0)
    is_valid = Column('isValid', BIT, nullable=False, default=1)
    is_delete = Column('isDelete', BIT, nullable=False, default=0)
    type = Column(TINYINT(1), nullable=False, default=0)
    hotel_id = None

    TYPE_NORMAL = 0
    TYPE_ADMIN = 1
    TYPE_ROOT = 2
    TYPE_SUB = 3

    @classmethod
    def get_user_by_id(cls, session, id):
        return session.query(UserModel).filter(UserModel.id == id, UserModel.is_delete == 0).first()

    @classmethod
    def get_users_by_id(cls, session, ids):
        return session.query(UserModel).filter(UserModel.id.in_(ids)).filter(UserModel.is_delete == 0).all()

    @classmethod
    def get_user_by_merchantid_username(cls, session, merchant_id, username):
        return session.query(UserModel) \
            .filter(UserModel.username == username, UserModel.merchant_id == merchant_id, UserModel.is_delete == 0) \
            .first()

    @classmethod
    def get_user_by_merchantid_username_and_password(cls, session, merchant_id, username, password):
        password = md5_password(password)
        return session.query(UserModel) \
            .filter(UserModel.merchant_id == merchant_id, UserModel.username == username,
                    UserModel.password == password,
                    UserModel.is_delete == 0, UserModel.is_valid == 1) \
            .first()

    @classmethod
    def get_users_by_merchant_id(cls, session, merchant_id, hide_root=True):
        query = session.query(UserModel) \
            .filter(UserModel.merchant_id == merchant_id, UserModel.is_delete == 0)
        if hide_root:
            query = query.filter(UserModel.type != cls.TYPE_ROOT)
        return query.all()

    @classmethod
    def new_admin_root_user(cls, session, merchant_id, admin_pwd, root_pwd):
        admin_pwd = md5_password(admin_pwd)
        root_pwd = md5_password(root_pwd)
        admin = UserModel(merchant_id=merchant_id, username='admin', password=admin_pwd, authority=PERMISSIONS.admin,
                          type=cls.TYPE_ADMIN)
        root = UserModel(merchant_id=merchant_id, username='root', password=root_pwd,
                         authority=PERMISSIONS.root | PERMISSIONS.admin, type=cls.TYPE_ROOT)
        session.add_all([admin, root])
        session.commit()
        return admin, root

    @classmethod
    def update_user(cls, session, merchant_id, username, password, department, mobile, email, is_valid, authority=None,
                    hotel_id=None):
        if password:
            password = md5_password(password)
        user = cls.get_user_by_merchantid_username(session, merchant_id, username)
        if user:
            if password:
                user.password = password
            user.department = department
            user.mobile = mobile
            if email:
                user.email = email
            if authority:
                user.authority = authority
            user.is_valid = is_valid
            session.flush()
            if hotel_id:
                map_hotel = UserHotelMappingModel.get_hotel_by_id(session, user.id, user.merchant_id)
                if map_hotel:
                    if str(is_valid) == '1':
                        map_hotel[0].hotel_id = hotel_id
                    else:
                        session.delete(map_hotel[0])
                else:
                    if str(is_valid) == '1':
                        mapping = UserHotelMappingModel(merchant_id=merchant_id, user_id=user.id, hotel_id=hotel_id)
                        session.add(mapping)
            session.commit()

    @classmethod
    def update_password(cls, session, merchant_id, username, password):
        password = md5_password(password)
        user = cls.get_user_by_merchantid_username(session, merchant_id, username)
        if user:
            user.password = password
            session.commit()
        return user

    @classmethod
    def add_user(cls, session, merchant_id, username, password, department, mobile, authority, is_valid, hotel_id=None):
        password = md5_password(password)
        user = UserModel(merchant_id=merchant_id, username=username, nickname='', password=password,
                         department=department,
                         mobile=mobile, email='', authority=authority, is_valid=is_valid)
        if hotel_id is not None:
            user.type = UserModel.TYPE_SUB
        session.add(user)
        session.commit()
        Log.info(user.todict())
        mapping = UserHotelMappingModel(merchant_id=merchant_id, user_id=user.id, hotel_id=hotel_id)
        session.add(mapping)
        session.commit()
        return user

    def todict(self):
        return ObjectDict(
            id=self.id,
            merchant_id=self.merchant_id,
            username=self.username,
            nickname=self.nickname,
            department=self.department,
            mobile=self.mobile,
            email=self.email,
            authority=self.authority,
            is_valid=self.is_valid,
            is_delete=self.is_delete,
            type=self.type,
            hotel_id=self.hotel_id,
        )
