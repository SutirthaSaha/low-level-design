class Logger:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def __init__(self):
        if Logger._instance is not None:
            raise Exception("Instance already exists")
        else:
            Logger._instance = self

    def log_withdraw(self, account: str, amount: float):
        print(f"Withdraw {account}: {amount}")

    def log_deposit(self, account: str, amount: float):
        print(f"Deposit {account}: {amount}")

    def log_transfer(self, sender_account: str, receiver_account: str, amount: float):
        print(f"Transfer from {sender_account} to {receiver_account}: {amount}")
