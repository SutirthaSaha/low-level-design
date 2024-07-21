from abc import ABC, abstractmethod

from util import DoublyLinkedList
from enums import CacheType
from collections import deque


class Cache(ABC):
    def __init__(self, capacity):
        self.storage = dict()
        self.capacity = capacity

    @abstractmethod
    def get(self, key) -> str:
        pass

    @abstractmethod
    def add(self, key, value) -> bool:
        pass

    @abstractmethod
    def remove(self) -> bool:
        pass

    def is_storage_full(self) -> bool:
        if len(self.storage.keys()) == self.capacity:
            return True
        return False


class LRUCache(Cache):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.frequency = DoublyLinkedList()

    def get(self, key) -> str:
        if key not in self.storage:
            raise Exception("Key doesn't exist")
        node = self.frequency.remove_val(key)
        self.frequency.add_node(node)
        return self.storage[key]

    def add(self, key, value) -> bool:
        if self.is_storage_full():
            self.remove()
        self.storage[key] = value
        self.frequency.add(key)

    def remove(self) -> bool:
        key = self.frequency.remove_first().val
        self.storage.pop(key)
        return True


class FIFOCache(Cache):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.order = deque()

    def get(self, key) -> str:
        return self.storage[key]

    def add(self, key, value) -> bool:
        if self.is_storage_full():
            self.remove()
        self.order.append(key)
        self.storage[key] = value

    def remove(self) -> bool:
        key = self.order.popleft()
        self.storage.pop(key)


class CacheFactory:

    def __init__(self, capacity: int = 5):
        self.capacity = capacity

    def get_cache(self, cache_type: str):
        if cache_type == CacheType.LRU:
            return LRUCache(self.capacity)
        elif cache_type == CacheType.FIFO:
            return FIFOCache(self.capacity)
