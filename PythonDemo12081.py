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

## 代码实现
#sample 01

from multiprocessing import Queue,Process
import  time


def sample01():

    q = Queue(3) ##创建一个最大只能容纳3个数据的队列
    '''
    常用方法
    put、get、put_nowait,get_nowait,full,empty
    '''

    q.put(1) ##往队列中存放数据
    q.put(2)
    q.put(3)

    #q.put(3) ## 如果队列已经满了，程序就会停在这里，
    ##等待数据被人取走，在将数据放入队列。如果队列中的数据一直不被取走，
    ##程序就会永远停在这里

    try:
        q.put_nowait(3)
        ##可以使用put_nowait，如果队列满了不会阻塞，但是会因为队列满了而报错。
    except : #因此我们可以用一个try语句来处理这个错误。这样程序不会一直阻塞下去，但是会丢掉这个消息。
        print('队列已经满了')

    ## 因此我们在放入数据之前，可以先看下队列的状态，如果已经满了，就不要继续put了。
    print('队列塞满了吗？', q.full()) ##判断队列中的数据是否已经存放满了。

    print(q.get())  # 从队列中获取数据
    print(q.get())
    print(q.get())

    #print(q.get()) # 同put方法一样，如果度列已经空了，那么继续取值就会出现阻塞。
    try:
        q.get_nowait(3) ##可以使用get_nowait，如果队列满了不会阻塞，但是会因为没有取到值而报错。

    except :
        print('队列已经空了')

    print('对了已经全部取完了吗？',q.empty()) ## 判断队列中数据是否已经被全部取出





if __name__ == '__main__':
    sample01()





