import ujson as json
from uuid import uuid1

import redis

from conf.curr_config import REDIS_QUEUE_CONF


class RedisQueue(object):
    """
    如果有大量待处理数据需要放入队列，可以用这个，小量数据用python自带queue即可。
    """
    def __init__(self, queue_name=None, logger=None):
        self.logger = logger
        self.queue_name = queue_name or str(uuid1())

    @property
    def conn(self):
        _conn = redis.Redis(
            host=REDIS_QUEUE_CONF.get("HOST"),
            port=REDIS_QUEUE_CONF.get("PORT"),
            db=REDIS_QUEUE_CONF.get("DB"),
            password=REDIS_QUEUE_CONF.get("PASSWORD")
        )
        return _conn

    def push(self, value):
        try:
            val = json.dumps(value)
            r = self.conn.lpush(self.queue_name, val)
            return r
        except:
            self.logger.exception('')
            return None

    def pop(self):
        try:
            value = self.conn.rpop(self.queue_name)
            if value:
                return json.loads(value)
        except:
            self.logger.exception('')
        return None

    def len(self):
        try:
            value = self.conn.llen(self.queue_name)
            return value
        except:
            self.logger.exception('')
            return 0
