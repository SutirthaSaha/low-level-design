from model import CacheFactory
from enums import CacheType

cache = CacheFactory(3).get_cache(CacheType.FIFO)
cache.add("1", "1")
cache.add("2", "2")
cache.get("1")
cache.add("3", "3")
cache.add("4", "4")

cache.get("1")
cache.get("2")