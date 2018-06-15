import re
from sqlalchemy.ext.declarative import AbstractConcreteBase, declared_attr
from DocTrain import DocTrainDB as db


class BaseModel(AbstractConcreteBase, db.Model):
    """ 为所有Model提供公用方法 """

    id = db.Column(db.INTEGER, primary_key=True, autoincrement="auto increment")
    created = db.Column(db.DATETIME, nullable=False)
    modified = db.Column(db.DATETIME, nullable=False)
    is_deleted = db.Column(db.BOOLEAN, nullable=False, default=True)
    deleted = db.Column(db.DATETIME)
    deleted_by = db.Column(db.String(50))

    @declared_attr
    def __tablename__(cls):
        hunp_str = cls.__name__
        p = re.compile(r'([a-z]|\d)([A-Z])')
        # 这里第二个参数使用了正则分组的后向引用
        tablename = re.sub(p, r'\1_\2', hunp_str).lower()
        return "dt_" + tablename
