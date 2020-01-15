## 进程同步（multiprocess.Lock)

## 多进程模拟抢票实例（不用互斥锁，并发抢票导致混乱）

from multiprocessing import Process,Lock
import time,json,random

def search():
    dic = json.load(open('db'))
    print('\033[96m剩余票数%s \033[0m' %dic['count'])


def get():
    dic = json.load(open('db'))
    time.sleep(0.1)
    if dic['count'] >0:
        dic['count']-=1
        time.sleep(0.2)
        json.dump(dic,open('db','w'))
        print('\033[43m购票成功 \033[0m')


def task():
    search()
    get()



if __name__ == '__main__':
    for i in range(100):
        p=Process(target=task)
        p.start()
#引发问题：数据写入错乱
