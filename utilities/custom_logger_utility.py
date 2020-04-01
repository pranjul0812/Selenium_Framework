import logging
import inspect


def custom_logger(loglevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler("automation.log", mode='a')
    # use mode as 'a' for appending the logs(specially use in frameworks)
    handler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger