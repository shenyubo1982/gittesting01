## python 文件操作

## 1.文件读写
##
# 方式一：需要手动关闭文件
# f = open('文件路径'，'文件操作方式'，encoding='utf-8')
# 对文件进行操作
# f.close()
#
# 方式二:不需要手动关闭文件
# with open('文件路径'，'文件操作方式'，encoding='utf-8') as f:
#       对文件进行操作
#
#
#
# ,
import  os
cwd = os.getcwd()
files = os.listdir(cwd)
print("files in %r:%s" %(cwd,files))
real_path = os.path.expanduser('~/shenyubo1982/gittesting01/html')
print(real_path)


##打开文件，行读取
#sample 01
with open('/users/bobo/shenyubo1982/gittesting01/html/source.txt',encoding='utf-8') as f:
    content_list = f.readline()
    print(content_list)

##打开文件，全部内容用一个字符串返回
##sample 02
with open('/users/bobo/shenyubo1982/gittesting01/html/source.txt', encoding='utf-8') as f:
    content_all = f.read()
    print(content_all)



## python写文本文件
# 方式：
# with open('文件路径'，'w',encoding='utf-8') as f:
#      通过f写文件
# 参数：w 会覆盖原来的文件，a把新的内容写在原来的文件末尾。
#       f.write("一大段文字")
#       f.writelines(['第一段话','第二段话','第三段'])
# python写文件是不会自动换行的，需要人工输入换行符

##sample03
with open('/users/bobo/shenyubo1982/gittesting01/html/filewritetest.txt', 'w',encoding='utf-8') as f:
    f.write('[modify1] \n[modify2]')
    f.writelines(['aaaa \n','bbbbbbb \n','cccccc \n'])

## python 读写csv文件
## 1.导入csv模块 import csv
#  2.先以文本文件的方式打开，再讲文件对象传递给csv模块
#   读取文本内容的代码必须放在缩减内部进行
# ，



## python 写csv
#
#
#
# ，

csvdata = [
    {'name':'bobo'
     ,'age':24
     ,'salary':10000},
    {'name': 'jimmy'
        , 'age': 30
        , 'salary': 20000},
    {'name': 'frank'
        , 'age': 25
        , 'salary': 15000},
    {'name': 'shary'
        , 'age': 20
        , 'salary': 8000}
]

import csv
## sample 04
with open('/users/bobo/shenyubo1982/gittesting01/html/result.csv','w', encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=['name','age','salary'])
    writer.writeheader()
    writer.writerows(csvdata)
    writer.writerow({'name':'superman','age':100,'salary':0})

# sample 05
with open('/users/bobo/shenyubo1982/gittesting01/html/result.csv',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ##print(row)
        ## TODO
        name = row['name']
        salary = row['salary']
        age = row['age']
        print("用户名 %s,年龄 %s" %(name,age))





