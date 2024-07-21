from enum import Enum


class CacheType(Enum):
    LRU = "LRU"
    FIFO = "FIFO"
