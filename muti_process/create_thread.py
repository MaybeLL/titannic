import time,threading
import os
#线程代码





class producer(threading.Thread):
    def __init__(self,name):
        # super(TaskThread,self) 首先找到 TaskThread 的父类（就是类 threading.Thread），然后把类 TaskThread 的对象转换为类 threading.Thread 的对象
        super(producer,self).__init__(name=name)

    def run(self):
        global emptycon,fullcon,productnum
        print('producer %s is running...' % self.getName())
        while(True):
            if emptycon.acquire():
                if productnum<10:
                    print("PUT {} {}".format("product",os.getpid()))
                    product.append("product"+str(os.getpid()))
                    productnum = productnum +1

                    fullcon.notify()
                else:
                    print("producer {} is waitting ".format(self.getName()))
                    emptycon.wait()
                emptycon.release()
                time.sleep(2)

class customer(threading.Thread):
    def __init__(self,name):
        # super(TaskThread,self) 首先找到 TaskThread 的父类（就是类 threading.Thread），然后把类 TaskThread 的对象转换为类 threading.Thread 的对象
        super(customer,self).__init__(name=name)

    def run(self):
        global fullcon,productnum,emptycon
        print('customer %s is running...' % self.getName())
        while True:
            if fullcon.acquire():
                if productnum>0:
                    productnum = productnum-1
                    emptycon.notify()
                else:
                    print("customer {} is waitting".format(self.getName()))
                    fullcon.wait()
                fullcon.release()
                time.sleep(1)


if __name__=="__main__":

    emptycon = threading.Condition()
    fullcon = threading.Condition()
    productnum = 0
    product =[]

    for j in range(5):
        p = producer(str(j))
        p.start()

    for i in range(4):
        c = customer(str(i))
        c.start()