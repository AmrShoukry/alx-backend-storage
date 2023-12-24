#!/usr/bin/env python3
""" WEB """

import requests
from functools import wraps
from typing import Callable
import redis


def TrackUrl(method: Callable) -> Callable:
    """ TrackURL """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """ Wrapper """
        cache = redis.Redis()
        url = args[0]
        key = f'count:{url}'
        cache.incr(key, 1)
        cache.expire(key, 10)
        return method(url)
    return wrapper


@TrackUrl
def get_page(url: str) -> str:
    """ GET PAGE """
    cache = redis.Redis()
    try:
        requests.get(url)
        key = f'count:{url}'
        return (cache.get(key))
    except Exception:
        return "0".encode('utf-8')
