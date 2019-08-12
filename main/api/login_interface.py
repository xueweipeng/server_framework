from flask import jsonify
from flask import Blueprint
from flask import request

login = Blueprint("login", __name__)


# 获取验证码 /authcode?phone=10086
@login.route('/authcode', methods=['GET'])
def get_auth_code():
    phone = request.args.get('phone')
    data = {
        "data": {
            "auth": 1111
        },
        "code": 200,
        "message": "success"
    }
    return jsonify(data)


# 用户登录 参数为用户名和密码
@login.route('/user', methods=['GET'])
def user_login():
    user_name = request.args.get('user_name')
    password = request.args.get('password')
    data = {
        "data": {
            "user": {
                "name": user_name,
                "sex": "male",
                "phone": "18519661369",
                "avatar": "http://www.ecfo.com.cn/img2/elevenV.png",
                "birth": "1900/01/01",
                "signature": "我思故我在",
                "token": "1212asfasdfasdfsdf"
            }
        },
        "code": 200,
        "message": "success"
    }
    return jsonify(data)


# 用户注册 参数为手机号与验证码
@login.route('/register', methods=['GET'])
def user_register():
    phone = request.args.get('phone')
    authcode = request.args.get('authcode')
    data = {
        "data": {
        },
        "code": 200,
        "message": "success"

    }
    return jsonify(data)


# 设置密码 参数为手机号和密码（两次密码）
@login.route('/setpassword', methods=['GET'])
def set_password():
    phone = request.args.get('phone')
    password1 = request.args.get('password1')
    password2 = request.args.get('password2')
    data = {
        "data": {
        },
        "code": 200,
        "message": "success"

    }
    return jsonify(data)


# 找回密码
@login.route('/findpassword', methods=['GET'])
def find_password():
    phone = request.args.get('phone')
    data = {
        "data": {
            "auth": 1111
        },
        "code": 200,
        "message": "success"

    }
    return jsonify(data)
