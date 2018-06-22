from flask import Flask
from flask_cache import Cache
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from markdown.extensions.wikilinks import WikiLinkExtension

DocTrainApp = Flask(__name__)
DocTrainApp.config.from_pyfile("conf.py", False)

DocTrainDB = SQLAlchemy()
DocTrainDB.init_app(DocTrainApp)

from models import init_db
from models.user_models import User

DocTrainCache = Cache()
DocTrainCache.init_app(DocTrainApp)

login_manager = LoginManager()


@login_manager.user_loader
def load_user(userid):
    return User.query.filter_by(id=userid).first()


login_manager.login_view = "/login"
login_manager.init_app(DocTrainApp)

from views.index import blueprint as index_blueprint
from views.project import blueprint as project_blueprint

DocTrainApp.register_blueprint(index_blueprint)
DocTrainApp.register_blueprint(project_blueprint)

if __name__ == '__main__':
    init_db.init_db()
    DocTrainApp.run()
