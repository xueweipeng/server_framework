from flask import Blueprint, request, jsonify

camera = Blueprint("camera", __name__)


# 启动摄像头
@camera.route('/start', methods=['POST'])
def startCamera():
    ret_code = 0

    # todo 不断将预览帧写入文件，每三分钟覆盖一次
    #     ret_code = 1
    if ret_code == 0:
        ret = {'url': '预览地址'}
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1,
            "data": ret
        }
    else:

        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


# 拍照
@camera.route('/snapshot', methods=['POST'])
def stopCamera():
    ret_code = 0

    # ret_code = 1
    if ret_code == 0:
        ret = {'url': '图片地址'}
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1,
            "data": ret
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)
