from abc import ABCMeta
import signal
import os
from threading import Thread
import asyncio
from concurrent.futures import ThreadPoolExecutor
from traceback import format_exc
import requests
import ujson as json


class CanDaemon(metaclass=ABCMeta):

    def __init__(self, logger):
        """
        针对调度类组件提供一些基本方法，其中涵盖了接受信号，心跳监控， 产生事件循环，线程池等。每个wrapper， dispatcher都有可能
        成为一个daemon进程。
        注意：要继承这个类，类必须存在于主线程，因为这个类有信号机制
        """
        self.log = logger
        self.exit = False
        signal.signal(signal.SIGTERM, self.exit_msg)

    def exit_msg(self, signum, frame):
        if signum == 15:
            self.log.info("accept exit command...")
            self.log.info("waiting data handling finishing..")
            self.exit = True
        else:
            self.log.error('unknown cnd and signal num:{0}'.format(str(signum)))

    def judge_exit(self):
        if self.exit:
            self.log.warn('{0} exit..'.format(self.__class__.__name__))
            os._exit(0)

    def heartbeat(self, *args, **kwargs):
        """主要用于心跳的监控。"""
        pass

    def event_loop(self):
        self.log.info("start a event loop thread for class: {0}".format(self.__class__.__name__))
        loop = asyncio.new_event_loop()

        def start_loop(inner_loop):
            asyncio.set_event_loop(inner_loop)
            inner_loop.run_forever()
        t = Thread(target=start_loop, args=(loop, ))
        t.setDaemon(True)
        t.start()
        return loop

    @staticmethod
    def run_coroutine(ins_obj, loop):
        asyncio.run_coroutine_threadsafe(ins_obj, loop)

    def thread_pool(self, max_num=3):
        self.log.info("start a thread pool for class:{0}, size:{1}".format(self.__class__.__name__, max_num))
        pool = ThreadPoolExecutor(max_workers=max_num)
        return pool


class CanNotify(object):
    def __init__(self, logger):
        self.log = logger

    def send_msg(self, msg, *phone):
        for i in phone:
            try:
                data = {
                    "channel_group": "4a727188-e3c6-4e8b-b513-4a375a1d6d15",
                    "content": msg,
                    "mobile": i
                }
                msg_url = 'http://localhost:8007/send_sms'
                res = requests.post(url=msg_url,
                                    data=json.dumps(data),
                                    headers={'Content-Type': 'application/json'},
                                    timeout=10)
                self.log.info('send msg to {0}, result:{1}'.format(i, res.json()))
            except:
                self.log.error(format_exc())
