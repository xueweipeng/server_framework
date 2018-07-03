import time

from blue.common.logger import Logger
from blue.common.mixin import CanDaemon, CanNotify
from blue.common.mysql_util import Cursor
from conf.curr_config import GOV_PROD_MYSQL_INFO


class TouchMonitor(CanDaemon, CanNotify):
    """
    表结构： monitor_service
    服务自己去更新db的时间戳，来表示自己在线。
    """
    def __init__(self):
        self.log = Logger(self.__class__.__name__)
        CanDaemon.__init__(self, self.log)
        CanNotify.__init__(self, self.log)

    @staticmethod
    def touch_db(service):
        sql = "update monitor_service set utime=now() where service='{0}'".format(service)
        Cursor(GOV_PROD_MYSQL_INFO).execute(sql, ())

    def send_warning(self, msg, *phone):
        self.send_msg(msg, *phone)

    def scan(self):
        self.log.info("begin scanning ...")
        sql = '''select * from monitor_service where status=True 
        and UNIX_TIMESTAMP(now()) - UNIX_TIMESTAMP(utime) > warning_interval;'''
        result = Cursor(GOV_PROD_MYSQL_INFO).fetch_all(sql, ())
        if result:
            for item in result:
                service = item.get('service')
                utime = str(item.get('utime'))
                warning_list = item.get('warning_list').split(',')
                warning_interval = item.get('warning_interval')
                for phone in warning_list:
                    msg = 'touch db warning:{0},last utime:{1},warning interval:{2}'.\
                        format(service, utime, warning_interval)
                    self.log.info("send warning to {0}".format(phone))
                    self.send_warning(msg, phone)
        self.log.info('end scanning ...')

    def daemon(self):
        while True:
            try:
                self.scan()
                self.log.info('sleeping ....')
                time.sleep(60)
            except:
                self.log.exception()
