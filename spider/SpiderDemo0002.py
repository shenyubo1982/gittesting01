## 半自动爬虫
## 抓取百度贴吧，
# 其中一篇热门帖子的每层楼的发帖人、发帖内容和发帖时间抓取下来。

##一、手动保存贴吧html源代码
## /users/bobo/shenyubo1982/gittesting01/html/source.txt

## 读取html源码
import re
import csv

def spiderdemo0002():

    with open('/users/bobo/shenyubo1982/gittesting01/html/source.txt',encoding='utf-8') as f:
        index = 0
        ## contexts = f.readlines()
        contexts = f.read()
        ##print(contexts)
        ## for context in contexts:
        ##    index+=1
        ##    print("index:%s, %s" %(index,context.strip()))
        ##print("index:%s| context:%s" %(index,context))

        ## 取出30个评论块
        talkblocks_start = "l_post j_l_post u_post_bright"
        talkblocks_end = "lzl_editor_container j_lzl_e_c lzl_editor_container_s"

        talkblockslist = re.findall('l_post j_l_post l_post_bright(.*?)<div class="clear"></div>'
                              ,contexts,re.S)
        ## 写csv文件头
        writecsvhead()
        '''<div class="clear"></div>'''
        for talkblock in talkblockslist:
            index+=1
            ## 每个评论块:talkblock
            ##print("index:%s,context:%s" %(index,talkblock))
            ## TODO 找用户名 step1 取名字相关模块
            '''style="width:13px;height:13px"></a>'''
            '''<li class="d_name" data-field='''
            '''</li>'''
            talkblock_names = re.findall('<li class="d_name" data-field=(.*?)</li>'
                                         ,talkblock,re.S)

            ##if talkblock_names == None:
            ##print("index:%s,talkblock_name:%s" % (index,"".join(talkblock_names)))

            index_bn = 0
            for tbnamare in talkblock_names:
                index_bn+=1
                ##print("index:%s,indexbn:%s,name:%s" % (index, index_bn, tbnamare))
                ## TODO 将名字模块拆分后，取具体的名字
                talkblockname= re.findall('target="_blank">(.*?)<'
                                          ,tbnamare,re.S)
                ## TODO 如果名字之前有图片（之前的正则没有匹配上的情况下，再用新规则匹配一次）
                if ("".join(talkblockname) == ""):
                    ##print('================没找到=============')
                    talkblockname = re.findall('style="width:13px;height:13px">(.*?)<'
                                               ,tbnamare,re.S)
                    '''style="width:13px;height:13px">Cipher</a>'''
                    ##print("再次匹配结果：",talkblockname)

                ##print("index:%s,indexbn:%s,name:%s" % (index, index_bn, "".join(talkblockname)))

                '''target="_blank">'''
                '''<'''



            ## TODO 找评论内容
            talkblock_contexts = re.findall('class="d_post_content j_d_post_content  clearfix" style="display:;">(.*?)</div><br>',
                                            talkblock,re.S)
            index_bl = 0
            for talkblock_context in talkblock_contexts:
                index_bl+=1
                print("index:%s,indexbl:%s,context:%s" %(index,index_bl,talkblock_context))
                '''class="d_post_content j_d_post_content  clearfix" style="display:;">'''
                '''</div><br>'''

            ## TODO 找日期
            ##print("index:%s,blockcontext:%s" %(index,talkblock))
            talkblock_date = re.findall('</span></li><li><span>(.*?)</span></li></ul>'
                                        ,talkblock,re.S)

            ##print("index:%s,date:%s" %(index,talkblock_date))
            ##print("index:%s,date:%s" %(index,"".join(talkblock_date)))

            ## </span></li><li><span>
            ## </span></li></ul>

            ## TODO 写csv
            writecsvdata("".join(talkblockname)
                         ,"".join(talkblock_context)
                         ,"".join(talkblock_date))


def writecsvhead():
    ##写文件头
    '''baiduresult.csv'''
    with open('/users/bobo/shenyubo1982/gittesting01/html/baiduresult.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'context', 'date'])
        writer.writeheader()


def writecsvdata(name,context,date):
    with open('/users/bobo/shenyubo1982/gittesting01/html/baiduresult.csv', 'a', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'context', 'date'])
        writer.writerow({'name':name
                            ,'context':context
                            ,'date':date})


spiderdemo0002()
