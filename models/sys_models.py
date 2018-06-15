from enum import Flag

from models.base_model import BaseModel

from DocTrain import DocTrainDB as db


class SysSetting(BaseModel):
    class Section(Flag):
        SYSTEM = 0,
        DOCUMENT = 0,
        USER = 0,

    section = db.Column(db.Enum(Section), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.TEXT)
    desc = db.Column(db.String(200))
