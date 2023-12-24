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
        if cache.get("page"):
            return method(url)
        cache.incr(key, 1)
        page = method(url)
        cache.setex("page", 10, page)
        return page
    return wrapper


@TrackUrl
def get_page(url: str) -> str:
    """ GET PAGE """
    try:
        request = requests.get(url)
        return request.text
    except Exception:
        return ""
