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


def int_to_float(f):
    b32_l = utils.encode_ieee(f)
    b16_l = utils.long_list_to_word([b32_l])
    return b16_l


# 连接MODBUS TCP从机
master = modbus_tcp.TcpMaster(host=modbus_address, port=502)
logger.info("modbus connected")
try:
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 47, output_value=WriteFloat(1.00))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 49, output_value=WriteFloat(1.00))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 51, output_value=WriteFloat(1.00))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 43, output_value=WriteFloat(1.00))
    master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 23, output_value=WriteFloat(300.00))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 25, output_value=WriteFloat(8.00))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 27, output_value=WriteFloat(0.00))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 1, output_value=WriteFloat(1.00))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 3, output_value=WriteFloat(10.00))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 5, output_value=WriteFloat(20.00))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 7, output_value=WriteFloat(1.00))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 9, output_value=WriteFloat(2.00))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 11, output_value=WriteFloat(1.00))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 13, output_value=WriteFloat(0.0001))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 15, output_value=WriteFloat(0.000100))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 42, output_value=WriteFloat(0.01))
    # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 44, output_value=WriteFloat(0.000100))
except modbus_tk.modbus.ModbusError as e:
    logger.error("%s- Code=%d" % (e, e.get_exception_code()))
except socket.timeout as e1:
    ret_code = 1


@modbus.route('/test', methods=['POST'], strict_slashes=False)
def modbus_tcp_test():
    try:
        # 读保持寄存器
        demo1 = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 9)
        print(demo1)
        # 读输入寄存器
        logger.info(master.execute(3, cst.READ_INPUT_REGISTERS, 0, 9, output_value=1))
        # 读线圈寄存器
        logger.info(master.execute(2, cst.READ_COILS, 0, 8))
        logger.info(master.execute(2, cst.WRITE_SINGLE_COIL, 1, output_value=2))
        # 读离散输入寄存器
        logger.info(master.execute(4, cst.READ_DISCRETE_INPUTS, 0, 8))
        # 单个读写寄存器操作
        # 写寄存器地址为0的保持寄存器
        logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 0, output_value=20))
        logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 8))
        # 写寄存器地址为0的线圈寄存器，写入内容为0（位操作）
        logger.info(master.execute(2, cst.WRITE_SINGLE_COIL, 0, output_value=2))
        logger.info(master.execute(2, cst.READ_COILS, 0, 1))
        # # 多个寄存器读写操作
        # # 写寄存器起始地址为0的保持寄存器，操作寄存器个数为4
        logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[20, 21, 22, 23]))
        logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 4))
        # # 写寄存器起始地址为0的线圈寄存器
        logger.info(master.execute(2, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 1]))
        logger.info(master.execute(2, cst.READ_COILS, 0, 4))
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))


@modbus.route('/frontPointMoveAction', methods=['POST'])
def front_point_move_action():
    data = request.get_json()
    # 1 启动 0 停止
    action = data.get(move_action_key)
    ret_code = 0
    try:
        # c01 = master.execute(1, cst.READ_COILS, 1, 1)
        # if c01 == 0:
        master.execute(1, cst.WRITE_SINGLE_COIL, 1, output_value=1)
        time.sleep(1)
        # c16 = master.execute(1, cst.READ_COILS, 16, 1)
        # if c16 == 1:
        master.execute(1, cst.WRITE_SINGLE_COIL, 16, output_value=1)
        time.sleep(1)
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 37, output_value=WriteFloat(500.00))
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 41, output_value=WriteFloat(20.00))
        master.execute(1, cst.WRITE_SINGLE_COIL, 6, output_value=1)
        time.sleep(1)
        logger.info(ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 37, 2)))
        time.sleep(1)
        logger.info(ReadFloat(master.execute(1, cst.READ_HOLDING_REGISTERS, 41, 2)))
        time.sleep(1)
        logger.info(master.execute(1, cst.READ_COILS, 16, 1))
        time.sleep(1)
        logger.info(master.execute(1, cst.READ_COILS, 1, 1))
        master.execute(1, cst.WRITE_SINGLE_COIL, 6, output_value=1)
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


@modbus.route('/backPointMoveAction', methods=['POST'])
def back_point_move_action():
    data = request.get_json()
    # 1 启动 0 停止
    action = data.get(move_action_key)
    logger.info("action = %d" % action)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 12, output_value=action)
        c01 = master.execute(1, cst.READ_COILS, 1, 1)
        if c01 == 0:
            master.execute(1, cst.WRITE_SINGLE_COIL, 1, output_value=1)

        c16 = master.execute(1, cst.READ_COILS, 16, 1)
        if c16 == 1:
            master.execute(1, cst.WRITE_SINGLE_COIL, 16, 0)
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
        master.execute(1, cst.WRITE_SINGLE_COIL, 1, output_value=1)
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


@modbus.route('/frontbackPointStopAction', methods=['POST'])
def front_back_point_stop_action():
    data = request.get_json()
    # 1 启动 0 停止
    action = data.get(move_action_key)
    logger.info("action = %d" % action)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=action)

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
    logger.info("finallyTension = %s" % finallyTension)
    finallyTensionTime = data.get("finallyTensionTime")
    walkLength = data.get("walkLength")
    walkSpeed = data.get("walkSpeed")
    zeroLocation = data.get("zeroLocation")
    tensionFactor = data.get("tensionFactor")
    tensionOffset = data.get("tensionOffset")
    pullFactor = data.get("pullFactor")
    pullOffset = data.get("pullOffset")
    Kp = data.get("Kp")
    Tn = data.get("Tn")
    Tv = data.get("Tv")
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
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 37, output_value=finallyTension)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 41, output_value=finallyTensionTime)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 19, output_value=walkLength)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 21, output_value=walkSpeed)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 31, output_value=zeroLocation)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 47, output_value=tensionFactor)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 49, output_value=tensionOffset)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 51, output_value=pullFactor)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 43, output_value=pullOffset)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 23, output_value=Kp)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 25, output_value=Tn)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 27, output_value=Tv)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 1, output_value=walkDeceleratorNumerator)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 3, output_value=walkDeceleratorDenominator)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 5, output_value=travelingAxleLength)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 7, output_value=tensionReductionNumerator)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 9, output_value=tensionReductionDeNumerator)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 11, output_value=tensionShaftPitch)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 13, output_value=walkingAcceleration)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 15, output_value=walkingDeacceleration)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 42, output_value=tensionPointSpeed)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 44, output_value=walkPointSpeed)

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
        finallyTension = master.execute(1, cst.READ_HOLDING_REGISTERS, 37, 1)
        finallyTensionTime = master.execute(1, cst.READ_HOLDING_REGISTERS, 41, 1)
        walkLength = master.execute(1, cst.READ_HOLDING_REGISTERS, 19, 1)
        walkSpeed = master.execute(1, cst.READ_HOLDING_REGISTERS, 21, 1)
        zeroLocation = master.execute(1, cst.READ_HOLDING_REGISTERS, 31, 1)
        tensionFactor = master.execute(1, cst.READ_HOLDING_REGISTERS, 47, 1)
        tensionOffset = master.execute(1, cst.READ_HOLDING_REGISTERS, 49, 1)
        pullFactor = master.execute(1, cst.READ_HOLDING_REGISTERS, 51, 1)
        pullOffset = master.execute(1, cst.READ_HOLDING_REGISTERS, 43, 1)
        Kp = master.execute(1, cst.READ_HOLDING_REGISTERS, 23, 1)
        Tn = master.execute(1, cst.READ_HOLDING_REGISTERS, 25, 1)
        Tv = master.execute(1, cst.READ_HOLDING_REGISTERS, 27, 1)
        walkDeceleratorNumerator = master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 1)
        walkDeceleratorDenominator = master.execute(1, cst.READ_HOLDING_REGISTERS, 3, 1)
        travelingAxleLength = master.execute(1, cst.READ_HOLDING_REGISTERS, 5, 1)
        tensionReductionNumerator = master.execute(1, cst.READ_HOLDING_REGISTERS, 7, 1)
        tensionReductionDeNumerator = master.execute(1, cst.READ_HOLDING_REGISTERS, 9, 1)
        tensionShaftPitch = master.execute(1, cst.READ_HOLDING_REGISTERS, 11, 1)
        walkingAcceleration = master.execute(1, cst.READ_HOLDING_REGISTERS, 13, 1)
        walkingDeacceleration = master.execute(1, cst.READ_HOLDING_REGISTERS, 15, 1)
        tensionPointSpeed = master.execute(1, cst.READ_HOLDING_REGISTERS, 42, 1)
        walkPointSpeed = master.execute(1, cst.READ_HOLDING_REGISTERS, 44, 1)
        walk1States = master.execute(1, cst.READ_INPUT_REGISTERS, 1, 1)
        walk2States = master.execute(1, cst.READ_INPUT_REGISTERS, 2, 1)
        walk3States = master.execute(1, cst.READ_INPUT_REGISTERS, 3, 1)
        tensionState = master.execute(1, cst.READ_INPUT_REGISTERS, 4, 1)
        walkCurrentPosition = master.execute(1, cst.READ_INPUT_REGISTERS, 5, 1)
        tensionForce = master.execute(1, cst.READ_INPUT_REGISTERS, 12, 1)
        walkForce = master.execute(1, cst.READ_INPUT_REGISTERS, 14, 1)
        walkPointState = master.execute(1, cst.READ_INPUT_REGISTERS, 18, 1)
        walkEnable = master.execute(1, cst.READ_COILS, 1, 1)
        walkStatus = master.execute(1, cst.READ_COILS, 16, 1)
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
        ret["walk1States"] = 1
        ret["walk2States"] = 2
        ret["walk3States"] = 3
        ret["tensionState"] = 4
        ret["walkCurrentPosition"] = 5
        ret_data = {
            "code": ret_code,
            "message": "fail",
            "success": 0,
            "data": ret
        }
    return jsonify(ret_data)


@modbus.route('/reset', methods=['POST'])
def reset():
    data = request.get_json()
    reset_int = data.get("reset")
    logger.info("reset_int = %d" % reset_int)
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 8, output_value=reset_int)
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
        master.execute(1, cst.WRITE_SINGLE_COIL, 17, output_value=action_int)
        c04 = master.execute(1, cst.READ_COILS, 4, 1)
        if c04 == 0:
            master.execute(1, cst.WRITE_SINGLE_COIL, 4, output_value=1)

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


@modbus.route('/leftRightOpen', methods=['POST'])
def leftRightOpen():
    data = request.get_json()
    # 1 启动 0 停止
    action_int = data.get("transversePointMove")
    logger.info("action_int = %d" % action_int)
    ret_code = 0
    try:
        master.execute(1, cst.WRITE_SINGLE_COIL, 13, output_value=action_int)
        c04 = master.execute(1, cst.READ_COILS, 4, 1)
        if c04 == 0:
            master.execute(1, cst.WRITE_SINGLE_COIL, 4, output_value=1)

        c10 = master.execute(1, cst.READ_COILS, 10, 1)
        if c10 == 0:
            master.execute(1, cst.WRITE_SINGLE_COIL, 10, output_value=1)

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
        master.execute(1, cst.WRITE_SINGLE_COIL, 14, output_value=action_int)
        c04 = master.execute(1, cst.READ_COILS, 4, 1)
        if c04 == 0:
            master.execute(1, cst.WRITE_SINGLE_COIL, 4, output_value=1)

        c10 = master.execute(1, cst.READ_COILS, 10, 1)
        if c10 == 0:
            master.execute(1, cst.WRITE_SINGLE_COIL, 10, output_value=1)

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
