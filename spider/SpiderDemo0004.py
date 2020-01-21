## python 爬虫属于IO密集型程序，所以使用多线程可以大大提高爬取效率。

## multiprocessing 是python的多进程库
## multiprocessing 下面有一个dummy模块，可以让python的进程使用multiprocessing的各种方法。
## dummy下面有一个Pool类，它用来实现线程池。Pool线程池有一个map()方法，
## 可以让线程池里面的所有线程都"同时"执行一个方法。

##sample 单线程与多线程处理0-9的平方

## 单线程

import time
from multiprocessing.dummy import Pool


time_s = time.time()
for i in  range(10):
    print(i**i)
time_e = time.time()
print('耗时：', time_e-time_s)


## 多线程

time_s = time.time()


def calc_power2(num):
    return num**num


pool = Pool(3)
origin_num = [x for x in range(10)]
print(type(origin_num))
result = pool.map(calc_power2,origin_num)
time_e = time.time()
print(result)
print('耗时：', time_e-time_s)


## 惰性求值的概念
## 延迟求值特别用于函数式编程语言中。
## 在使用延迟求值的时候，表达式不在它被绑定到边浪之后就立即求值，
## 而是在该值被取用的时候求值。
## 也就是说，语句如：x:=expression;(把一个表达式的结果赋给一个变量）明显的调用这个表达式
## 被计算并把结果放置到x中，但是先不管实际在x中的是什么，直到通过后面的表达式中，
## 到x的引用而有了对他的值的需求的时候，而后面表达式自身的求值也可以被延迟，
## 最终为了生成让外界看到的某个符号而计算这个快速增长的依赖树

## 问题，以下内容为什么是9
li = [lambda :x for x in range(10)]
res = li[9]()
print('为啥是9? ',res)
## 解答：在print语句中，要求对res进行输出，于是开始求值
## 在[lamdba:x for x in range(10)]中，x循环10次，x计算得9 ，并且
# 返回给li一个10长度的list，内容全是9


#sample 04
f  = lambda x:x*x
print([f(x) for x in range(10)])
##sample04 也sample05 写法等效
#sample 05
print([(lambda x: x * x)(x) for x in range(10)])

#sample 06
print([lambda x: x * x for x in range(10)])
##没有调用函数，它创建了10个lamdba匿名函数，并把他们放入一个list中


## sample 07
a = [lambda x:x*x for x in range(10)]
for aa in a:
    print(aa(2))


li = [(lambda :x for x in range(10))]
li_len = len(li)
print('len:',li_len)

for i in li[0]:
    print(i())

print('------------')
li = [lambda :x for x in range(10)]
for i in li:
    print(i())




