import logging 
from logging.handlers import TimedRotatingFileHandler


def get_logger():
    log_file_handler = TimedRotatingFileHandler(filename="./watermark_detect.log", when="D", interval=2, backupCount=2)
    log_fmt = '%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s'
    formatter = logging.Formatter(log_fmt)
    log_file_handler.setFormatter(formatter)
    log_file_handler.suffix = "%Y-%m-%d"
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger()
    log.addHandler(log_file_handler)
    return log
