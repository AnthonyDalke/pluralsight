from logger_base import Logger

logger = Logger("my.log")
logger.write_log("Logging with base Singleton pattern.")

logger2 = Logger("***ignored***")
assert logger is logger2
print("Assertion passed.")

logger2.write_log("Another log record.")
logger.close_log()

with open("my.log", "r") as f:
    for line in f:
        print(line, end="")
