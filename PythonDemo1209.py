# -*- coding:utf-8 -*-

## 12-09 生产者消费者模型
## 作用：
## 在并发编程中，使用生产者和消费者模型能够解决绝大多数并发问题。
## 该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度。

## 生产者消费者模型定义
## 通过一个容器来解决生产者和消费者的强耦合问题。
## 生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯。
## 所以生产者生产完数据（做包子的）之后不用等待消费者（吃包子）处理，
## 直接扔给阻塞队列（盘子），消费者不找生产者要数据，
## 而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。


## 为什么要使用生产者和消费者模型
## 在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。
#  在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，
#  那么生产者就必须等待消费者处理完毕后，才能继续生产数。
#  同样的道理，如果消费者处理能力大于生产者，那么消费者就必须等待生产者。
#  为了解决这个问题，就引入了这一模型。
#

## sample 01
## 基于队列实现生产者消费者模型

from multiprocessing import Process,Queue
import  time,random,os

def consumer(q):

    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('%s 吃 %s' % (os.getpid(), res))


def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res = '包子%s' %i
        q.put(res)
        print('%s 生产了 %s' %(os.getpid(),res))



if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer,args=(q,))

    c1 = Process(target=consumer,args=(q,))

    p1.start()
    c1.start()
    print('主线程')
