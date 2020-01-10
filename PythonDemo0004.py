##用python 匿名函数做一个功能 将list内容换行打印出来 ##lambda k:print(k,end=''),(listA) ##print(lambda k:listA[k](listA),end='') ##for l1 in listA:
##    print(l1,end='\n')


def showlinefeed(obj):
    print("开始打印....")
    for o in obj:
        print(o,end='\n')



def unittest():
    if __name__ == 'main':
        listA = list(['a', 'b', 'c', 'd'])
        array = ["ary1", "ary2", "ary3", "ary4"]
        stra = "abdcdefg"

        kv={"aaa","bbb","CCC","DDD"}

        print('showlinefeed TESTING...(list)')
        showlinefeed(listA)
        print('showlinefeed TESTING...(array)')
        showlinefeed(array)
        print('showlinefeed TESTING...(str)')
        showlinefeed(stra)
        print('showlinefeed TESTING...(seta)')
        showlinefeed(kv)

unittest()
