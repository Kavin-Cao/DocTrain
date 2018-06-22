from models.base_model import BaseModel

from DocTrain import DocTrainDB as db
from enum import IntEnum


class Document(BaseModel):

    class DocType(IntEnum):
        PLAIN_TEXT = 0,
        HTML = 1,
        MARKDOWN = 2

    # 文档标题
    title = db.Column(db.String(100), nullable=False)
    # 文档内容
    content = db.Column(db.TEXT)
    # 文档类型
    doc_type = db.Column(db.Enum(DocType))
    # 创建人User.id
    created_by = db.Column(db.INTEGER, nullable=False)


class DocumentModifiedLog(BaseModel):

    # 文档document.id
    document_id = db.Column(db.INTEGER, nullable=False)
    # 修改人User.id
    modified_by = db.Column(db.INTEGER, nullable=False)
    # 原始文档内容
    original_content = db.Column(db.TEXT)
    # 修改后文档内容
    modified_content = db.Column(db.TEXT)
