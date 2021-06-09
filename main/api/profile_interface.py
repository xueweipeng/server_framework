from flask import jsonify, app
from flask import Blueprint
from flask import request
from werkzeug.utils import secure_filename
from flask import Flask, render_template, jsonify, request, send_from_directory
import time
import os
import base64

from main.api import network_constants
from main.common import business_util
from main.common.logger import Logger

profile = Blueprint("profile", __name__)

basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'jpeg', 'JPEG'])
logger = Logger("profile_interface")


# 设置头像
@profile.route('/set_avatar', methods=['POST'], strict_slashes=False)
def upload_avatar():
    file_dir = os.path.join(basedir, 'upload_avatar')
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['myavatar']  # 从表单的file字段获取文件，myfile为该表单的name值

    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname = secure_filename(f.filename)
        logger.debug(fname)
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        # new_filename = str(unix_time)+'.'+ext  # 修改了上传的文件名
        new_filename = '12' + '.' + ext  # 修改了上传的文件名
        f.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录

        return jsonify({"errno": 0, "errmsg": "上传成功"})
    else:
        return jsonify({"errno": 1001, "errmsg": "上传失败"})


# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 上传资料
@profile.route('/upload_profile', methods=['POST'])
def upload_profile():
    data = request.get_json()
    token = data.get("token")

    print("data = %s" % data)
    return jsonify(data)


# 获取资料
@profile.route('/get_profile', methods=['GET'])
def get_profile():
    data = request.args
    token = data.get("token")
    print("token = %s" % token)
    # 用token解密后查询用户资料
    user = business_util.getUserFromToken(token)
    if user is not None:
        data = {
            "data": {
                "avatar": user.getAvatar(),
                "nick_name": user.getNickName(),
                "signature": user.getSignature(),
                "sex": user.getSex(),
                "birthday": user.getBirthday(),
                "education": user.getEducation(),
                "industry": user.getIndustry(),
            },
            "code": network_constants.CODE_SUCCESS,
            "message": network_constants.MESSAGE_SUCCESS
        }
    else:
        data = {
            "data": {

            },
            "code": network_constants.CODE_FAIL,
            "message": network_constants.MESSAGE_USER_NOT_FOUND
        }
    return jsonify(data)
