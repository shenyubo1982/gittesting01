## https://www.jinse.com/

## 抓取头条标题/时间/正文连接/
import requests
import lxml.html
import csv

import  re


strhttps = 'https://www.jinse.com'
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"


def gethtml():
    '''
    获取jinse的html源代码
    后续可以动态添加html
    目前无法实现屏幕中下拉，获取翻页数据读取出来的功能，只能拉取第一次请求时候的列表内容。
    :return:
    '''
    html = requests.get(url="https://www.jinse.com", headers={'user-Agent': user_agent})
    html_bytes = html.content #获取网页完整内容
    html_str = html_bytes.decode()
    return html_str


def writehtml(file,html):
    '''
    将html源代码写入本地文件中
    后续文件名可以改成动态（日期：日时分）
    :return:
    '''
    fileob = open(file,'w')
    fileob.write(html)
    fileob.close()
    print('【jinse01html.txt】保存成功')

def openhtml(html):

    fob = open(html,'r',encoding='utf-8')
    source = fob.read()
    return source


def getobjs(source):
    '''
    根据保存的html，找到合适的内容集合
    :return:
    '''

    selector = lxml.html.fromstring(source)

    xpathaddress_title = '//div[@class="js-single__right"]/a/@title'
    xpathaddress_href = '//div[@class="js-single__right"]/a/@href'
    xpathaddress_desc = '//div[@class="js-single__right"]/p[@class="js-single__des"]/text()'

    info_title = selector.xpath(xpathaddress_title)
    info_href = changehref(selector.xpath(xpathaddress_href),strhttps)
    info_desc = selector.xpath(xpathaddress_desc)

    # print('xpath return\'s type is :', type(info_title))
    # print('info_title\'s size is ' , len(info_title))
    # print('info_href\'s size is ' , len(info_href))
    # print('info_desc\'s size is ' , len(info_desc))
    # showinfo(info_title,type='ncross')
    # showinfo(info_href,type='ncross')
    # showinfo(info_desc,type='ncross')

    ## TODO 将获取的内容转zip在一起
    zipobj = zipdict(info_title,info_href,info_desc)
    # print('zipobj\'s type is :',type(zipobj))
    showinfo(zipobj, type='necroses')

    return zipobj


def zipdict(ltitle,lhref,ldesc):
    '''

    :param listA:字典类型的value1
    :param listB:字典类型的value2
    :param listC:字典列席的value3
    :return: 合并后的dict对象
    '''

    keys = ('title','href','desc') ##字典类型的key
    csvdata = []


    try:
        listvalues = list(zip(ltitle,lhref,ldesc))
        index = 0
        ## TODO 合成csvdata
        # for values in listvalues:
        #     zip(keys,values)
        for values in listvalues:
            index+=1
            # print(index)
            # print(keys)
            # print(values)
            csvdata.append(dict(zip(keys,values)))
            # print('index:%s : %s ' %(index,csvdata))

        return csvdata


    except Exception:
        print(Exception.mro())
        return None


def writecsv(file,csvdata):



    with open(file,'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=['title','href','desc'])
        writer.writeheader()
        writer.writerows(csvdata)
        # writer.writerow({'name':'superman','age':100,'salary':0})




def showinfo(object ,type='cross'):
    '''
    测试打印数据，按照默认和竖型方式打印
    :param object: 要打印的对象
    :param type: cross是默认横向打印，否则将对象内容竖着排列打印
    :return: 无
    '''
    if type == 'cross':
        '''默认打印方式'''
        # print('对象打印中....')
        # print(object)
    else:
        '''竖着打印'''
        index = 0
        for obj in object:
            # print("index:1,对象：",end="",lambda x:x for x in object)
            index+=1
            # print("index:%s,%s" %(index,obj))

def changehref(hrefList,fix):

    hreflistRet = []

    for href in hrefList:
        if href.find('/') == 0:
            '''如果href是/开头的话，说明是相对路径，需要修改'''
            hreflistRet.append(fix+href)
        else:
            hreflistRet.append(href)

    return hreflistRet

if __name__ == '__main__':
    ## test mode
    writehtml('jinse01html.txt',gethtml())
    objcsv = getobjs(openhtml('jinse01html.txt'))

    writecsv('jinse01html.csv',objcsv)
    #print(type(obj))

