# *-* coding:utf-8 *-*
#
#
#
#
"""
"""

import threading

import color
import generator
from base import Configer
from db import Mongo,Redis
from settings import MONGO_HOST,MONGO_PORT,MONGO_TIMEOUT,REDIS_HOST,REDIS_PORT,REDIS_AUTH,REDIS_DB,REDIS_CHARSET,REDIS_TIMEOUT

class Loader(object):

    def __init__(self):
        self._config = {}
        self._config_handler = None

        self._generator = None
        self._style = None

        self._mongo = None
        self._redis = None
        self._mongo_lock = None
        self._redis_lock = None

    def load_config(self,config_path):
        configer = Configer(config_path)
        self._config_handler = configer
        self._config = configer.config
    
    def load_generator(self):
        self._generator = generator.Generator()

    def load_color(self):
        self._style = color.color_style('light')

    def load_mongo(self):
        mongo_config = {'host':MONGO_HOST,'port':MONGO_PORT,'timeout':MONGO_TIMEOUT}
        self._mongo = Mongo(**mongo_config)
        self._mongo_lock = threading.Lock()      

    def load_redis(self):
        redis_config = {'host':REDIS_HOST,'port':REDIS_PORT,'password':REDIS_AUTH,'db':REDIS_DB,'charset':REDIS_CHARSET,'timeout':REDIS_TIMEOUT}
        self._redis = Redis(**redis_config)
        self._redis_lock = threading.Lock()      

    def settings(self,key):
        mod = import_module('settings')
        return getattr(mod,key)

    @property
    def config(self):
        return self._config

    @property
    def config_handler(self):
        return self._config_handler

    @property
    def generator(self):
        return self._generator
    
    @property
    def color(self):
        return self._style

    @property
    def mongo(self):
        return self._mongo

    @property
    def redis(self):
        return self._redis

    @property
    def mongo_lock(self):
        return self._mongo_lock

    @property
    def redis_lock(self):
        return self._redis_lock

loader = Loader()

def load_config():
    loader.load_config()

def load_generator():
    loader.load_generator()

def load_color():
    loader.load_color()

def load_mongo():
    loader.load_mongo()

def load_redis():
    loader.load_redis()


