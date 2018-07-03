import logging
from logging.handlers import TimedRotatingFileHandler, WatchedFileHandler, RotatingFileHandler
import os
import gzip
import time
import fcntl
import shutil


class Logger(object):
    """
    注意：python中的logger是线程安全的，但不是进程安全的，如果存在多个进程同时写一个logger，容易出现混乱。
    """
    def __init__(self, name, level=logging.INFO, roll_type=None, log_dir=None):
        self._logger = logging.getLogger(name)
        if not self._logger.handlers:
            log_dir = log_dir or './logs/'
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            file_path = log_dir+name+'.log'
            handler = self.__log_map(file_path, roll_type)
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(lineno)d - %(message)s'
            )
            handler.setFormatter(formatter)
            self._logger.addHandler(handler)
            self._logger.setLevel(level)

    def __log_map(self, file_path, roll_type=None):
        log_map = {
            "watched": WatchedFileHandler(file_path, encoding='utf-8'),
            "base_roll": RotatingFileHandler(file_path, encoding='utf-8', maxBytes=50000000, backupCount=15),
            "time_roll": TimedRotatingFileHandler(file_path, encoding='utf-8', when='midnight', backupCount=15)
        }
        if roll_type is None:
            roll_type = 'time_roll'
        handler = log_map[roll_type]
        if roll_type in ('base_roll', 'time_roll'):
            handler.rotator = self.__rotator
            # watchedfilehandler 依靠于外部程序做轮转
        return handler

    def __rotator(self, source, dest):
        dest_alias = dest+'.tmp'
        compress_lock = source+'_compressing_lock'
        lock_file = open(compress_lock, 'w')
        try:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX|fcntl.LOCK_NB)
            retry = 3
            while True and retry > 0:
                try:
                    shutil.copyfile(source, dest_alias)
                    open(source, 'w').close()
                    f_in = open(dest_alias, 'rb')
                    f_out = gzip.open("%s.gz" % dest, 'ab', compresslevel=9)
                    f_out.writelines(f_in)
                    f_out.close()
                    f_in.close()
                    os.remove(dest_alias)
                    lock_file.close()
                    os.remove(compress_lock)
                    break
                except:
                    retry -= 1
                    continue
        except:
            # 这里的异常主要是文件锁的异常
            while True:
                try:
                    fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                    break
                except:
                    time.sleep(1)
                    continue

    def __msg(self, func, *msg_list, sep=u'-'):
        assert callable(func) == True
        if self._logger is not None:
            try:
                m_list = []
                for m in msg_list:
                    m_list.append(str(m))
                func(sep.join(m_list))
            except Exception:
                self._logger.exception('logger')

    def info(self, *msg_list, sep=u'-'):
        func = self._logger.info
        self.__msg(func, *msg_list, sep=sep)

    def warn(self, *msg_list, sep=u'-'):
        func = self._logger.warning
        self.__msg(func, *msg_list, sep=sep)

    def error(self, *msg_list, sep=u'-'):
        func = self._logger.error
        self.__msg(func, *msg_list, sep=sep)

    def debug(self, *msg_list, sep=u'-'):
        func = self._logger.debug
        self.__msg(func, *msg_list, sep=sep)

    def exception(self, *msg_list, sep=u'-'):
        func = self._logger.exception
        self.__msg(func, *msg_list, sep=sep)

    def message(self, msg):
        pass
