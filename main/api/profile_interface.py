from flask import jsonify
from flask import Blueprint

profile = Blueprint("profile", __name__)


# 设置头像
@profile.route('/avatar', methods=['POST'])
def upload_avatar():
    data = {
        "username": "rale",
        "age": 18,
        "desc": "this is profile!!"
    }
    return jsonify(data)


# 上传资料
@profile.route('/profile', methods=['POST'])
def upload_profile():
    data = {
        "username": "rale",
        "age": 18,
        "desc": "this is profile!!"
    }
    return jsonify(data)
