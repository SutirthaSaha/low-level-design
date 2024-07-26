from enum import Enum


class TransactionStatus(Enum):
    SUCCESSFUL = "Successful"
    IN_PROGRESS = "In Progress"
    FAILED = "FAILED"


class CurrencyType(Enum):
    INR = "Indian Rupee"
    USD = "US Dollar"
    EUR = " Euro"


class PaymentMethod(Enum):
    CARD = "Card"
    CASH = "Cash"
    UPI = "UPI"
