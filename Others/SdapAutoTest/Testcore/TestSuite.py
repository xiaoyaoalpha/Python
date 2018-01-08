#encoding:utf-8
from Testcore.TestGeneId import TestGeneid
from Testcore.TestCase import TestCase
import xlrd,os
class TestSuite:
    #通过ID生成器获取唯一标识
    uid=TestGeneid().getuuid()
    #测试场景序号
    testsuitenum=""
    #测试场景名称
    testsuitename=""
    #测试场景描述
    testsuitedesc=""
    #作者
    createUser=""
    #创建时间
    createDate=""
    #前置条件
    requirement=""
    #执行开始时间
    startTime=""
    #执行结束时间
    endTime=""
    #执行结果
    result=0
    #定义测试用例执行列表
    testcaseList = []
    #定义测试用例运行时数据MAP
    testsuiteRuntimeData={}
    def __TestSuite__(self,filepath):
        bk=xlrd.open_workbook(filepath)
        sh=bk.sheet_by_name(u"场景描述")
        self.__setcreateuser__(sh.row_values(0)[1])
        self.__setcreatedate__(sh.row_values(0)[3])
        self.__settestsuitename__(sh.row_values(1)[1])
        self.__settestsuitedesc__(sh.row_values(2)[1])
        self.__setrequirement__(sh.row_values(3)[1])
        sh=bk.sheet_by_name(u"场景执行步骤")
        nrows=sh.nrows
        localdir=os.path.abspath("..")
        for i in range(1,nrows):
            tc=TestCase()
            tc.__settestcasenum__(sh.row_values(i)[0])
            testcasefilepath=localdir+"\\Testcase"+sh.row_values(i)[1]
            tc.__TestCase__(testcasefilepath,self.__gettestsuitenum__())
            self.testcaseList.append(tc)
    def __setuid__(self,uid):
        self.uid=uid
    def __getuid__(self):
        return self.uid
    def __settestsuitename__(self,testsuitename):
        self.testsuitename=testsuitename
    def __gettestsuitename__(self):
        return self.testsuitename
    def __settestsuitedesc__(self,testsuitedesc):
        self.testsuitedesc=testsuitedesc
    def __gettestsuitedesc__(self):
        return self.testsuitedesc
    def __setcreateuser__(self,createuser):
        self.createUser=createuser
    def __getcreateuser__(self):
        return self.createUser
    def __setcreatedate__(self,createdate):
        self.createDate=createdate
    def __getcreatedate__(self):
        return self.createDate
    def __setrequirement__(self,requirement):
        self.requirement=requirement
    def __getrequirement__(self):
        return self.requirement
    def __setstarttime__(self,starttime):
        self.startTime=starttime
    def __getstarttime__(self):
        return self.startTime
    def __setendtime__(self,endtime):
        self.endTime=endtime
    def __getendtime__(self):
        return self.endTime
    def __setresult__(self,result):
        self.result=result
    def __getresult__(self):
        return self.result
    def __settestcaseList__(self,testcaseList):
        self.testcaseList=testcaseList
    def __gettestcaseList__(self):
        return self.testcaseList
    def __settestsuiteRuntimeData__(self,testsuiteRuntimeData):
        self.testsuiteRuntimeData=testsuiteRuntimeData
    def __gettestsuiteRuntimeData__(self):
        return self.testsuiteRuntimeData
    def __settestsuitenum__(self,testsuitenum):
        self.testsuitenum=testsuitenum
    def __gettestsuitenum__(self):
        return self.testsuitenum