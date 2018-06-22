from models.base_model import BaseModel

from DocTrain import DocTrainDB as db
from models.doc_models import Document


class Project(BaseModel):

    # 项目名称
    name = db.Column(db.String(30), nullable=False, unique=True)
    # 创建人User.id
    created_by = db.Column(db.INTEGER, nullable=False)
    # 项目说明
    description = db.Column(db.TEXT)
    # 项目说明的文档类型
    des_doc_type = db.Column(db.Enum(Document.DocType))
    # 项目logo
    logo = db.Column(db.String(200))


class ProjectUsers(BaseModel):

    # 项目Project.id
    project_id = db.Column(db.INTEGER, nullable=False)
    # 用户User.id
    user_id = db.Column(db.INTEGER, nullable=False)


class ProjectDocuments(BaseModel):

    # 项目Project.id
    project_id = db.Column(db.INTEGER, nullable=False)
    # 文档document.id
    document_id = db.Column(db.INTEGER, nullable=False)