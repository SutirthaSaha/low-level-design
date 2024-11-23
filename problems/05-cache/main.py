from model import Cache
from enums import EvictionPolicyType

cache = Cache(3, EvictionPolicyType.LRU)
cache.put("1", "1")
cache.put("2", "2")
cache.get("1")
cache.put("3", "3")
cache.put("4", "4")

cache.get("1")
cache.get("2")