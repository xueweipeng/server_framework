from flask import jsonify
from flask import Blueprint

profile = Blueprint("profile", __name__)


# 设置头像
@profile.route('/set_avatar', methods=['POST'])
def upload_avatar():
    data = {
        "username": "rale",
        "age": 18,
        "desc": "this is profile!!"
    }
    return jsonify(data)


# 上传资料
@profile.route('/upload_profile', methods=['POST'])
def upload_profile():
    data = {
        "username": "rale",
        "age": 18,
        "desc": "this is profile!!"
    }
    return jsonify(data)


# 获取资料
@profile.route('/get_profile', methods=['GET'])
def get_profile():
    data = {
        "username": "weapon",
        "age": 18,
        "desc": "this is get_profile!!"
    }
    return jsonify(data)
