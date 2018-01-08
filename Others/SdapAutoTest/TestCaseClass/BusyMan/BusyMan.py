#coding:utf-8
'''
Created on 2017年1月17日

@author: ******
'''
import time
from Testcore.TestCase import TestCase
from Testcore.TestStep import TestStep
from Testcore.TestSuite import TestSuite
from Testcore.TestPlan import TestPlan
from Testcore.TestWebDriver import TestWebDriver
from selenium.webdriver.common.keys import Keys   
from selenium.webdriver.common.action_chains import ActionChains 
class BusyMan:
    testcase=TestCase()
    testsuite=TestSuite()
    testplan=TestPlan()
    teststep=TestStep()
    inputdata={}
    expectData={}
    def AddApplication(self,testsuite,testcase,inputdata,expectdata):
        #----------添加应用信息-------------
        appName=inputdata.get("appName")
        apptypeName=inputdata.get("apptypeName")
        appdec=inputdata.get("appdec")
        if inputdata.get("operaUnitName")==u"添加":
            #若有未退出iframe，需先退出
            TestWebDriver.driver.switch_to_default_content()
            #1.定位iframe
            TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))
            #点击添加应用按钮
            TestWebDriver.driver.find_element_by_css_selector("button.cgridbtn").click()
            time.sleep(2)
            #输入应用名称
            if appName is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.appName").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.appName").send_keys(appName)
            #选择业务应用类型:OA
            TestWebDriver.driver.find_element_by_id("gridModeltypeNam").click()
#           TestWebDriver.driver.find_element_by_id("ui-id-23").click()
            time.sleep(2)
            e=TestWebDriver.driver.find_element_by_id("gridModeltypeNam")
            n=4
            for i in range(0,n):
                e.send_keys(Keys.DOWN)
                time.sleep(2)
            ActionChains(TestWebDriver.driver).key_down(Keys.TAB).perform()
            time.sleep(2)
            #输入应用描述信息
            if appdec is not None:
                TestWebDriver.driver.find_element_by_xpath("//input[@id='gridModel.appName']/parent::*/parent::*/td[3]/input").send_keys(appdec)
                time.sleep(2)
            #选择加入的资产数据：默认选择第一个资产信息
            e=TestWebDriver.driver.find_element_by_id("appJqGridLeft")
            e.find_element_by_css_selector("td.exchanger-sel > input[type=\"checkbox\"]").click()
            time.sleep(2)
            TestWebDriver.driver.find_element_by_xpath("//input[@value='>>']").click()
            TestWebDriver.driver.find_element_by_id("assetWeight1").clear()
            TestWebDriver.driver.find_element_by_id("assetWeight1").send_keys("0.2")
            time.sleep(2)
            #点击提交按钮
            TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
            time.sleep(2)
            #点击确定按钮
            TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
            #--------------业务系统-------------
            busyname=inputdata.get("busyname")
            busydec=inputdata.get("busydec")
            #点击添加业务系统按钮
            TestWebDriver.driver.find_element_by_xpath("//button[@onclick=\"systemDlgFunc('add',-1)\"]").click()
            time.sleep(2)
            #业务系统名称
            if busyname is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.name").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.name").send_keys(busyname)
            time.sleep(2)
            #选择客户:默认选择第一个客户
            TestWebDriver.driver.find_element_by_id("gridModelorgIdNam").click()
            e1=TestWebDriver.driver.find_element_by_id("treeDemo_1_span")
            e1.click()
            time.sleep(2)
            #选择使用人：默认选择系统管理员
            TestWebDriver.driver.find_element_by_id("gridModelmasterNam").click()
            e=TestWebDriver.driver.find_element_by_id("gridModelmasterNam")
            n=1
            for i in range(0,n):
                e.send_keys(Keys.DOWN)
                time.sleep(2)
            ActionChains(TestWebDriver.driver).key_down(Keys.TAB).perform()
            time.sleep(2)
            #输入描述信息
            if busydec is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.info").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.info").send_keys(busydec)
            #选择应用，输入权重
            TestWebDriver.driver.find_element_by_css_selector("td.exchanger-sel > input[type=\"checkbox\"]").click()
            TestWebDriver.driver.find_element_by_xpath("//input[@value='>>']").click()
            TestWebDriver.driver.find_element_by_id("weight1").clear()
            TestWebDriver.driver.find_element_by_id("weight1").send_keys("0.2")
            time.sleep(2)
            #点击提交按钮
            TestWebDriver.driver.find_element_by_xpath("//button[@type='button']").click()
            time.sleep(2)
            #点击确定按钮
            TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
            time.sleep(2)
            #退出iframe
            TestWebDriver.driver.switch_to_default_content()
    def EditApplication(self,testsuite,testcase,inputdata,expectdata):
        #----------修改业务系统信息-------------
        oldbusyname=inputdata.get("oldbusyname")
        newbusyname=inputdata.get("newbusyname")
        busydec=inputdata.get("busydec")
        if inputdata.get("operaUnitName")==u"修改":
            #若有未退出iframe，需先退出
            TestWebDriver.driver.switch_to_default_content()
            #1.定位iframe
            TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))
            #选中业务系统
            try:
                ele1="td[title=\""+oldbusyname+"\"] > span.cell-wrapper"
                e=TestWebDriver.driver.find_element_by_css_selector(ele1)
                e.click()
            except Exception as e:
                print "未选中数据",('%s' % e)
            #点击修改按钮
            TestWebDriver.driver.find_element_by_xpath("//button[@onclick='editFunc()']").click()
            time.sleep(2)
            #修改业务系统名称
            if newbusyname is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.name").clear()
                time.sleep(2)
                TestWebDriver.driver.find_element_by_id("gridModel.name").send_keys(newbusyname)
                time.sleep(2) 
            #选择第一个应用
            try:
#                 TestWebDriver.driver.find_element_by_css_selector("td.exchanger-sel > input[type=\"checkbox\"]").click()
#                 time.sleep(2)
#                 #点击'>>'移到应用列
#                 TestWebDriver.driver.find_element_by_xpath("//input[@value='>>']").click()
                #应用列为第二个修改权重
                TestWebDriver.driver.find_element_by_id("weight2").clear()
                TestWebDriver.driver.find_element_by_id("weight2").send_keys("0.1")
            except Exception as e:
                print "未选中应用数据",('%s' % e)
            #点击提交按钮
            TestWebDriver.driver.find_element_by_xpath("//button[@type='button']").click()
            time.sleep(2)
            #点击确定按钮
            TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
            #----------修改应用信息-------------
            oldappName=inputdata.get("oldappName")
            newappName=inputdata.get("newappName")
            apptypeName=inputdata.get("apptypeName")
            appdec=inputdata.get("appdec")
            #选中业务系统下的应用：oldappName
            if oldappName is not None:
                ele2="td[title=\""+oldappName+"\"] > span.cell-wrapper"
                TestWebDriver.driver.find_element_by_css_selector(ele2).click()
            #点击修改按钮
            TestWebDriver.driver.find_element_by_xpath("//button[@onclick='editFunc()']").click()
            time.sleep(2)
            #修改业务应用名称
            if newappName is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.appName").clear()
                time.sleep(2)
                TestWebDriver.driver.find_element_by_id("gridModel.appName").send_keys(newappName)
                time.sleep(2)
            #修改业务应用类型
            try:
                TestWebDriver.driver.find_element_by_id("gridModeltypeNam").click()
                time.sleep(2)
                n=4
                for i in range(0,n):
                    e.send_keys(Keys.DOWN)
                    time.sleep(2)
                ActionChains(TestWebDriver.driver).key_down(Keys.TAB).perform()
                time.sleep(2)
            except Exception as e:
                print "修改业务应用类型失败",('%s' % e)
            #修改第个应用的权重
            TestWebDriver.driver.find_element_by_id("assetWeight3").clear()
            TestWebDriver.driver.find_element_by_id("assetWeight3").send_keys("0.3")
            #点击提交按钮
            TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
            time.sleep(2)
            #点击确定按钮
            TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
            #退出iframe
            TestWebDriver.driver.switch_to_default_content()
    def DEleteApplication(self,testsuite,testcase,inputdata,expectdata):
        pass