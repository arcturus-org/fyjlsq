from flask import Blueprint, Flask
from .authorize import auth_blueprint
from .articles import article_blueprint

api_v1 = Blueprint("api/v1", __name__, url_prefix="/api/v1")


def blueprint_init(app: Flask):
    # 注册蓝图
    api_v1.register_blueprint(auth_blueprint)
    api_v1.register_blueprint(article_blueprint)

    app.register_blueprint(api_v1)
