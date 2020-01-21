##

import os

def getcpuct():
    print('目前cpu个数：%s' %os.cpu_count())
    ## 这边看到的结果，可能是超核后的结果，4核双线程 就是8







if __name__ == '__main__':
    getcpuct()