from abc import ABC, abstractmethod

from util import DoublyLinkedList, ListNode
from enums import CacheType


class EvictionPolicy(ABC):
    def __init__(self):
        self.list = DoublyLinkedList()
        self.mapper = dict()

    @abstractmethod
    def access_key(self, key):
        pass

    @abstractmethod
    def evict_key(self):
        pass


class LeastRecentlyUsed(EvictionPolicy):

    def access_key(self, key):
        if key in self.mapper:
            node = self.mapper[key]
            self.list.detach(node)
        else:
            node = ListNode(key)
            self.mapper[key] = node
        self.list.attach(node)

    def evict_key(self):
        node = self.list.head
        self.list.detach(node)
        self.mapper.pop(node.val)
        return node.val


class FirstInFirstOut(EvictionPolicy):

    def access_key(self, key):
        if key not in self.mapper:
            node = ListNode(key)
            self.mapper[key] = node
            self.list.attach(node)

    def evict_key(self):
        node = self.list.head
        self.list.detach(node)
        self.mapper.pop(node.val)
        return node.val


class Cache:
    def __init__(self, capacity, eviction_policy: EvictionPolicy):
        self.storage = dict()
        self.capacity = capacity
        self.eviction_policy = eviction_policy

    def get(self, key) -> str:
        if key not in self.storage:
            raise Exception("Key doesn't exist")
        self.eviction_policy.access_key(key)
        return self.storage[key]

    def add(self, key, value) -> bool:
        if self.is_storage_full():
            self.remove()
        self.storage[key] = value
        self.eviction_policy.access_key(key)

    def remove(self) -> bool:
        key = self.eviction_policy.evict_key()
        self.storage.pop(key)

    def is_storage_full(self) -> bool:
        if len(self.storage.keys()) == self.capacity:
            return True
        return False


class CacheFactory:

    def __init__(self, capacity: int = 5):
        self.capacity = capacity

    def get_cache(self, cache_type: str):
        if cache_type == CacheType.LRU:
            return Cache(self.capacity, LeastRecentlyUsed())
        elif cache_type == CacheType.FIFO:
            return Cache(self.capacity, FirstInFirstOut())
