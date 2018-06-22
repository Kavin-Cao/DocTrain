from flask_login import UserMixin

from models.base_model import BaseModel
from DocTrain import DocTrainDB as db


class User(BaseModel, UserMixin):
    user_name = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(64))
    email = db.Column(db.String(64))
    mobile = db.Column(db.String(16), nullable=False, unique=True)
    nickname = db.Column(db.String(64))
    avatar = db.Column(db.String(200))


class UserLoginLog(BaseModel):
    user_id = db.Column(db.INTEGER, nullable=False)
    log_msg = db.Column(db.String(100))
    ip = db.Column(db.String(16))
