from datetime import datetime, timedelta
import threading
import time

from Storage.cache import Cache
from Storage.EvictionStrategies.strategies import LRU, AutoEvictionStrategy
from Storage.cache import KeyValue


if __name__ == "__main__":
    cache = Cache(5, LRU())
    storage = cache.get_storage()
    key_value = KeyValue("A", 1, datetime.now() + timedelta(seconds=2))
    cache.set(key_value)
    aes = AutoEvictionStrategy()
    download_thread = threading.Thread(target=aes.evict, name="Downloader", args=([storage]))
    download_thread.start()
    print(cache)
    time.sleep(5) # We get auto eviction mesage here when ttl for A is expired
    print(cache)
    print(cache)





# abhishek.gaonkar@treebohotels.com

