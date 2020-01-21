import lxml.html
from lxml import etree




source = '''
<html>
    <head>
        <title>测试</title>
    </head>
    <body>
        <div class="useful">
            <ul>
                <li class="info">我需要的信息1</li>
                <li class="info">我需要的信息2</li>
                <li class="info">我需要的信息3</li>
            </ui>
        </div>
        <div class="useless">
            <ui>
                <li class="info">垃圾信息1</li>
                <li class="info">垃圾信息2</li>
            </ui>
        <div>
    </body>
</html>
'''

selector = lxml.html.fromstring(source)
info = selector.xpath('//div[@class="useful"]/ul/li/text()')
print(info)

html = etree.HTML(source)
result = etree.tostring(html)
print(result.decode('utf-8'))


## selector = lxml.html.fromstring('网页源代码')
## info = selector.xpath('一段xpath语句')

## xpath语句格式
## 写xpath就是写地址
## 获取文本：
## //标签1[@属性1='属性值1']/标签2[@属性2='属性值2']/..../text()

## 获取属性值：
## //标签1[@属性1='属性值1']/标签2[@属性2='属性值2']/..../@属性n
## 其中，[@属性='属性值']不是必须的。



