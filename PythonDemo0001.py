# python:  cmd,file =str.split() 调查
# split 方法学习
# 参数：str 分隔符，默认为所有的空字符，包括空格、换行(\n)，制表符(\t)等
# 返回值： 分割后的字符串列表

## sample 01

str1 = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print("打印str1")
print(str1)

print("\n打印str1.split()")
print(str1.split()) ## 以空格为分隔符，包含 \n（换行）
## >> ['Line1-abcdef', 'Line2-abc', 'Line4-abcd']

print(" \nstr1.split(' ',1)的结果：")
print(str1.split(' ',1)) ##以空格为分隔符，分割成2个

res1,res2 = str1.split(' ',1) ##将分割后的内容分别赋给变量
print("res1:",res1)
print("res2:",res2)



## sample 02
import  re
mystr = 'www.baidu.com'
print(mystr)
print(re.split('.',mystr))
print(re.split('\.',mystr))
## 在用了re模块（python正则表达式） 后，
## .是匹配了除了换行符以外的任意字符。所以要加一个斜杠转义一下。




