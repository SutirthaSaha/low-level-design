from enum import Enum


class EvictionPolicyType(Enum):
    LRU = "LRU"
    FIFO = "FIFO"
