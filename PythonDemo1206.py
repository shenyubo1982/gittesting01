## 12-06 进程知识

##进程隔离：安全性通过禁止进程间内存的访问可以方便时实现

from multiprocessing import Process

#sample 01
n=100

def work():
    global n
    n=0
    print('子进程内：',n)

if __name__ == '__main__':
    p = Process(target=work)
    p.start()
    print('主进程内：',n)
