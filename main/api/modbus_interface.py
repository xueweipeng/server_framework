import socket
import time

import modbus_tk
import modbus_tk.modbus_tcp as modbus_tcp
import numpy as numpy
from flask import Blueprint, request, jsonify
import modbus_tk.defines as cst
import struct

from pyModbusTCP import utils

from main.api.cal import WriteFloat, ReadFloat

logger = modbus_tk.utils.create_logger("console")

modbus = Blueprint("modbus", __name__)
modbus_address = "192.168.137.2"
move_action_key = "verticalPointMove"

# 连接MODBUS TCP从机
master = modbus_tcp.TcpMaster(host=modbus_address, port=502)
logger.info("modbus connected")
try:
    logger.info("hello modbus")
    # 写寄存器 起始地址为8的保持寄存器，操作寄存器个数为 4 ，一个浮点数float 占两个寄存器;
    # 写浮点数时一定要加 data_format 参数，两个ff 表示要写入两个浮点数，以此类推
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 1, output_value=[1.00], data_format='<f')
    # logger.info("1 = %s" % master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 2, data_format='<f'))
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 1, output_value=WriteFloat(1))
    logger.info("3 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 3, output_value=WriteFloat(10))
    logger.info("3 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 3, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 5, output_value=WriteFloat(20))
    logger.info("5 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 5, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 7, output_value=WriteFloat(1))
    logger.info("7 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 7, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 9, output_value=WriteFloat(2.00))
    logger.info("9 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 9, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 11, output_value=WriteFloat(1.00))
    logger.info("11 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 11, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 13, output_value=WriteFloat(0.000100))
    logger.info("13 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 13, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 15, output_value=WriteFloat(0.000100))
    logger.info("15 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 15, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 23, output_value=WriteFloat(400))
    logger.info("23 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 23, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 25, output_value=WriteFloat(8.00))
    logger.info("25 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 25, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 27, output_value=WriteFloat(0.00))
    logger.info("27 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 27, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 43, output_value=WriteFloat(5))
    logger.info("43 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 43, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 45, output_value=WriteFloat(0.01))
    logger.info("45 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 45, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 47, output_value=WriteFloat(1.00))
    logger.info("47 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 47, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 49, output_value=WriteFloat(1.00))
    logger.info("49 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 49, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 51, output_value=WriteFloat(1.00))
    logger.info("51 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 51, 2)))
    time.sleep(0.1)
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 53, output_value=WriteFloat(1.00))
    logger.info("53 = %s" % ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 53, 2)))
    time.sleep(0.1)
    # walkCurrentPosition = ReadFloat(master.execute(1, cst.READ_INPUT_REGISTERS, 5, 2))
    # time.sleep(0.1)
except modbus_tk.modbus.ModbusError as e:
    logger.error("%s- Code=%d" % (e, e.get_exception_code()))
except socket.timeout as e1:
    logger.error("timeout")
    ret_code = 1


# 行走点动前进
@modbus.route('/frontPointMoveAction', methods=['POST'])
def front_point_move_action():
    data = request.get_json()
    # 1 启动 0 停止
    action = data.get(move_action_key)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 10, output_value=0)
        master.execute(1, cst.WRITE_SINGLE_COIL, 0, output_value=1)  # 行走使能
        time.sleep(0.1)
        master.execute(1, cst.WRITE_SINGLE_COIL, 15, output_value=0)  # 行走模式
        time.sleep(0.1)
        master.execute(1, cst.WRITE_SINGLE_COIL, 10, output_value=action)  # 行走点动前进

    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


# 行走点动后退
@modbus.route('/backPointMoveAction', methods=['POST'])
def back_point_move_action():
    data = request.get_json()
    # 1 启动 0 停止
    action = data.get(move_action_key)
    logger.info("action = %d" % action)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 11, output_value=0)
        c01 = master.execute(1, cst.READ_COILS, 0, 1)
        if c01[0] == 0:
            master.execute(1, cst.WRITE_SINGLE_COIL, 0, output_value=1)
        c16 = master.execute(1, cst.READ_COILS, 15, 1)
        if c16[0] == 1:
            master.execute(1, cst.WRITE_SINGLE_COIL, 15, 0)
        master.execute(1, cst.WRITE_SINGLE_COIL, 11, output_value=action)
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


@modbus.route('/frontbackPointMoveAction', methods=['POST'])
def front_back_point_move_action():
    data = request.get_json()
    # 1 启动 0 停止
    action = data.get(move_action_key)
    logger.info("action = %d" % action)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 0, output_value=1)
        time.sleep(0.1)
        master.execute(1, cst.WRITE_SINGLE_COIL, 5, output_value=action)
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


@modbus.route('/frontbackPointStopAction', methods=['POST'])
def front_back_point_stop_action():
    data = request.get_json()
    # 1 启动 0 停止
    action = data.get(move_action_key)
    logger.info("action = %d" % action)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 6, output_value=action)

    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


@modbus.route('/setting', methods=['POST'])
def setting():
    data = request.get_json()
    # 1 启动 0 停止
    finallyTension = data.get("finallyTension")
    logger.info("data = %s" % data)
    finallyTensionTime = data.get("finallyTensionTime")
    walkLength = float(data.get("walkLength"))
    walkSpeed = data.get("walkSpeed")
    zeroLocation = data.get("zeroLocation")
    tensionFactor = data.get("tensionFactor")
    tensionOffset = data.get("tensionOffset")
    pullFactor = data.get("pullFactor")
    pullOffset = data.get("pullOffset")
    Kp = data.get("Kp")
    Tn = data.get("Tn")
    Tv = data.get("Tv")
    tensionDegreeSetting = data.get("tensionDegreeSetting")
    tensionTimeSetting = data.get("tensionTimeSetting")
    walkDeceleratorNumerator = data.get("walkDeceleratorNumerator")
    walkDeceleratorDenominator = data.get("walkDeceleratorDenominator")
    travelingAxleLength = data.get("travelingAxleLength")
    tensionReductionNumerator = data.get("tensionReductionNumerator")
    tensionReductionDeNumerator = data.get("tensionReductionDeNumerator")
    tensionShaftPitch = data.get("tensionShaftPitch")
    walkingAcceleration = data.get("walkingAcceleration")
    walkingDeacceleration = data.get("walkingDeacceleration")
    tensionPointSpeed = data.get("tensionPointSpeed")
    walkPointSpeed = data.get("walkPointSpeed")
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 37, output_value=WriteFloat(finallyTension))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 33, output_value=WriteFloat(finallyTensionTime))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 19, output_value=WriteFloat(walkLength))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 21, output_value=WriteFloat(walkSpeed))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 31, output_value=WriteFloat(zeroLocation))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 47, output_value=WriteFloat(tensionFactor))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 49, output_value=WriteFloat(tensionOffset))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 51, output_value=WriteFloat(pullFactor))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 53, output_value=WriteFloat(pullOffset))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 23, output_value=WriteFloat(Kp))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 25, output_value=WriteFloat(Tn))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 27, output_value=WriteFloat(Tv))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 29, output_value=WriteFloat(tensionDegreeSetting))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 39, output_value=WriteFloat(tensionTimeSetting))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 1, output_value=WriteFloat(walkDeceleratorNumerator))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 3, output_value=WriteFloat(walkDeceleratorDenominator))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 5, output_value=WriteFloat(travelingAxleLength))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 7, output_value=WriteFloat(tensionReductionNumerator))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 9, output_value=WriteFloat(tensionReductionDeNumerator))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 11, output_value=WriteFloat(tensionShaftPitch))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 13, output_value=WriteFloat(walkingAcceleration))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 15, output_value=WriteFloat(walkingDeacceleration))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 43, output_value=WriteFloat(tensionPointSpeed))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 45, output_value=WriteFloat(walkPointSpeed))

    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


@modbus.route('/readData', methods=['POST'])
def readData():
    ret_code = 0
    ret = {}
    try:
        finallyTension = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 37, 2))
        finallyTensionTime = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 33, 2))
        walkLength = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 19, 2))
        walkSpeed = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 21, 2))
        zeroLocation = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 31, 2))
        tensionFactor = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 47, 2))
        tensionOffset = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 49, 2))
        pullFactor = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 51, 2))
        pullOffset = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 53, 2))
        Kp = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 23, 2))
        Tn = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 25, 2))
        Tv = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 27, 2))
        tensionDegreeSetting = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 29, 2))
        tensionTimeSetting = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 39, 2))
        walkDeceleratorNumerator = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 2))
        walkDeceleratorDenominator = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 3, 2))
        travelingAxleLength = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 5, 2))
        tensionReductionNumerator = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 7, 2))
        tensionReductionDeNumerator = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 9, 2))
        tensionShaftPitch = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 11, 2))
        walkingAcceleration = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 13, 2))
        walkingDeacceleration = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 15, 2))
        tensionPointSpeed = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 43, 2))
        walkPointSpeed = ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 45, 2))
        walk1States = master.execute(1, cst.READ_INPUT_REGISTERS, 1, 1)[0]
        walk2States = master.execute(1, cst.READ_INPUT_REGISTERS, 2, 1)[0]
        walk3States = master.execute(1, cst.READ_INPUT_REGISTERS, 3, 1)[0]
        tensionState = master.execute(1, cst.READ_INPUT_REGISTERS, 4, 1)[0]
        walkCurrentPosition = ReadFloat(master.execute(1, cst.READ_INPUT_REGISTERS, 5, 2), reverse=False)
        walkForce = ReadFloat(master.execute(1, cst.READ_INPUT_REGISTERS, 45, 2), reverse=False)  # 行走拉力
        tensionForce = ReadFloat(master.execute(1, cst.READ_INPUT_REGISTERS, 44, 2), reverse=True)
        walkPointState = ReadFloat(master.execute(1, cst.READ_INPUT_REGISTERS, 48, 2), reverse=True)  # 张紧轴当前位置
        walkEnable = master.execute(1, cst.READ_COILS, 0, 1)[0]
        walkStatus = master.execute(1, cst.READ_COILS, 15, 1)[0]
        ret["finallyTension"] = finallyTension
        ret["finallyTensionTime"] = finallyTensionTime
        ret["walkLength"] = walkLength
        ret["walkSpeed"] = walkSpeed
        ret["zeroLocation"] = zeroLocation
        ret["tensionFactor"] = tensionFactor
        ret["tensionOffset"] = tensionOffset
        ret["pullFactor"] = pullFactor
        ret["pullOffset"] = pullOffset
        ret["Kp"] = Kp
        ret["Tn"] = Tn
        ret["Tv"] = Tv
        ret["tensionDegreeSetting"] = tensionDegreeSetting
        ret["tensionTimeSetting"] = tensionTimeSetting
        ret["walkDeceleratorNumerator"] = walkDeceleratorNumerator
        ret["walkDeceleratorDenominator"] = walkDeceleratorDenominator
        ret["travelingAxleLength"] = travelingAxleLength
        ret["tensionReductionNumerator"] = tensionReductionNumerator
        ret["tensionReductionDeNumerator"] = tensionReductionDeNumerator
        ret["tensionShaftPitch"] = tensionShaftPitch
        ret["walkingAcceleration"] = walkingAcceleration
        ret["walkingDeacceleration"] = walkingDeacceleration
        ret["tensionPointSpeed"] = tensionPointSpeed
        ret["walkPointSpeed"] = walkPointSpeed
        ret["walk1States"] = walk1States
        ret["walk2States"] = walk2States
        ret["walk3States"] = walk3States
        ret["tensionState"] = tensionState
        ret["walkCurrentPosition"] = walkCurrentPosition
        ret["tensionForce"] = tensionForce
        ret["walkForce"] = walkForce
        ret["walkPointState"] = walkPointState
        ret["walkEnable"] = walkEnable
        ret["walkStatus"] = walkStatus
        logger.info(ret)
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
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
            "success": 0,
            "data": 0
        }
    return jsonify(ret_data)


@modbus.route('/reset', methods=['POST'])
def reset():
    ret_code = 0
    data = request.get_json()
    reset_int = data.get("reset")
    logger.info("reset_int = %d" % reset_int)
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=1)
        time.sleep(0.1)
        master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=0)
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


@modbus.route('/leftRightLaunch', methods=['POST'])
def leftRightLaunch():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("transversePointMove")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 16, output_value=action_int)
        c04 = master.execute(1, cst.READ_COILS, 3, 1)
        if c04 == 0:
            master.execute(1, cst.WRITE_SINGLE_COIL, 3, output_value=1)

    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


@modbus.route('/leftRightStop', methods=['POST'])
def leftRightStop():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("transversePointMove")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 17, output_value=action_int)

    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


@modbus.route('/leftRightOpen', methods=['POST'])
def leftRightOpen():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("transversePointMove")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 12, output_value=action_int)
        c04 = master.execute(1, cst.READ_COILS, 4, 1)
        if c04 == 0:
            master.execute(1, cst.WRITE_SINGLE_COIL, 4, output_value=1)

        c10 = master.execute(1, cst.READ_COILS, 9, 1)
        if c10 == 0:
            master.execute(1, cst.WRITE_SINGLE_COIL, 9, output_value=1)

    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


@modbus.route('/leftRightTense', methods=['POST'])
def leftRightTense():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("transversePointMove")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 13, output_value=action_int)
        c04 = master.execute(1, cst.READ_COILS, 3, 1)
        if c04 == 0:
            master.execute(1, cst.WRITE_SINGLE_COIL, 3, output_value=1)

        c10 = master.execute(1, cst.READ_COILS, 9, 1)
        if c10 == 0:
            master.execute(1, cst.WRITE_SINGLE_COIL, 9, output_value=1)

    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


# 行走零点定位
@modbus.route('/walkZeroLocation', methods=['POST'])
def walkZeroLocation():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("action")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 14, output_value=action_int)
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


# 行走模式
@modbus.route('/walkMode', methods=['POST'])
def walkMode():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("action")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 15, output_value=action_int)
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


# 轴4使能
@modbus.route('/enablePivot4', methods=['POST'])
def enablePivot4():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("action")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 3, output_value=1)
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


# 张紧点动张开
@modbus.route('/tensionPointOpen', methods=['POST'])
def tensionPointOpen():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("action")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 3, output_value=1)
        master.execute(1, cst.WRITE_SINGLE_COIL, 12, output_value=action_int)
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


# 张紧点动收缩
@modbus.route('/tensionPointClose', methods=['POST'])
def tensionPointClose():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("action")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 3, output_value=1)
        master.execute(1, cst.WRITE_SINGLE_COIL, 13, output_value=action_int)
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


# 张紧轴模式
@modbus.route('/tensionPivotMode', methods=['POST'])
def tensionPivotMode():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("action")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 9, output_value=action_int)
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


# 张紧启动
@modbus.route('/tensionLaunch', methods=['POST'])
def tensionLaunch():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("action")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 17, output_value=action_int)
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


# 张紧停止
@modbus.route('/tensionStop', methods=['POST'])
def tensionStop():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("action")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 18, output_value=action_int)
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


# 行走停止
@modbus.route('/walkStop', methods=['POST'])
def walkStop():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("action")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 6, output_value=action_int)
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)


# 行走启动
@modbus.route('/walkLaunch', methods=['POST'])
def walkLaunch():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("action")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 5, output_value=action_int)
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
    except socket.timeout as e1:
        ret_code = 1
    if ret_code == 0:
        ret_data = {
            "code": 0,
            "message": "success",
            "success": 1
        }
    else:
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0
        }
    return jsonify(ret_data)
