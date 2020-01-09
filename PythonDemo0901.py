## 09-01 面向对象编程


from Student import Student

#print(Student.__dict__)

stu1 = Student('bobo','男',30)
stu2 = Student('jojo','女',28)
#stu3 = Student()

print(Student)
print(stu1.__dict__)
print(stu2.__dict__)
stu1.choose()


print("School name is :",stu1.school)
stu1.school = 'aaa'
print("School name is :",stu1.school)


##操作对象属性
del stu1.school
print("School name is :",stu1.school)
del stu1.sex
print(stu1.__dict__)
## print("sex is:", stu1.sex) ## 如果执行会报错，因为sex已被删除



## 3.2.2 熟悉查找顺序与绑定的方法
## 对象的名称空间里至存放着对象独有的熟悉，而对象们相似的熟悉是存放于类中的。
## 对象在访问属性时，会优先从对象本身的__dict__中查找，未找到，则去类的__dict__中查找


## 1.l 类中定义的变量是类的数据属性，是共享给所有对象用的，指向相同的内存地址
# sample 02
print(id(Student.school))
print(id(stu1.school))
print(id(stu2.school))

## 2.勒种定义的函数是类的函数属性，类可以使用，单必须遵循函数的参数规则，有几个参数需要传几个参数
print("--------Student.choose(stu1)---start")
Student.choose(stu1)
print("--------Student.choose(stu1)---end")

## 但其实勒种定义的函数主要是给对象使用的，而且是绑定给对象的，
## 虽然所有对象指向的都是相同的功能，但是绑定到不同的对象就是不同的绑定方法
## 内存地址各不相同
print("--------sut2.choose()---start")
stu2.choose()
print(stu2.choose)
print("--------sut2.choose()---end")

print("--------sut1.choose()---start")
stu1.choose()
print(stu1.choose)
print("--------sut1.choose()---end")

## 绑定到对象的方法特殊之处在于，绑定给谁就应该由谁来调用，
## 谁来调用，就会将'谁'本身当做第一个参数自动传入（方法__init__也是一样的道理）


## sample 03
print("sample 03")
print(list)
l1=list([1,2,3])
l2=list(['a','b','c'])
l3=list(['x','y'])

print("l1.append:")
print(l1.append)
print("l2.append:")
print(l2.append)
print("l3.append:")
print(l3.append)

l1.append(4)
print(l1)
print(l2)
print(l3)





