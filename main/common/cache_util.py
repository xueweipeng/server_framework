import redis
from conf.curr_config import REDIS_CACHE_CONF
import json
import decimal
from abc import ABCMeta, abstractmethod


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


class Cache(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set(self, *args, **kwargs):
        pass

    @abstractmethod
    def get(self, *args, **kwargs):
        pass


class AutoExpireCache(Cache):
    """设置过期时间为明天的缓存"""
    def __init__(self):
        super(AutoExpireCache, self).__init__()
        self.conn = redis.Redis(host=REDIS_CACHE_CONF.get("HOST"),
                                port=REDIS_CACHE_CONF.get("PORT"),
                                db=REDIS_CACHE_CONF.get("DB"),
                                password=REDIS_CACHE_CONF.get("PASSWORD")
                                )
        self.secret = "kk_tmp_"

    def set(self, key, value, expire_time=60):
        self.conn.setex(self.secret+str(key), value, expire_time)
        return True

    def get(self, key):
        result = self.conn.get(self.secret+str(key))
        if result:
            return result.decode('utf-8')
        else:
            return None

    def clear(self, key):
        return self.conn.delete(self.secret+str(key))

