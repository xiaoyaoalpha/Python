#encoding:utf-8
from Testcore.TestGeneId import TestGeneid
import xlrd,os
from Testcore.TestSuite import TestSuite
class TestPlan:
    #测试计划id
    testplanid=TestGeneid().getuuid()
    #测试计划创建者
    testplanuser=""
    #测试计划创建日期
    testplandate=""
    #测试计划名称
    testplanname=""
    #测试计划前置条件
    testplanrequirement=""
    #测试计划目标
    testplandst=""
    #测试计划执行批次号
    testplanrunNo=""
    #测试计划开始时间
    testplanstarttime=""
    #测试计划结束时间
    testplanendtime=""
    testsuiteList=[]
    #测试计划结果
    result=0
    def __TestPlan__(self,filepath):
        bk=xlrd.open_workbook(filepath)
        sh1=bk.sheet_by_name(u"计划描述")
        self.__settestplanname__(sh1.row_values(1)[1])
        self.__settestplanuser__(sh1.row_values(0)[1])
        self.__settestplandate__(sh1.row_values(0)[3])
        self.__settestplanrunNo__(sh1.row_values(2)[1])
        sh2=bk.sheet_by_name(u"执行计划")
        nrows=sh2.nrows
        localdir=os.path.abspath("..")
        for i in range(1,nrows):
            ts=TestSuite()
            ts.__settestsuitenum__(sh2.row_values(i)[0])
            testsuitefilepath=localdir+"\\TestSuite"+"\\"+sh2.row_values(i)[1]
            ts.__TestSuite__(testsuitefilepath)
            self.testsuiteList.append(ts)
    def __settestplanid__(self,testplanid):
        self.testplandst=testplanid
    def __gettestplanid__(self):
        return self.testplanid
    def __settestplanuser__(self,testplanuser):
        self.testplanuser=testplanuser
    def __gettestplanuser__(self):
        return self.testplanuser
    def __settestplandate__(self,testplandate):
        self.testplandate=testplandate
    def __gettestplandate__(self):
        return self.testplandate
    def __settestplanname__(self,testplanname):
        self.testplanname=testplanname
    def __gettestplanname__(self):
        return self.testplanname
    def __settestplanrequirement__(self,testplanrequirement):
        self.testplanrequirement=testplanrequirement
    def __gettestplanrequirement__(self):
        return self.testplanrequirement
    def __settestplandst__(self,testplandst):
        self.testplandst=testplandst
    def __gettestplandst__(self):
        return self.testplandst
    def __settestplanrunNo__(self,testplanrunNo):
        self.testplanrunNo=testplanrunNo
    def __gettestplanrunNo__(self):
        return self.testplanrunNo
    def __settestplanstarttime__(self,testplanstarttime):
        self.testplanstarttime=testplanstarttime
    def __gettestplanstarttime__(self):
        return self.testplanstarttime
    def __settestplanendtime__(self,testplanendtime):
        self.testplanendtime=testplanendtime
    def __gettestplanendtime__(self):
        return self.testplanendtime
    def __setresult__(self,result):
        self.result=result
    def __getresult__(self):
        return self.result
    def __settestsuiteList__(self,testsuiteList):
        self.testsuiteList=testsuiteList
    def __gettestsuiteList__(self):
        return self.testsuiteList