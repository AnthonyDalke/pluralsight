from logger_mono import Logger

logger = Logger("my.log")
logger.write_log("Logging with monostate Singleton pattern.")
logger2 = Logger("***ignored***")
logger2.write_log("Another log record.")

logger.close_log()

with open("my.log", "r") as f:
    for line in f:
        print(line, end="")
