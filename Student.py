class Student:
    school ='清华大学'
    _number = 1234567890

    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age =age



    def choose(self):
        print('%s is choosing a course:' %self.name)


##ython中不存在只能从对象内部访问的“私有(private)”变量，但Python制定了以下公约：
##
##以单下划线开头的成员变量或方法，是设计者不想暴露给外部的API，使用者不应该进行访问。
##以双下划线开头且以至多一个下划线结尾的成员变量或方法，会进行名称转写。
##至于Python为什么通过这样不够强力的手段进行约束，这源于Python这门语言的文化和哲学：简单至上。


