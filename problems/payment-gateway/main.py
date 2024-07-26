from random import randint
from enums import CurrencyType, TransactionStatus, PaymentMethod
from abc import ABC, abstractmethod


class Amount:
    def __init__(self, value: float, currency: CurrencyType):
        self.value = value
        self.currency = currency


class Transaction:
    def __init__(self, amount: Amount, sender_account: 'Account', receiver_account: 'Account',
                 payment_method: PaymentMethod):
        self.id = randint(1, 10)
        self.amount = amount
        self.status = TransactionStatus.IN_PROGRESS
        self.sender_account = sender_account
        self.receiver_account = receiver_account
        self.payment_method = payment_method
        self.observers = [SuccessfulTransactionStatusObserver(),
                          FailedTransactionStatusObserver(),
                          InProgressTransactionStatusObserver()]

    def set_status(self, status: TransactionStatus):
        self.status = status
        for observer in self.observers:
            if self.status == observer.status:
                observer.notify(self.sender_account, self.receiver_account)


class User:
    def __init__(self, name):
        self.id = randint(1, 10)
        self.name = name

    def create(self, transaction):
        pass


class TransactionValidationStrategy(ABC):
    @abstractmethod
    def validate(self, transaction: Transaction):
        pass


class CashStrategy(TransactionValidationStrategy):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def __init__(self):
        if CashStrategy._instance is not None:
            raise Exception("Instance already exists")
        CashStrategy._instance = self

    def validate(self, transaction: Transaction):
        return True


class OnlineStrategy(TransactionValidationStrategy):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def __init__(self):
        if OnlineStrategy._instance is not None:
            raise Exception("Instance already exists")
        OnlineStrategy._instance = self

    def validate(self, transaction: Transaction):
        return True


class RuleEngine:

    @staticmethod
    def validate(self, transaction: Transaction):
        if transaction.payment_method == PaymentMethod.CASH:
            return CashStrategy.get_instance().validate(transaction)
        else:
            return OnlineStrategy.get_instance().validate(transaction)

    @staticmethod
    def is_fraudulent(self, transaction: Transaction):
        return False


class Bank:
    def __init__(self, name):
        self.name = name


class Account:
    def __init__(self, user: User, bank: Bank):
        self.id = randint(1, 10)
        self.user = user
        self.bank = bank


class TransactionStatusObserver(ABC):

    @abstractmethod
    def notify(self, sender_account: Account, receiver_account: Account):
        pass


class SuccessfulTransactionStatusObserver(TransactionStatusObserver):
    def __init__(self):
        self.status = TransactionStatus.SUCCESSFUL

    def notify(self, sender_account: Account, receiver_account: Account):
        print(f"Transaction from {sender_account.user.name} to {receiver_account.user.name} was successful")


class FailedTransactionStatusObserver(TransactionStatusObserver):
    def __init__(self):
        self.status = TransactionStatus.FAILED

    def notify(self, sender_account: Account, receiver_account: Account):
        print(f"Transaction from {sender_account.user.name} to {receiver_account.user.name} failed")


class InProgressTransactionStatusObserver(TransactionStatusObserver):
    def __init__(self):
        self.status = TransactionStatus.IN_PROGRESS

    def notify(self, sender_account: Account, receiver_account: Account):
        print(f"Transaction from {sender_account.user.name} to {receiver_account.user.name} is in-progress")
