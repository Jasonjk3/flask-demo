import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler


def initLog():
    #配置日志模块
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    # 建立一个TimedRotatingFileHandler来把日志记录在文件里，级别为debug以上
    path=time.strftime("%Y-%m-%d", time.localtime())+".log"
    handler = TimedRotatingFileHandler("./logs/"+path, when="D", interval=1, backupCount=15,
                                       encoding="UTF-8", delay=False, utc=True)
    # 配置日志格式
    formatter = logging.Formatter(
        "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    log.addHandler(handler)

    # 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
    cmd = logging.StreamHandler()
    cmd.setLevel(logging.INFO)
    log.addHandler(cmd)

    return log

