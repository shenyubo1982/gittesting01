##模块
# 一个py文件就是一个模块
# 导入模块可以应用模块中已经写好的功能。
# 使用模块既保证了戴梦得重要性，有增强了程序的结构性和维护性
# 另外除了自定义模块外，我们还可以导入使用内置或第三方模块提供的现成功能，
# 这种拿来主义极大提高了程序员的开发效率

## 模块的使用
# import语句
## import 首次导入模块会做三件事情
## 1.执行源文件代码
## 2.产生一个新的名称空间用于存放源文件执行过程中产生的名字
## 3.在当前执行文件所在的名称空间中得到一个名字PythonDemo0801foo，
##   该名字纸箱新创建的模块名称空间，若要引用模块名称空间中的名字，需要加上该前缀

##sample 01

import PythonDemo0801foo  ##导入模块

##a = PythonDemo0801foo.x   ##引用模块中变量x的值赋值给当前名称空间中的名字a
##PythonDemo0801foo.get()    ## 调用模块的get函数
##PythonDemo0801foo.change() ## 调用模块中的change函数
##obj= PythonDemo0801foo.Foo  ## 使用模块的类Foo来实例化，进一步可以执行obj.func()
##
#### 加上PythonDemo0801foo.作为前缀就相当于指名道姓地说明要引用该名称空间中的名字，
#### 所以肯定不会与当前执行文件所在的名称空间中的名字相冲突，
#### 并且若当前执行文件的名称空间中存在x，执行get()或change()操作的都是源文件中的全局变量x
##
#### 需要强调的一点是，第一次导入模块已将其加载到了内存空间中，
#### 之后的重复导入会直接引用内存中已存在的模块，不会重复执行文件，
#### 通过import sys，打印sys.modules的值可以看到内存中已经加载的模块名
##import  sys
##
##print(list(sys.modules))
##
#### 1.在python中，模块也属于第一类对象，可以进行赋值、以数据形式传递以及作为容器类型的元素等操作。
#### 2.模块名应该遵循小写形式，标准库从python2过度到python3做出了狠毒哦这类的调整
#### 比如：ConfigParser、Queue、SocketServer全更新为纯小写形式。
##
#### 导入模块的顺序标准
#### 1.python内置模块
#### 2.第三个模块
#### 3.程序员自定义模块
##
#### 如果再函数内部导入模块，则属于局部的作用域。
##
##
####2.2 from-import 语句
#### from 模块名 import 内容
##from PythonDemo0801foo import x,get,change
##a=x
##get()
##change()
#### 如此导入模块后，调用的时候不用使用模块名
##
##
#### 2.3 导入as
##import PythonDemo0801foo as f
####print("import PythonDemo0801foo as f")
####a=f.x
####f.add()
####f.get()
####print("makecount testing...")
######f.makecounttest()
####
####print("sys.path")
####print(sys.path)
####f.makecounttest()
print("demo0801 __name__:",__name__)
