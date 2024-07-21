from logger.model import Logger

logger_1 = Logger.get_instance()
logger_2 = Logger.get_instance()
logger_3 = Logger.get_instance()

logger_1.log_deposit("0001", 50)
logger_2.log_withdraw("0002", 100)
logger_3.log_transfer("0001", "0002", 20)

if logger_1 == logger_2:
    print("Yes")
