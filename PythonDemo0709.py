##07-09 面向过程与函数式
## 一、编程范式
## 二、面向过程
## 三、函数式
## 3.1 匿名函数与lambda
## 3.2 map、reduce、filter



## 3.1匿名函数与lambda
## 语法： lambda 参数1，参数2，...:expression
#lambda x,y,z:x+y+z
### example 01
res=(lambda x,y,z:x+y+z)(1,2,3)  ##调用方式1
print(res)

func = lambda a,b,c,d:a+b+c+d   ## 调用方式2
res2 = func(1,2,3,4)
print(res2)

## 匿名函数通常与其他函数配合使用，我们用下述字典为例来介绍它
## sample 02
salaries ={
    'siry':3000,
    'tom':7000,
    'lili':10000,
    'jack':2000
}

##要想要取得薪水的最大值和最小值，我们可以使用内置函数max和min（为了方便开发，
##python解释器已经为我们定义好了一系列常用的功能，称之为内置的函数，我们只需要拿来用即可）

print("工资max的是：", max(salaries))
print("工资min的是：", min(salaries))
## 问题：内置max和min都支持迭代器协议，工作原理都是迭代字典，取得是字典的key，
## 因此，比较的是key的最大和最小值，而我们想要的是比较value的最大值和最小值，
## 于是，做一下改动
print("改造后")
print("工资最大的是：",max(salaries,key=lambda k:salaries[k]))
##函数max会迭代字典salaries，每取出一个"人名"就会当做参数传递给制定的匿名函数，
## 然后将匿名函数的返回值当做比较依据，最终返回薪资最高的那个人名字
## With two or more arguments, return the largest argument.
print("工资最低的是：", min(salaries,key=lambda k:salaries[k]))

print("按照姓名排序：",sorted(salaries))
print("按照工资大小排序：",sorted(salaries,key=lambda k:salaries[k]))

## 3.2 map、reduce、filter
## 函数map、reduce、filter都支持迭代器协议、用来处理可迭代对象，
## 我们以一个可迭代对象array为例来介绍它的三个用法
## sample 03 对array的每个元素做平方处理，可以使用map函数
## map函数可以接受两个参数，一个是函数，另外一个是可迭代对象，具体用法如下：
array =[1,2,3,4,5]
res=map(lambda x:x**2,array)
print(res)
## 解析：map会依次迭代array，得到的值依次传给匿名函数，而map函数得到的结果仍然是迭代器
print(list(res))

## sample 04 对array进行合并操作，比如求和运算，这就用到了reduce函数
## reduce函数可以接受三个参数，第一个是函数，第二个是可迭代对象，第三个初始值
## reduce在python2是内置函数，在python3被集成到了模块functools中，需要导入才能使用


from functools import reduce
res = reduce(lambda x,y:x+y,array)
print("reduce 结果：",res)
##解析：
##1.没有初始值，reduce函数会先迭代一次array得到的值作为初始值，
##  作为第一值数传递给x，然后继续迭代一次array得到的值作为第二个值传递给y，运算结果为3
##2.将上一次reduce运算的结果作为第一值传给x，然后迭代一次array得到的结果作为第二个值传给y，
##  依次类推，直到迭代完array的所有元素，得到最终结果15
##也可以为reduce制定初始值
res=reduce(lambda x,y:x+y,array,100)
print("reduce 100 的结果：",res)


## sample 05 对array进行过滤操作，这就要用到了filter函数，比如过滤大于3的元素
res= filter(lambda x:x>3,array)
print("filter >3 :",list(res))


