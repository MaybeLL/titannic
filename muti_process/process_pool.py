from multiprocessing import Process, Queue
import os, time, random
from threading import Lock
from threading import Condition

class Moniter(object):
    def __init__(self,buffer,queue):
        self.mutex = 1
        self.empty = buffer
        self.full = 0
        self.q = queue
        self.lock = Lock()

    # 写数据进程执行的代码:
    def write(self):
        print('Process to write: %s' % os.getpid())

        self.lock.acquire()
        print('Put %s to queue...' % os.getpid())
        self.q.put(os.getpid())
        self.lock.release()


    # 读数据进程执行的代码:
    def read(self):
        print('Process to read: %s' % os.getpid())
        while (True):
            value = self.q.get(True)
            print('Get %s from queue.' % value)





if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    moniter = Moniter(10,q)
    writer = Process(target=moniter.write)
    reader = Process(target=moniter.read)
    # 启动子进程pw，写入:
    writer.start()
    # 启动子进程pr，读取:
    reader.start()
    # 等待pw结束:
    writer.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    reader.terminate()

