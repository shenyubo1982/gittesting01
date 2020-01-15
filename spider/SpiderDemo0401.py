## 四、建档的网页爬虫开发

##学习使用自动化的方式来获取网页源代码。
## requests是python的一个第三方thhp（Hypertext Transfer Protocol,超文本传输协议）库，
## 它比python自带的网络库urllib更加简单
## 第四章学习目标：1.requests安装使用； 2.多线程爬虫开发； 3.爬虫常见算法


## 安装
## 方法一、pip3 install 第三方库的名字
## pip3 install requests
## 方法二、打开网页，下载zip，解压源码，找到setup.py
## phthon3 setup.py install


# 使用request获取源代码
## sample 02
import requests
import re
##source = requests.get('https://www.baidu.com').content.decode()

##print(source)


## 1.GET方法
## 对于使用GET方式的网页，在python里面可以使用requests的get()方法获取网页的源代码
## sample 03
url1 = 'http://sports.sohu.com/?spm=smpc.home.top-nav.7.15790513720807nJw45N'
url2 = 'https://movie.douban.com/chart'
url22 = 'https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action='
url23 = 'https://movie.douban.com/top250'
url231 = 'https://movie.douban.com/top250?start=25&filter='
url3 = 'https://www.baidu.com'
url_get_test ='http://exercise.kingname.info/exercise_requests_get.html'
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"


html = requests.get(url=url_get_test,headers={'user-Agent':user_agent})
html_txt = html.text  ## 只获取文本
html_bytes = html.content #获取网页完整内容
html_str = html_bytes.decode()
## decode 默认使用utf-8编码格式吧bytes型解码为字符串，
## 如果一些中文网站，格式可能不是utf-8，需要在括号中标明编码格式如下：
## decode('GBK') 等

print(html_str)

## 2.POST方式
## post方法主要用于向服务器发送大量数据并接受服务器的返回
## post方法不仅可以提交文本数据，还可以提交二进制数据
## 绝大数情况下，只支持post方法的url不能直接使用浏览器访问
## post一般都需要提交参数
## requests的post方法能够获取支持post方法的url的数据
## 返回的数据类型是bytes的字符串
## sample 04
url_post_test = 'http://exercise.kingname.info/exercise_requests_post'
url_post1 = 'https://sm.ms/api/upload'

## 1.使用二进制方式打开一张图片
pic1 = '/Users/bobo/shenyubo1982/gittesting01/spider/posttest.jpg'
f = open(pic1,'rb')
data = {'smfile':f}
## files 可以是字典、json等各种参数
content = requests.post(url_post1,files=data).content
print(content.decode())
f.close()
##api提示失败，因为图床已经使用了v2的api库，需要认证

## sample 05
## 对练习网址，使用2中提交方式
## data方式
dataposttest = {'name':"shenyubo",'password':1234567}
jsonposttest = {'name':"LILI",'password':98765}
contentposttestdt = requests.post(url_post_test,data=dataposttest).content.decode()

print(contentposttestdt)
## json方式
contentposttestjs = requests.post(url_post_test,json=jsonposttest).content.decode()
print(contentposttestjs)



# 结合requests与正则表达式
# 把测试网址，提交后的信息提取出来
titledt = re.search('title>(.*?)<',contentposttestdt,re.S).group(1)
print(titledt)
contentdt = re.findall('p>(.*?)<',contentposttestdt,re.S)
print("".join(contentdt))

titlejs = re.search('title>(.*?)<',contentposttestjs,re.S).group(1)
print(titlejs)
contentjs = re.findall('p>(.*?)<',contentposttestjs,re.S)
print("".join(contentjs))





