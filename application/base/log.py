import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler


def initLog(level):
    #配置日志模块
    level_dict ={'ERROR':logging.ERROR,'DEBUG':logging.DEBUG,'INFO':logging.INFO,'WARNING':logging.WARNING}
    level = level_dict.get(level) or logging.DEBUG

    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    # 建立一个TimedRotatingFileHandler来把日志记录在文件里，级别为debug以上
    path=time.strftime("%Y-%m-%d", time.localtime())+".log"
    handler = TimedRotatingFileHandler("./logs/"+path, when="D", interval=1, backupCount=15,
                                       encoding="UTF-8", delay=False, utc=True)
    # 配置日志格式
    formatter = logging.Formatter(
        "[%(levelname)s][%(thread)d][%(asctime)s][%(filename)s:%(lineno)d] %(funcName)s - %(message)s")
    handler.setFormatter(formatter)
    handler.setLevel(level)
    log.addHandler(handler)

    # 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
    cmd = logging.StreamHandler()
    cmd.setLevel(logging.INFO)
    cmd.setFormatter(formatter)
    log.addHandler(cmd)

    return log

