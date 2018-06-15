from DocTrain import DocTrainDB
from DocTrain import DocTrainApp
from models import user_models
from models import doc_models
from models import sys_models

def init_db():
    DocTrainDB.create_all(app=DocTrainApp)
