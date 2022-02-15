import datetime as datetime
from collections import OrderedDict

import threading
import threading, time


class KeyValue:
    def __init__(self, key, value, expiry=None):
        self.key = key
        self.value = value
        self.expiry = expiry


class Cache:
    def __init__(self, size, eviction_strategy):
        self.__max_size = size
        self.__storage = OrderedDict()

        self.__eviction_strategy = eviction_strategy
        self.__auto_eviction_thread = None

    def auto_eviction(self):
        def auto_evict(your_self):
            print(your_self.__storage)
            time.sleep(10)

        return threading.Thread(target=auto_evict, args=([self]))

    def __evict_cache(self):
        self.__eviction_strategy.evict(self.__storage)

    def __size_of_cache(self):
        return len(self.__storage)

    def __str__(self):
        print(self.__storage)
        return ""

    def set(self, key_value: KeyValue):
        if self.__size_of_cache() == self.__max_size:
            self.__evict_cache()

        self.__storage[key_value.key] = (key_value.value, key_value.expiry)

    def get(self, key):
        if key in self.__storage:
            cache_value = self.__storage.get(key)
            self.__storage.move_to_end(key)

            return cache_value[0]

        return None

    def delete(self, key):
        if key in self.__storage:
            self.__storage.pop(key)
            return 1

        return 0

    def get_storage(self):
        return self.__storage

