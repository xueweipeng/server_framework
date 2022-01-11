import _thread
import logging
import os
import time

import requests
from flask import Blueprint, request, jsonify

from main.api import ThreadFlag

camera = Blueprint("camera", __name__)

streamUrl = "http://192.168.137.2:8090/?action=stream"
snapUrl = "http://192.168.137.2:8090/?action=snapshot"
taskInterval = 1  # 一秒一次


def preview(name, count):
    while ThreadFlag.exitFlag:
        r = requests.get(snapUrl)
        img = r.content
        filename = time.strftime("%Y-%m-%d-%H-%M-%S-preview.jpg", time.localtime())
        # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
        with open('runtime/' + filename, 'wb') as f:
            f.write(img)

        if os.path.getsize('runtime/' + filename) > 0:
            print('预览保存成功')
        else:
            print('预览保存失败')
        time.sleep(taskInterval)


# 启动摄像头
@camera.route('/start', methods=['POST'])
def startCamera():
    try:
        ThreadFlag.exitFlag = True
        _thread.start_new_thread(preview, ("preview", 2))
    except Exception as e:
        print("启动线程失败" + e.__str__())

    ret_code = 1
    if ret_code == 0:
        ret = {'filename': ''}
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


@camera.route('/stop', methods=['POST'])
def stopCamera():
    print('停止预览截图任务')
    ThreadFlag.exitFlag = False
    ret_data = {
        "code": 0,
        "message": "success",
        "success": 1
    }
    return jsonify(ret_data)


# 拍照
@camera.route('/snapshot', methods=['POST'])
def snapShot():
    r = requests.get(snapUrl)
    logging.debug(r)
    img = r.content
    filename = time.strftime("%Y-%m-%d-%H-%M-%S-snapshot.jpg", time.localtime())
    # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
    with open('snapshot/' + filename, 'wb') as f:
        f.write(img)

    if os.path.getsize('snapshot/' + filename) > 0:
        ret_code = 0
    else:
        ret_code = 1

    # ret_code = 1
    if ret_code == 0:
        ret = {'filename': filename}
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
