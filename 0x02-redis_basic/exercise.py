#!/usr/bin/env python3
""" Exercise """

import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args)
    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = str(args)
        ukey = method(self, key)
        self._redis.rpush("{}:inputs".format(method.__qualname__), key)
        self._redis.rpush("{}:outputs".format(method.__qualname__), ukey)
        return ukey
    return wrapper


def replay(method: Callable) -> None:
    """ Reply """
    cache = redis.Redis()
    name = method.__qualname__
    print(f'{name} was called {cache.get(name).decode("utf-8")} times:')

    input_name = "{}:inputs".format(name)
    output_name = "{}:outputs".format(name)

    input_elements = cache.lrange(input_name, 0, -1)
    output_elements = cache.lrange(output_name, 0, -1)

    for i, o in zip(input_elements, output_elements):
        print(f'{name}(*{i.decode("utf-8")}) -> {o.decode("utf-8")}')


class Cache:
    """ Cache """
    def __init__(self):
        """ Init """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
