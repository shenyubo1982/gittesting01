## 12-06 进程知识
# 主进程创建守护进程
## 1.守护进程会在主进程代码执行结束后就终止
## 2.守护进程内无法再开启子进程，否则抛出异常
## AssertionError:daemonic processes are not allowed to have children
## 进程之间是互相独立的，主进程代码运行结束，守护进程随即终止。


#sample 01
import  os
import time
from multiprocessing import Process

class Myprocess(Process):
    def __init__(self,person):
        super().__init__()
        self.person = person

    def run(self):
        print(os.getpid(),self.name)
        print('%s正在和女主播聊骚' %self.person)



p = Myprocess('炮王')
p.daemon = True
p.start()
time.sleep(20)
print('主')

## 在shell用以下命令观察进程（父进程和子进程ID）
## ps -le | grep "Python"




