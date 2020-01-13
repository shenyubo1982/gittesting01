# -*- coding:utf-8 -*
###
# 2.5.1 需求分析使用Python开发一个猜数小游戏。
# 在游戏中，程序每一轮会随机生成一个0～1024之间的数字，
# 用户输入猜测的数字，程序告诉用户猜大了还是猜小了。
# 在一定次数内猜对，则本轮用户获胜，
# 否则本轮用户失败。每一轮开始时，程序会要求用户输入用户名。
# 程序会一直运行，直到用户输入“3”，停止游戏。
# 在每一轮游戏开始前，输入“1”可以查看用户的输入历史。
#

import random
import numpy as np


class GuessNumber(object):

    '''变量定义'''
    ##guessinput={[0,0]}
    inputnumber = 0


    def __init__(self):
        pass



    def guess(self,times):
        '''游戏中，猜数字'''
        if times< self.times :
            '''可继续输入'''
            self.__getnumber(times)



    def newGame(self):
        '''初始化游戏'''
        self.initgame()

    def gameover(self,resBloon):
        '''结束游戏'''
        print("正确结果是:",self.resnumber)
        if resBloon == True:
            print("恭喜获胜！游戏结束...")
        else:
            print("失败！游戏结束...")

    def again(self):
        '''选择游戏'''
        pass

    def showgameresult(self,reslut):
        '''
        显示比赛结果，并清空数据
        :param reslut: win or loss
        :return:
        '''
        print("Ur %s!" %reslut)
        self.__cleardata()

    def __getround(self):
        '''获得随机数0-1024之间'''
        self.resnumber = random.randint(0,1024)

    def getnumber(self,timers):
        '''通过屏幕输入猜测的数字'''
        ##inputn = input("请输入你猜的数字（0-1024）：")
        self.inputnumber = int(input("请输入你猜的数字（0-1024）："))
        ## TODO 如果用户输入his，则显示历史数据

        '''保存输入结果'''
        self.hisdata[timers][[0,0]] = self.inputnumber
        ## hisdata[轮次][[0,0 第一个元素、1,1第二个元素]]
        ##print(self.hisdata)

    def initgame(self):
        '''游戏初始化'''
        self.name = input("请输入玩家姓名：") #玩家姓名
        self.times = int(input("请输入游戏级别（3-10）：")) #选择难度
        self.__getround() ##生成随机数
        self.__setseleve(self.times) ## 生成本轮历史数据结构


        print("玩家%s,你有%d次猜数字的机会！" %(self.name,self.times))
        ##print(self.times)
        ##print(self.resnumber)
        ##print(self.hisdata)


    def checknumber(self,timers):
        '''校验输入的数字与结果是否一致，并给出提示'''
        if self.resnumber == self.inputnumber:
            ## TODO 配对成功
            ## self.showgameresult('Win')
            self.hisdata[timers][[1,1]] = -1
            print("tips：成功")
            return True
        else:
            ## TODO 配对失败
            if self.resnumber < self.inputnumber:
                self.hisdata[timers][[1,1]] = 1 ##输入值大于随机数
                print("tips:输入的数据过大")
                return False
            else:
                self.hisdata[timers][[1,1]] = 2 ##输入值小于随机数
                self.hisdata[timers][[1,1]] = 2 ##输入值小于随机数
                print("tips:输入的数据过小")
                ##self.showgameresult('loss')
                return False



    def __cleardata(self):
        '''清空数据待下次重新游戏'''
        self.times = 0  ## 清空计数器

        ## TODO 清空结果集合

    def __showResult(self,res):
        if res == -1:
            return "匹配成功！"
        elif res ==1 :
            return "过大！"
        elif res ==2:
            return "过小！"


    def __setseleve(self,level):
        '''根据难度创建本轮游戏的数据格式
            结构：[[0,0]  用户猜的数字，结果（0表示小于结果、1表示大于结果）
                 ,[1,1]]
        '''
        self.hisdata = np.zeros((level, 2), dtype=np.int)

    def showlog(self):
        '''【本轮游戏历史输入记录：】'''
        print("【本轮游戏历史输入记录：】")
        index = 0
        for n in self.hisdata:
            index += 1
            if self.__showResult(n[1]) == None:
                break
            else:
                print("第%d轮输入数据：%s ;比较结果：%s" % (index, n[0], self.__showResult(n[1])))



def unitest():
    print(__name__)
    if __name__ == '__main__':
        print("========进入测试模式=======")
        game = GuessNumber()
        ## step1. 开始游戏
        game.newGame()
        ## step2. 按照设定循环输入数字，直到游戏结束或者胜利
        res = False
        for index in range(game.times):
            game.getnumber(index)
            if game.checknumber(index) == True:
                ## TODO 显示游戏获胜，退出循环
                res = True
                break
            game.showlog()
        game.gameover(res)



## UT
unitest()