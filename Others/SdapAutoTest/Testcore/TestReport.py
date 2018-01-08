#encoding:utf-8
#encoding:utf-8
import xlwt,xlrd
import time,os
from Testcore.TestCase import TestCase
from Testcore.TestStep import TestStep
from Testcore.TestSuite import TestSuite
from Testcore.TestPlan import TestPlan
#from xlrd import open_workbook
#from xlutils.copy import copy
'''
Created on 2016-11-28

@author: ******
'''
class TestReport:
    tc=0
    t=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    #设置单元格样式 
    def set_style(self,name,height,bold=False):
        # 初始化样式
        style = xlwt.XFStyle() 
        # 为样式创建字体
        font = xlwt.Font() 
        font.name = name 
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font
        return style
    #根据测试执行计划批次编号（code,20161017-01） 生成对应测试报告数据文件 编号相同则覆盖文件
    def __createTestReport__(self,testplan):
        #创建测试报告文件
        #PlanRunNo=str(int(testplan.__gettestplanrunNo__()))
        PlanRunNo=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        if PlanRunNo=='':
            print "测试计划执行编号为空"
            PlanRunNo=self.t+'001'
        reportname=os.path.abspath("..")+"\\Testresult\\"+PlanRunNo+'.xls'
        reportname1=PlanRunNo+self.t+'.xls'
        self.__setreportname__(reportname1)
        #print self.__getreportname__()
        ReportFile=xlwt.Workbook()
        #创建多个测试报告sheet页名称
        ReportFile.add_sheet(u'测试节点树',cell_overwrite_ok=True)
        ReportFile.add_sheet(u'测试计划', cell_overwrite_ok=True)
        ReportFile.add_sheet(u'测试场景', cell_overwrite_ok=True)
        ReportFile.add_sheet(u'测试用例', cell_overwrite_ok=True)
        ReportFile.add_sheet(u'测试步骤', cell_overwrite_ok=True)
        #写入测试节点树表头
        wr_tree = ReportFile.get_sheet(0)
        row0=[u'节点ID',u'父节点ID',u'名称',u'类型']
        #生成测试节点树的表头
        for i in range(0,len(row0)):
            wr_tree.write(0,i,row0[i],TestReport().set_style('Times New Roman',220,True))
        #写入测试计划表头
        wr_plan=ReportFile.get_sheet(1)
        row1=[u"编号", u"测试计划名称", u"描述", u"执行开始时间", u"执行结束时间", u"执行结果"]
        #生成测试计划的表头
        for i in range(0,len(row1)):
            wr_plan.write(0,i,row1[i],TestReport().set_style('Times New Roman',220,True))
        #写入测试场景表头
        wr_suite=ReportFile.get_sheet(2)
        row2=[u"ID", u"测试场景名称", u"描述", u"前置条件", u"执行开始时间", u"执行结束时间", u"执行结果"]
        #生成测试场景的表头
        for i in range(0,len(row2)):
            wr_suite.write(0,i,row2[i],TestReport().set_style('Times New Roman',220,True))
        #写入测试用例表头
        wr_case=ReportFile.get_sheet(3)
        row3=[u"ID", u"所属测试场景ID", u"测试用例名称", u"描述", u"前置条件", u"执行开始时间",u"执行结束时间", u"执行结果"]
        #生成测试用例的表头
        for i in range(0,len(row3)):
            wr_case.write(0,i,row3[i],TestReport().set_style('Times New Roman',220,True))
        #写入测试步骤表头
        wr_step=ReportFile.get_sheet(4)
        row4=[u"ID", u"所属测试用例ID", u"测试步骤名称", u"调用业务组件名称", u"输入数据",u"预期数据", u"执行开始时间", u"执行结束时间", u"执行结果", u"异常信息", u"错误截图"]
        #生成测试步骤的表头
        for i in range(0,len(row4)):
            wr_step.write(0,i,row4[i],TestReport().set_style('Times New Roman',220,True))
        #测试节点树，写入测试计划节点
        p=1
        wr_tree.write(p,0,"0")
        wr_tree.write(p,1,"-1")
        wr_tree.write(p,2,testplan.__gettestplanname__())
        wr_tree.write(p,3,"0")
        p=p+1

        #写入测试计划执行信息
        #编号
        wr_plan.write(1,0,testplan.__gettestplanrunNo__())
        #名称
        wr_plan.write(1,1,testplan.__gettestplanname__())
        #描述
        wr_plan.write(1,2,testplan.__gettestplanname__())
        #执行开始时间
        wr_plan.write(1,3,testplan.__gettestplanstarttime__())
        #执行结束时间
        wr_plan.write(1,4,testplan.__gettestplanendtime__())
        #执行结果
        wr_plan.write(1,5,testplan.__getresult__())
        #写入测试场景、测试用例、测试步骤执行信息
        testsuiteList=testplan.__gettestsuiteList__()
        testsuite=TestSuite()
        testcase=TestCase()
        teststep=TestStep()
        for i in range(0,len(testsuiteList)):
            #获取测试场景
            testsuite=testsuiteList[i]
            #测试节点树，写入测试场景节点信息
            wr_tree.write(p,0,str(testsuite.__gettestsuitenum__()))
            wr_tree.write(p,1,"0")
            wr_tree.write(p,2,testsuite.__gettestsuitename__())
            wr_tree.write(p,3,"1")
            p=p+1
            #写入测试场景执行信息
            #ID
            wr_suite.write(i+1,0,str(testsuite.__gettestsuitenum__()))
            #名称
            wr_suite.write(i+1,1,testsuite.__gettestsuitename__())
            #描述
            wr_suite.write(i+1,2,testsuite.__gettestsuitedesc__())
            #前置条件
            wr_suite.write(i+1,3,testsuite.__getrequirement__())
            #执行开始时间
            wr_suite.write(i+1,4,testsuite.__getstarttime__())
            #执行结束时间
            wr_suite.write(i+1,5,testsuite.__getendtime__())
            #执行结果
            wr_suite.write(i+1,6,testsuite.__getresult__())
            #写入测试场景下的测试用例执行信息
            testcaseList=testsuite.__gettestcaseList__()
            for n in range(0,len(testcaseList)):
                #获取测试用例
                testcase=testcaseList[n]
                print testcase.__gettestcasename__()
                #测试节点树，写入测试用例节点信息
                wr_tree.write(p,0,str(testcase.__getId__()))
                wr_tree.write(p,1,"1")
                wr_tree.write(p,2,testcase.__gettestcasename__())
                wr_tree.write(p,3,"2")
                p=p+1
                #写入测试用例执行信息
                #ID", "所属测试场景ID", "名称", "描述", "前置条件", "执行开始时间","执行结束时间", "执行结果"
                wr_case.write(n+1,0,str(testcase.__gettestcasenum__()))
                wr_case.write(n+1,1,str(testcase.__gettestsuiteId__()))
                wr_case.write(n+1,2,testcase.__gettestcasename__())
                wr_case.write(n+1,3,testcase.__getdec__())
                wr_case.write(n+1,4,testcase.__getrequirement__())
                wr_case.write(n+1,5,testcase.__getstarttime__())
                wr_case.write(n+1,6,testcase.__getendtime__())
                wr_case.write(n+1,7,testcase.__getresult__())
                #写入测试用例下测试步骤执行信息
                teststepList=testcase.__gettestcaseStepList__()
                print self.tc
                for m in range(0,len(teststepList)):
                    #获取测试步骤
                    teststep=teststepList[m]
                    #测试步骤执行信息
                    '''ID, 所属测试用例ID, 步骤名称, 调用业务组件名称, 输入数据,预期数据, 
                                                 执行开始时间, 执行结束时间, 执行结果, 异常信息, 错误截图'''
                    wr_step.write(m+1+self.tc,0,str(teststep.__getId__()))
                    wr_step.write(m+1+self.tc,1,str(teststep.__gettestcaseId__()))
                    wr_step.write(m+1+self.tc,2,teststep.__gettestcasename__())
                    wr_step.write(m+1+self.tc,3,teststep.__getcomponentName__())
                    wr_step.write(m+1+self.tc,4,teststep.__getinputdata__())
                    wr_step.write(m+1+self.tc,5,teststep.__getexpectData__())
                    wr_step.write(m+1+self.tc,6,teststep.__gettestcasestepstarttime__())
                    wr_step.write(m+1+self.tc,7,teststep.__gettestcasestependtime__())
                    wr_step.write(m+1+self.tc,8,teststep.__getresult__())
                    wr_step.write(m+1+self.tc,9,teststep.__getErrorMessage__())
                    wr_step.write(m+1+self.tc,10,teststep.__getErrorpic__())
                self.tc=self.tc+len(teststepList)
        #保存文件
        ReportFile.save(reportname)
        #rb = open_workbook(reportname)
        #wb = copy(rb)
        #wb.save("E:\\1.xls")
    #从测试报告中，根据testplanrunNo查询测试计划基本信息
    def __getTestPlan__(self,testplanrunNo):
        #测试报告路径
        reportpath=os.path.abspath("")+'\\'+testplanrunNo+'.xls'
        #打开测试报告excel
        bk=xlrd.open_workbook(reportpath)
        #获取测试计划的sheet页
        plansh=bk.sheet_by_name(u"测试计划")
        suitesh=bk.sheet_by_name(u"测试场景")
        #测试计划初始化对象
        testplan=TestPlan()
        #编号、测试计划名称、描述、执行开始时间、执行结束时间、执行结果
        testplan.__settestplanrunNo__(plansh.row_values(1)[0])
        testplan.__settestplanname__(plansh.row_values(1)[1])
        testplan.__settestplandec(plansh.row_values(1)[2])
        testplan.__settestplanstarttime__(plansh.row_values(1)[3])
        testplan.__settestplanendtime__(plansh.row_values(1)[4])
        testplan.__setresult__(plansh.row_values(1)[5])
        #读取测试计划所包含的测试场景信息
        testsuite=TestSuite()
        testsuiteList=[]
        n=suitesh.nrows
        #ID 名称    描述    前置条件    执行开始时间    执行结束时间    执行结果
        for j in range(1,n):
            testsuite.__setuid__(suitesh.row_values(j)[0])
            testsuite.__settestsuitename__(suitesh.row_values(j)[1])
            testsuite.__settestsuitedec__(suitesh.row_values(j)[2])
            testsuite.__setrequirement__(suitesh.row_values(j)[3])
            testsuite.__setstarttime__(suitesh.row_values(j)[4])
            testsuite.__setendtime__(suitesh.row_values(j)[5])
            testsuite.__setresult__(suitesh.row_values(j)[6])
            testsuiteList.append(testsuite)
        testplan.__settestsuiteList__(testsuiteList)
        return testplan 
    #根据测试计划testplanrunNo与测试场景testSuiteuid 得到测试场景基本信息  
    def __getTestSutieById__(self,testplanrunNo,testSuiteuid):
        ReportPath=os.path.abspath("")+'\\'+testplanrunNo+'.xls'
        bk=xlrd.open_workbook(ReportPath)
        suitesh=bk.sheet_by_name(u"测试场景")
        casesh=bk.sheet_by_name(u"测试用例")
        n=suitesh.nrows
        m=casesh.nrows
        self.testsuit=TestSuite()
        testcase=TestCase()
        testcaseList=[]
        for i in range(1,n):
            #测试场景：ID 名称    描述    前置条件    执行开始时间    执行结束时间    执行结果
            if suitesh.row_values(i)[0]==testSuiteuid:
                self.testsuit.__setuid__(suitesh.row_values(i)[0])   
                self.testsuit.__settestsuitename__(suitesh.row_values(i)[1])
                self.testsuit.__settestsuitedesc__(suitesh.row_values(i)[2])
                self.testsuit.__setrequirement__(suitesh.row_values(i)[3])
                self.testsuit.__setstarttime__(suitesh.row_values(i)[4])
                self.testsuit.__setendtime__(suitesh.row_values(i)[5])
                self.testsuit.__setresult__(suitesh.row_values(i)[6])                          
            #测试用例:ID    所属测试场景ID    名称    描述    前置条件    执行开始时间    执行结束时间    执行结果
            for j in range(1,m):
                if casesh.row_values(j)[1]==self.testsuit.__getuid__():
                    testcase.__setId1__(casesh.row_values(j)[0])
                    testcase.__settestsuiteId__(casesh.row_values(j)[1])
                    testcase.__settestcasename__(casesh.row_values(j)[2])
                    testcase.__setdec__(casesh.row_values(j)[3])
                    testcase.__setrequirement__(casesh.row_values(j)[4])
                    testcase.__setstarttime__(casesh.row_values(j)[5])
                    testcase.__setendtime__(casesh.row_values(j)[6])
                    testcase.__setresult__(casesh.row_values(j)[7])
                    testcaseList.append(testcase)
                self.testsuit.__settestcaseList__(testcaseList)
            break
        return self.testsuit
    #根据测试计划testplanrunNo与测试用例testCaseId 得到测试用例基本信息
    def getTestCaseById(self,testplanrunNo,testCaseId):
        ReportPath=os.path.abspath("")+'\\'+testplanrunNo+'.xls'
        bk=xlrd.open_workbook(ReportPath)
        casesh=bk.sheet_by_name(u"测试用例")
        n=casesh.nrows
        self.testcase=TestCase()
        #测试用例:ID    所属测试场景ID    名称    描述    前置条件    执行开始时间    执行结束时间    执行结果
        for i in range(1,n):
            if casesh.row_values(i)[0]==testCaseId:
                self.testcase.__setId1__(casesh.row_values(i)[0])
                self.testcase.__settestsuiteId__(casesh.row_values(i)[1])
                self.testcase.__settestcasename__(casesh.row_values(i)[2])
                self.testcase.__setdec__(casesh.row_values(i)[3])
                self.testcase.__setrequirement__(casesh.row_values(i)[4])
                self.testcase.__setstarttime__(casesh.row_values(i)[5])
                self.testcase.__setendtime__(casesh.row_values(i)[6])
                self.testcase.__setresult__(casesh.row_values(i)[7])
                break
        return self.testcase
    #根据测试计划testPlanCode与测试用例testCaseId得到测试用例的测试步骤列表
    def getTestStepListById(self,testplanrunNo,testCaseId):
        ReportPath=os.path.abspath("")+'\\'+testplanrunNo+'.xls'
        bk=xlrd.open_workbook(ReportPath)
        stepsh=bk.sheet_by_name(u"测试步骤")
        teststep=TestStep()
        teststepList=[]
        k=stepsh.nrows
        for i in range(1,k):
            #ID 所属测试用例ID  测试步骤名称    调用业务组件名称    输入数据    预期数据    执行开始时间    执行结束时间    执行结果    异常信息    错误截图
            if stepsh.row_values(i)[1]==testCaseId:
                teststep.__setId__(stepsh.row_values(i)[0])
                teststep.__settestcaseId__(stepsh.row_values(i)[1])
                teststep.__settestcasestepname__(stepsh.row_values(i)[2])
                teststep.__setcomponentName__(stepsh.row_values(i)[3])
                teststep.__setinputdata__(stepsh.row_values(i)[4])
                teststep.__setexpectData__(stepsh.row_values(i)[5])
                teststep.__settestcasestepstarttime__(stepsh.row_values(i)[6])
                teststep.__settestcasestependtime__(stepsh.row_values(i)[7])
                teststep.__setresult__(stepsh.row_values(i)[8])
                teststep.__setErrorMessage__(stepsh.row_values(i)[9])
                teststep.__setErrorpic__(stepsh.row_values(i)[10])
                teststepList.append(teststep)
            return teststepList
    #得到测试报告左侧菜单树
    def getTestreportTreeMenu(self,testplanrunNo):
        ReportPath=os.path.abspath("")+'\\'+testplanrunNo+'.xls'
        bk=xlrd.open_workbook(ReportPath)
        sh=bk.sheet_by_name(u"测试节点树")  
        n=sh.nrows
        #节点ID 父节点ID  名称    类型
        for j in range(1,n):
            self.subid=sh.row_values(j)[0]
            self.fatherid=sh.row_values(j)[1]
            self.name=sh.row_values(j)[2]
            self.type=sh.row_values(j)[3]
    #通过包路径获取所有的测试计划编号TestplanrunNo集合  
    def getTestplanrunNo(self):
        TestplanrunNoList=[]
        FileNames=os.listdir(os.getcwd()) 
        #使用字符串分离存储字典
        str1='.xls'
        if (len(FileNames)>4):  
            for filename in FileNames:
                if str1 in filename:
                    f=filename.split('.')
                    TestplanrunNoList.append(f(0))
                else:
                    print "this is not .xls!"
        else:
            "this is too short!"
        return TestplanrunNoList
    def __setreportname__(self,reportn):
        self.reportname1=reportn
    def __getreportname__(self):
        return self.reportname1
            
            
            
                

        