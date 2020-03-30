from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
    print("child process name : {}".format(name))
    print("child process id : {}".format(os.getpid()))
    print("parent process id : {}".format(os.getppid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    # 创建子进程
    p = Process(target=run_proc, args=('kuang_b',))
    # 启动子进程
    p.start()
    # 等子进程结束，才往下执行
    p.join()
    print('Child process end.')

