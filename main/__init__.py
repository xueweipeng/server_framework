from flask import Flask

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
    from main.api.modbusInterface import modbus
    app.register_blueprint(modbus, url_prefix='/modbus')
    return app


application = Flask(__name__)
app = register_route(application)

