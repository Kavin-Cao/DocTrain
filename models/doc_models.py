from models.base_model import BaseModel

from DocTrain import DocTrainDB as db
from enum import Flag


class Document(BaseModel):

    class DocType(Flag):
        PLAIN_TEXT = 0,
        HTML = 1,
        MARKDOWN = 2

    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.TEXT)
    doc_type = db.Column(db.Enum(DocType))

