import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
1、获取课程信息接口（参数：无）
2、获取验证码接口（参数：手机号码）
3、注册接口（参数：手机号码，获取的验证码）
4、设置密码接口（参数：手机号码，密码）
5、找回密码接口（参数：手机号码）
6、上传头像接口（参数：手机号码，图片）
7、上传个人资料接口（参数：手机号码，信息（昵称，性别，生日等）
8、用户名密码登录接口
"""


def register_route(app):
    from main.api.sub_business_1 import bp_business1
    app.register_blueprint(bp_business1, url_prefix='/business1')
    from main.api.sub_business_2 import bp_business2
    app.register_blueprint(bp_business2, url_prefix='/business2')
    from main.api.login_interface import login
    app.register_blueprint(login, url_prefix='/login')
    from main.api.lesson_interface import lesson
    app.register_blueprint(lesson, url_prefix='/lesson')
    from main.api.profile_interface import profile
    app.register_blueprint(profile, url_prefix='/profile')
    from main.api.upgrade_interface import upgrade
    app.register_blueprint(upgrade, url_prefix='/upgrade')
    from main.api.modbus_interface import modbus
    app.register_blueprint(modbus, url_prefix='/modbus')
    from main.api.camera_interface import camera
    app.register_blueprint(camera, url_prefix='/camera')
    return app


db = SQLAlchemy()
application = Flask(__name__)
app = register_route(application)
# 初始化App配置
# SQLALCHEMY_DATABASE_URI 配置 SQLAlchemy 的链接字符串儿
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.getcwd() + os.path.sep + "picFile.db"
# SQLALCHEMY_POOL_SIZE 配置 SQLAlchemy 的连接池大小
# app.config["SQLALCHEMY_POOL_SIZE"] = 5
# SQLALCHEMY_POOL_TIMEOUT 配置 SQLAlchemy 的连接超时时间
# app.config["SQLALCHEMY_POOL_TIMEOUT"] = 15
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
if not os.path.exists(os.getcwd() + os.path.sep + "picFile.db"):
    db.create_all(app=app)
