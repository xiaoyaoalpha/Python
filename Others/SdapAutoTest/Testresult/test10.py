#encoding:utf-8
import os,xlrd,time
from Testcore.TestCaseComponent import TestCaseComponent
from Testcore.TestCase import TestCase
from Testcore.TestSuite import TestSuite
from Testcore.TestPlan import TestPlan
from Testcore.TestStep import TestStep

fpath=os.path.abspath("..")+u"\Testplan\测试执行计划.xls"
testplan=TestPlan()
testsuite=TestSuite()
testplan.__TestPlan__(fpath)
testsuiteList=testplan.__gettestsuiteList__()
testsuite=testsuiteList[0]
testcaseList=testsuite.__gettestcaseList__()
testcase=testcaseList[0]
testcaseStepList=testcase.__gettestcaseStepList__()
testcasestep=testcaseStepList[0]
testcomponentlist=TestCaseComponent().__getcomponentList__()
t=TestCaseComponent()
t.__TestCaseComponent__()
testcomponentlist=t.__getcomponentList__()
print testcasestep.__getcomponentName__()
print testcomponentlist.get(testcasestep.__getcomponentName__())
str1=testcomponentlist.get(testcasestep.__getcomponentName__()).split('->')
moduleName=str1[0]
className=str1[1]
methodName=str1[2]
#利用python的反射机制
m=__import__(moduleName)
s=getattr(m, className) 
k=getattr(s(), methodName) 
k()

