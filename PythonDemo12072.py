## 进程同步（multiprocess.Lock)

## 多进程模拟抢票实例(互斥锁保证数据安全)

from multiprocessing import Process,Lock
import time,json,random

def search():
    dic = json.load(open('db'))
    print('\033[96m剩余票数%s \033[0m' %dic['count'])


def get():
    dic = json.load(open('db'))
    time.sleep(random.random()) ##模拟读数据的网络延迟
    if dic['count'] >0:
        dic['count']-=1
        time.sleep(random.random()) ##模拟写数据的网络延迟
        json.dump(dic,open('db','w'))
        print('\033[41m购票成功 \033[0m')
    else:
        print('\033[41m购票失败 \033[0m')

def task(lock):
    search()
    lock.acquire() ##将买票这个一个环节由并发变成串行，牺牲了运行效率但是保证了数据的安全。
    get()
    lock.release() ##释放锁



if __name__ == '__main__':
    try:
        lock = Lock()
        for i in range(100): ##模拟并发100个客户抢票
            p = Process(target=task(lock, ))
            p.start()
    except KeyboardInterrupt:
        print('testing end for your hand.')


##仍然存在问题：虽然可以用文件共享数据显示进程间数据通信但问题是：
## 1.效率低
## 2.需要自己加锁处理
## 后续需要找到一种更加合理快捷的方法，那就是队列和管道


