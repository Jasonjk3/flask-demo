from datetime import datetime



def timed_task():
    print('测试定时任务 -> ',datetime.now().strftime("%Y-%m-%d %H:%M:%S"))