
from abc import abstractmethod
from datetime import datetime


class EvictionStrategies:
    def __init__(self):
        pass

    @abstractmethod
    def evict(self, storage):
        raise NotImplementedError("Not implemented !!!")


class LRU(EvictionStrategies):
    def __init__(self):
        super(LRU, self).__init__()

    def evict(self, storage):
        item = storage.popitem(0)
        print(f"Item {item} evicted as per LRU policy")


class AutoEvictionStrategy(EvictionStrategies):
    def evict(self, storage):
        while True:
            for key_val in storage:
                if storage.get(key_val) and storage.get(key_val)[1] \
                        and storage.get(key_val)[1] < datetime.now():
                    evicted = storage.pop(key_val)
                    print(f"Auto evicted {evicted} as ttl has expired")




