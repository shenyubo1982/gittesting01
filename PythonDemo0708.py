import sys
sys.setrecursionlimit(1200)
##07-08 函数递归
## 一、函数递归调用介绍
## 二、回溯与递推


##一、函数递归调用介绍
##函数不仅可以嵌套定义，还可以嵌套调用，即在调用一个函数的过程中
##函数内部又调用另一个函数，而函数的递归调用指的是在调用一个函数
##的过程中又直接或间接地调用该函数本身

##例如 在下面的例子中，调用f1的过程中，又调用f1，这就是直接调用函数f1本身
# sample 01
##def f1():
##    print('from f1')
##    f1()
##
##f1()

## 在调用f1的过程中，又调用f2，而在调用f2的过程中又调用f1，这就是间接调用函数f1本身
## sample 02

##def f1(depth):
##    depth +=1
##    print('from f1 depth:%s' %depth)
##    f2(depth)
##
##def f2(depth):
##    depth+=1
##    print('from f2 depth:%s' %depth)
##    f1(depth)
##
##
##f1(0)

## 可以看出以上两种情况下的递归调用都是一个无限循环的过程，
## 但是python对函数的递归调用的深度做了限制，因而并不会像大家所想的
## 的那样进入无限循环，会抛出异常，要避免出现这种情况，就必须让递归调用在满足某个特定条件下结束。
## 提示：1.可以使用sys.getrecursionlimit()去查看递归深度，默认是1000，虽然可以使用
## 提示：2.python不是移门函数式编程语言，无法对递归进行尾递归优化。


##二、回溯与递推
## 用一个浅显的例子，阐述递归的原理和使用:
## 某公司四个员工坐在一起，问第四个人薪水，他说比第三个人多1000
## 问第三个人薪水，他说比第二个人多1000
## 问第二个人薪水，他说比第一个人多1000
## 最后第一个人说他薪水5000，问第四个人薪水

##解析 要知道第四个人的薪水必须知道第三个，取决于第二人和第一个人，

## salary(4)=salary(3)+1000
## salary(3)=salary(2)+1000
## salary(2)=salary(1)+1000
## salary(1)=5000
## -> salary(n)=salary(n-1)+1000 [n>1]
## -> salary(1)=5000
##这是一个很明显的递归过程，可以将该过程分为两个阶段：回溯和递推

## 代码实现

def salary(n):
    if n == 1 :
        return 5000
    return salary(n-1)+1000

print(salary(4))

## 递归本质就是在做重复的事情，所以理论上递归可以解决的问题循环也都可以解决
## 只不过在某些情况下，使用递归会更容易实现，比如：
##有一个嵌套多层的列表，要求打印出所有的元素，
item=[[1,2],3,[4,[5,[6,7]]]]

def foo(items):
    for i in items:
        if isinstance(i,list):
            foo(i)
        else:
            print(i,end=' ')

foo(item)

##使用递归，我们只需要分析出重复执行的代码逻辑，然后提取进入
##下一次递归调用的条件或者说递归结束的条件即可，代码实现起来简洁清晰

