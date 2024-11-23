from enum import Enum


class ParkingSpotType(Enum):
    COMPACT = "Compact"
    MINI = "Mini"
    LARGE = "Large"
    DEFAULT = "Default"


class PaymentMode(Enum):
    CASH = "CASH"
    CARD = "CARD"
