#!/usr/bin/env python3
""" Exercise """

import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """ Cache """
    def __init__(self):
        """ Init """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key, fn: Optional[Callable] = None):
        """ get """
        if not fn:
            return self._redis.get(key)
        return fn(self._redis.get(key))

    def get_str(self, key):
        """ get str """
        return self._redis.get(key).decode('utf-8')

    def get_int(self, key):
        """ get int """
        try:
            return int(self._redis.get(key).decode('utf-8'))
        except Exception:
            return 0
