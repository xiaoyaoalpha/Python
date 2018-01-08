#encoding:utf-8
import os,time
from Testcore.TestCaseComponent import TestCaseComponent
from Testcore.TestCase import TestCase
from Testcore.TestStep import TestStep
from Testcore.TestSuite import TestSuite
from Testcore.TestPlan import TestPlan
from Testcore.TestGeneId import TestGeneid
from Testcore.TestWebDriver import TestWebDriver
from Testcore.TestReport import TestReport
#测试用例执行器
'''
@author: ******
@date:2016-11-06
'''
class TestRun:
    #定义测试组件列表
    testcomponentlist=TestCaseComponent().__getcomponentList__()
    #定义测试流程步骤
    #按照测试执行流程配置进行测试
    def TestRun(self):
        #获取当前时间
        t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        #对测试流程各个步骤初始化对象
        testplan=TestPlan()
        testsuite=TestSuite()
        testcase=TestCase()
        teststep=TestStep()
        #id生成执行计数器清零
        TestGeneid().resetid()
        #创建（获取）测试计划
        fpath=os.path.abspath("..")+u"\\TestPlan\\测试执行计划.xls"
        testplan.__TestPlan__(fpath)
        #获取测试计划下的测试场景列表
        testsuiteList=testplan.__gettestsuiteList__()
        #设置测试执行开始时间
        testplan.__settestplanstarttime__(t)
        #设置默认测试执行结果
        testplan.__setresult__(1)
        #第一层循环，循环执行测试计划配置的所有测试场景
        print "测试场景的个数",len(testsuiteList)
        #启动测试
        TestWebDriver().startFirefoxDriver()
        for i in range(0,len(testsuiteList)):
            #try:
            #获取测试场景
            testsuite=testsuiteList[i]
            #获取测试场景下测试用例列表
            testcaseList=testsuite.__gettestcaseList__()
            #设置测试场景开始执行时间
            t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            testsuite.__setstarttime__(t)
            #第二层循环，循环执行测试场景中配置的所有用例
            print "测试用例个数",len(testcaseList)
            for j in range(0,len(testcaseList)):
                #获取测试用例
                testcase=testcaseList[j]
                #获取测试用例下测试步骤列表
                testcaseStepList=testcase.__gettestcaseStepList__()
                #设置测试用例开始执行时间
                t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                testcase.__setstarttime__(t)
                #第三层循环，循环执行用例步骤
                print "测试步骤个数:",len(testcaseStepList)
                for k in range(0,len(testcaseStepList)):
                    #执行用例步骤
                    teststep=testcaseStepList[k]
                    if teststep.__getisrun__()==1:
                        try:
                            #设置测试步骤开始执行时间
                            t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                            teststep.__settestcasestepstarttime__(t)
                            #执行测试步骤
                            self.executeTestStep(testsuite,testcase,teststep)
                            #设置测试步骤结束执行时间
                            t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                            teststep.__settestcasestependtime__(t)
                            #设置测试步骤运行结果为"1"成功
                            teststep.__setresult__(1)
                        except Exception as e:
                            #存放异常截图的路径
                            t=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
                            pngname=teststep.__gettestcasename__()+t+".png"
                            dirpath=os.path.abspath("..")+"\\Testresult\\ErrorPic\\"
                            save_fn=dirpath+pngname
                            TestWebDriver().printScreen(save_fn)
                            #测试步骤的异常截图名称
                            teststep.__setErrorpic__(pngname)
                            print teststep.__gettestcasename__(),"-测试步骤执行异常!",('%s' % e)
                            #设置测试步骤运行结果为"0"成功
                            teststep.__setresult__(0)                            
                    else:
                        #设置测试步骤运行结果为"1"成功
                        teststep.__setresult__(0)
                        print teststep.__gettestcasename__(),"-测试步骤执行异常!"
                #设置测试用例执行结束时间
                t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                testcase.__setendtime__(t)
                #设置测试用例运行结果为"1"成功
                testcase.__setresult__(1)
            #设置测试场景执行结束时间
            t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            testsuite.__setendtime__(t)
            #设置测试场景运行结果为"1"成功
            testsuite.__setresult__(1)
#             except Exception as e:
#                 print testcase.__gettestcasename__(),"-测试用例执行失败!",('%s' % e)
#                 testsuite.__setresult__(0)
#             finally:
#                 time.sleep(2)
#                 print "测试用例执行完毕!"
        TestWebDriver().closeFirefoxDriver()
        #设置测试计划执行结束时间
        t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        testplan.__settestplanendtime__(t)
        try:
            testreport=TestReport()
            testreport.__createTestReport__(testplan)
            print "测试报告生成成功--测试报告名称:",testreport.__getreportname__()
        except Exception as e:
            print "测试报告生成失败：",('%s' % e)
    #执行测试步骤，结合业务组件中的类和方法
    def executeTestStep(self,testsuite,testcase,teststep):
        t=TestCaseComponent()
        t.__TestCaseComponent__()
        testcomponentlist=t.__getcomponentList__()
        testc=testcomponentlist.get(teststep.__getcomponentName__())
        try:
            testcomp=testc.split('->')
        except Exception as e:
            print "未获取到组件数据!",('%s' % e)
        moduleName=testcomp[0]
        className=testcomp[1]
        methodName=testcomp[2]
        inputdata=TestRun().__getDataDic(teststep.__getinputdata__())
        expectdata=TestRun().__getDataDic(teststep.__getexpectData__())
        #利用python的反射机制
        m=__import__(moduleName)
        s=getattr(m, className)
        k=getattr(s(), methodName)
        k(testsuite,testcase,inputdata,expectdata)
#         try:
#             s=getattr(m, className)
#             try:
#                 k=getattr(s(), methodName)
#                 try: 
#                     k(testsuite,testcase,inputdata,expectdata)
#                 except Exception as e:
#                     print methodName,"-method获取错误!",('%s' % e)
#             except Exception as e:
#                 print className,"-class获取错误!",('%s' % e)
#         except Exception as e:
#             print moduleName,"-module获取错误:",('%s' % e)
    #测试输入输出数据转换为字典
    def __getDataDic(self,datastr):
        datadic={}
        if datastr=="":
            return datadic=={}
        else:
            datadictmp={}
            datastrlist=datastr.split(",")
            for i in range(0,len(datastrlist)):
                datalist=datastrlist[i].split("=")
                datakey=datalist[0]
                datavalue=datalist[1]
                dic=datadictmp.fromkeys([datakey],datavalue)
                datadic.update(dic)
        return datadic  

