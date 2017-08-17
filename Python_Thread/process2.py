from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:',__name__)
    if hasattr(os,'getppid'):
        #getppid()得到父进程ID，如果已经是父进程，则返回系统进程ID
        print('parent process:',os.getppid())
    #getpid()得到本身进程ID
    print('process id:',os.getpid())

def f(name):
    print('hello',name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f,args=('bob',))
    p.start()
    p.join()