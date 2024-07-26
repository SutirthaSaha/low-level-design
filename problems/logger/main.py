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

if __name__ == '__main__':
    logger_1 = Logger.get_instance()
    logger_2 = Logger.get_instance()
    logger_3 = Logger.get_instance()

    logger_1.log_deposit("0001", 50)
    logger_2.log_withdraw("0002", 100)
    logger_3.log_transfer("0001", "0002", 20)

    if logger_1 == logger_2:
        print("Yes")
