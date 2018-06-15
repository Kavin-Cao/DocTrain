import datetime
from flask import Flask, render_template
from flask_cache import Cache
from flask_sqlalchemy import SQLAlchemy
from models import init_db
import views

DocTrainApp = Flask(__name__)
DocTrainApp.config.from_pyfile("conf.py", False)


DocTrainCache = Cache()
DocTrainCache.init_app(DocTrainApp)


DocTrainDB = SQLAlchemy(DocTrainApp)


@DocTrainApp.route('/')
@DocTrainCache.cached(timeout=30*60)
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    init_db.init_db()
    DocTrainApp.run()
