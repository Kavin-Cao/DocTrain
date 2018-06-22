from flask import Blueprint, render_template
from flask_login import login_required

from DocTrain import DocTrainDB as db
from models.doc_models import Document
from models.project_models import Project, ProjectUsers, ProjectDocuments
from models.user_models import User

from flask import Markup

blueprint = Blueprint('project', __name__, url_prefix='/project')


@blueprint.route('/<int:project_id>', methods=['GET'])
@blueprint.route('/<int:project_id>/<tab>', methods=['GET'])
@login_required
def project(project_id, tab=None):
    data = dict()
    if not tab:  # 项目详情
        _project = Project.query.filter_by(id=project_id,is_deleted=False).first()
        # 创建人
        created_user = User.query.filter_by(id=_project.created_by)
        data = {
            "project": dict(
                id=_project.id,
                modified=_project.modified,
                name=_project.name,
                description=_project.description,
                des_doc_type=_project.des_doc_type,
                logo=_project.logo,
                created_by=_project.created_by,
                created=_project.created,
                created_user=created_user
            )
        }
    elif tab == 'users':  # 项目用户管理
        pro_users = ProjectUsers.query.filter_by(project_id=project_id).all()
        user_ids = [user.user_id for user in pro_users]
        if len(user_ids) > 0:
            uesrs = User.query.filter(User.id.in_(user_ids))
        data = {
            "users": uesrs
        }
    elif tab == 'docs':  # 项目文档管理
        pro_documents = ProjectDocuments.query.filter_by(project_id=project_id).all()
        document_ids = [document.document_id for document in pro_documents]
        documents = []
        if len(document_ids) > 0:
            documents = Document.query.filter(Document.id.in_(document_ids)).all()
        data = {
            "documents": documents
        }
    data["project_id"] = project_id
    data["tab"] = tab
    return render_template("/project/project.html", **data)
