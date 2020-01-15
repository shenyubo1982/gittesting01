##

from multiprocessing import Process
import  time


def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")


p1=Process(target=foo)
p2=Process(target=bar)

p1.daemon=True
##一定要在start()之前设置，设置P1为守护进程，禁止p1创建子进程，
## 并且父进程或者主进程执行结束，p1立即终止运行，所以p1 foo的print有可能不会被执行

p1.start()
p2.start()
time.sleep(0.1)
print("main-------")
#打印该行则主进程代码结束,则守护进程p1应该被终止.
# #可能会有p1任务执行的打印信息123,
# 因为主进程打印main----时,p1也执行了,但是随即被终止.

