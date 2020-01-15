## 12-05 创建多线程
##
#  所有的进程都是通过它的父进程来创建的
#  python程序也是一个进程，我也可以在python程序中再创建进程。
#  多个进程可以实现并发效果，可以让程序的执行速度变快

## multiprocess模块
## multiprocess是python中的一个操作，管理进程的包。在里面包含了和进程有关的所有子模块。
## 大致分为四部分：创建进程、进程同步、进程池、进程之间数据共享。

## Process类介绍
## process(group,target,name,args,kwargs)
## 由该类实例化得到的对象，表示一个子进程中的任务（尚未启动）
## 重点：1.需要使用关键字的方式来指定参数
## 重点：2.args指定的是传给target函数的位置参数，是一个元祖形式，必须有逗号
## 参数1.group参数未使用，值始终未None
## 参数2.target表示调用对象，即子进程要执行的任务
## 参数3.args表示调用对象的位置元祖，args=(1,2,'kkk',)
## 参数4.kwargs表示调用对象的字典，kwargs={'name':'kkk','arg':18}
## 参数5.namne是子进程的名称

#开进程的方法一：
import time
import random
from multiprocessing import Process

def piao(name):
    print('%s piaoing' %name)
    sleeprnd =random.randrange(1,5)
    print(sleeprnd)
    time.sleep(sleeprnd)
    print('%s piao end' %name)


if __name__ == '__main__':
    p1 = Process(target=piao,args=('kkk',)) ##必须加逗号
    p2 = Process(target=piao,args=('ttt',)) ##必须加逗号
    p3 = Process(target=piao,args=('aaa',)) ##必须加逗号
    p4 = Process(target=piao,args=('bbb',)) ##必须加逗号

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('主线程')