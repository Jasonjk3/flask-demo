"""
配置定时器
"""
import atexit
import platform
from flask_apscheduler import APScheduler

from jobs.job import timed_task

# 解决 Flask-Apscheduler 多进程环境重复运行
# 通过全局锁，控制 scheduler 只运行一次
# 首次创建进程时，会创建一个 scheduler.lock 文件，并加上非阻塞互斥锁，此时 scheduler 可以成功开启，
# 如果文件加锁失败抛出异常，则表示当前 scheduler 已经开启了，最后再注册一个退出事件，
# 此时 flask 退出的话，就释放文件锁。
def initScheduler(app,log):
    """
        保证系统只启动一次定时任务
        :param app:
        :return:
        """
    scheduler = APScheduler()
    scheduler.add_job(id='time_task',func=timed_task, trigger='interval', seconds=60)

    if platform.system() != 'Windows':
        fcntl = __import__("fcntl")
        f = open('scheduler.lock', 'wb')
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            scheduler.init_app(app)
            scheduler.start()
        except Exception as e:
            log.error('Scheduler异常 - ',e)

        def unlock():
            fcntl.flock(f, fcntl.LOCK_UN)
            f.close()

        atexit.register(unlock)
    else:
        msvcrt = __import__('msvcrt')
        f = open('scheduler.lock', 'wb')
        try:
            msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
            scheduler.init_app(app)
            scheduler.start()
        except Exception as e:
            log.error('Scheduler异常 - ', e)

        def _unlock_file():
            try:
                f.seek(0)
                msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
            except:
                log.error('Scheduler 解锁异常 - ', e)

        atexit.register(_unlock_file)

