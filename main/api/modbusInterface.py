import modbus_tk
import modbus_tk.modbus_tcp as modbus_tcp
from flask import Blueprint
import modbus_tk.defines as cst
logger = modbus_tk.utils.create_logger("console")

modbus = Blueprint(("modbus", __name__))
modbus_address = "192.168.1.66"


@modbus.route('/test', methods=['POST'], strict_slashes=False)
def modbus_tcp_test():
    try:
        # 连接MODBUS TCP从机
        master = modbus_tcp.TcpMaster(host=modbus_address)
        master.set_timeout(5.0)
        logger.info("connected")
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
