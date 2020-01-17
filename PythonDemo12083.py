## 进程间通讯
#  进程之间数据是互相隔离的，要先实现进程间的通信（IPC机制），
#  需要借助技术实现，比如multiprocessing模块中的
#  队列和管道，这两种方法都可以实现进程间数据传输的，由于队列是管道+锁的方式实现的
#  我们着重研究队列


# 队列： 创建共享的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。
# 队列支持多个人从队列的一端放入数据，同样支持多个人从队列的另一端取数据


## 基本用法
## Queue([maxsize]) #创建共享的进程队列，队列底层使用管道和锁定实现。
#  参数： maxsize是队列中允许的最大项数。如果省略此参数，则无大小限制。

## 基于队列实现进程间通信
#sample 02

from multiprocessing import Queue,Process
import  time

def producer(q):
    q.put('hello big baby!')

def consumer(q):
    print(q.get())


if __name__ == '__main__':
    q = Queue() ##创建一个共享的进程队列
    p1 = Process(target=producer,args=(q,)) ##创建一个进程
    p1.start()
    p2 = Process(target=consumer,args=(q,))
    p2.start()
    ## 实现了2个进程在一个进程队列中存储和读取信息。






