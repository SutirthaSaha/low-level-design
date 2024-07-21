from abc import ABC, abstractmethod

from util import DoublyLinkedList, ListNode
from enums import EvictionPolicyType


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


class Storage:
    def __init__(self, capacity):
        self.storage = dict()
        self.capacity = capacity

    def get(self, key) -> str:
        if key not in self.storage:
            raise Exception("Key doesn't exist")
        return self.storage[key]

    def add(self, key, value) -> bool:
        self.storage[key] = value

    def remove(self, key) -> bool:
        self.storage.pop(key)

    def is_storage_full(self) -> bool:
        if len(self.storage.keys()) == self.capacity:
            return True
        return False


class Cache:
    def __init__(self, capacity, eviction_policy: str):
        self.capacity = capacity
        self.storage = Storage(capacity)
        self.eviction_policy = EvictionPolicyFactory.get_eviction_policy(eviction_policy)

    def get(self, key) -> str:
        value = self.storage.get(key)
        self.eviction_policy.access_key(key)
        return value

    def put(self, key, value) -> bool:
        if self.storage.is_storage_full():
            self.storage.remove(self.eviction_policy.evict_key())
        self.storage.add(key, value)
        self.eviction_policy.access_key(key)


class EvictionPolicyFactory:

    @classmethod
    def get_eviction_policy(cls, eviction_policy_type: str):
        if eviction_policy_type == EvictionPolicyType.LRU:
            return LeastRecentlyUsed()
        elif eviction_policy_type == EvictionPolicyType.FIFO:
            return FirstInFirstOut()
