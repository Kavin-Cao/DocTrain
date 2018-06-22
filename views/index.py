import hashlib

import flask
from flask import render_template, Blueprint, request, session
from flask_login import login_user, login_required
from sqlalchemy import or_

from models.project_models import Project, ProjectUsers
from models.user_models import User
from utils import is_safe_url
from views import KEY_SESSION_USER

blueprint = Blueprint('index', __name__, url_prefix='/')


@blueprint.route('/')
@blueprint.route('/index')
@login_required
def index():
    # 查询出用户的projects
    session_user = dict(session.get(KEY_SESSION_USER))
    user_id = session_user.get("id")
    project_users = ProjectUsers.query.filter_by(user_id=user_id).all()
    project_ids = [project.id for project in project_users]
    projects = Project.query.filter(Project.id.in_(project_ids)).all()

    project_dicts = [
        dict(
            id=project.id,
            name=project.name,
            logo=project.logo
        ) for project in projects
    ]
    session_user['projects'] = project_dicts
    session[KEY_SESSION_USER] = session_user
    return render_template("index.html")


@blueprint.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        login_account = request.form.get("login_account")
        login_passwd = request.form.get("login_passwd")

        user = User.query.filter(or_(User.user_name == login_account, User.mobile == login_account)).first()
        if not user:
            return render_template("login.html", **{
                "message": "账户不存在"
            })

        password = user.password
        if hashlib.md5(login_passwd.encode("utf-8")).hexdigest() != password:
            return render_template("login.html", **{
                "message": "密码错误"
            })

        login_flag = login_user(user, remember=request.form.get("remembr_me"))
        if login_flag:
            session_user = dict(
                id=user.id,
                user_name=user.user_name,
                nickname=user.nickname,
                mobile=user.mobile,
                email=user.email,
                avatar=user.avatar,
            )
            session[KEY_SESSION_USER] = session_user
            next = flask.request.args.get('next')
            if not is_safe_url(next):
                return flask.abort(400)
            return flask.redirect(next or "/index")
        return render_template("login.html", **{
            "message": "登陆失败"
        })

