#!/usr/bin/env python3
""" Module for Redis db """

import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from sys import byteorder
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ This function counts number of calls to a class method """
    # use qualname dunder for qualified class method name
    key = method.__qualname__
    # use functools.wraps to create wrapper method for incrementing

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ The wrapper for method """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """The Class that defines methods that operate a caching system """

    def __init__(self):
        """ Initializes an Instance of Redis db """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """This function creates keys and stores it with the data. """
        # uuid must type-casted to str for Redis to be able to accept it
        key = str(uuid4())
        # using pipelining for multi sets, mset() isn't approrpiate for a cache
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """ This function returns data converted to desired format """
        # default Redis.get in case key does not exist
        data = self._redis.get(key)
        # use callable if one provided
        if fn:
            data = fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """ This function converts bytes to str """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ This function converts bytes to int """
        return int.from_bytes(data, byteorder)
