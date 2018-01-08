#coding:utf-8
'''
Created on 2017年1月19日

@author: *******
'''
import time
from Testcore.TestCase import TestCase
from Testcore.TestStep import TestStep
from Testcore.TestSuite import TestSuite
from Testcore.TestPlan import TestPlan
from Testcore.TestWebDriver import TestWebDriver
from selenium.webdriver.common.keys import Keys   
from selenium.webdriver.common.action_chains import ActionChains 
class DomainMan(object):
    testcase=TestCase()
    testsuite=TestSuite()
    testplan=TestPlan()
    teststep=TestStep()
    inputdata={}
    expectData={}
    def AddDomain(self,testsuite,testcase,inputdata,expectdata):
        #----------网域信息---------------
        domianname=inputdata.get("domianname")
        OfficeBui=inputdata.get("OfficeBui")
        floor=inputdata.get("floor")
        manager=inputdata.get("manager")
        telephone=inputdata.get("telephone")
        if inputdata.get("operaUnitName")==u"添加":
            #若有未退出iframe，需先退出
            TestWebDriver.driver.switch_to_default_content()
            #1.定位iframe
            TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))
            #点击添加按钮
            TestWebDriver.driver.find_element_by_css_selector("span.ui-icon.ui-icon-plus").click()
            #选择客户：第一个
            TestWebDriver.driver.find_element_by_id("gridModelorgIdNam").click()
            time.sleep(2)
            TestWebDriver.driver.find_element_by_id("treeDemo_1_span").click()
            time.sleep(2)
            #输入网域名称
            if domianname is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.name").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.name").send_keys(domianname)
            #选择省市区
            #选择省：北京市
            TestWebDriver.driver.find_element_by_id("gridModelprovinceCodeNam").click()
            time.sleep(2)
            e=TestWebDriver.driver.find_element_by_id("gridModelprovinceCodeNam")
            n=1
            for i in range(0,n):
                e.send_keys(Keys.DOWN)
                time.sleep(1)
            ActionChains(TestWebDriver.driver).key_down(Keys.TAB).perform()
            time.sleep(2)
            #选择市
            TestWebDriver.driver.find_element_by_id("gridModelcityCodeNam").click()
            time.sleep(2)
            e=TestWebDriver.driver.find_element_by_id("gridModelcityCodeNam")
            n=1
            for i in range(0,n):
                e.send_keys(Keys.DOWN)
                time.sleep(2)
            ActionChains(TestWebDriver.driver).key_down(Keys.TAB).perform()
            time.sleep(2)
            #选择区
            TestWebDriver.driver.find_element_by_id("gridModelnoteNam").click()
            time.sleep(2)
            e=TestWebDriver.driver.find_element_by_id("gridModelnoteNam")
            n=1
            for i in range(0,n):
                e.send_keys(Keys.DOWN)
                time.sleep(2)
            ActionChains(TestWebDriver.driver).key_down(Keys.TAB).perform()
            time.sleep(2)
#             except Exception as e:
#                 print "选择省市区失败！",('%s' % e)
            #输入办公楼信息
            if OfficeBui is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.building").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.building").send_keys(OfficeBui)
            #输入楼层信息
            if floor is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.floor").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.floor").send_keys(floor)
            #输入管理员信息
            if manager is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.manager").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.manager").send_keys(manager)
            #输入电话信息
            if telephone is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.tel").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.tel").send_keys(telephone)

            #点击提交按钮
            TestWebDriver.driver.find_element_by_css_selector("button[type=\"button\"]").click()
            time.sleep(2)
            #点击确认按钮
            TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
            #退出iframe
            TestWebDriver.driver.switch_to_default_content()
    def EditDomain(self,testsuite,testcase,inputdata,expectdata):
        #----------网域信息---------------
        olddomianname=inputdata.get("olddomianname")
        newdomianname=inputdata.get("newdomianname")
        OfficeBui=inputdata.get("OfficeBui")
        floor=inputdata.get("floor")
        manager=inputdata.get("manager")
        telephone=inputdata.get("telephone")
        if inputdata.get("operaUnitName")==u"修改":
            #若有未退出iframe，需先退出
            TestWebDriver.driver.switch_to_default_content()
            #定位iframe
            TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))
            
            if olddomianname is not None:
                try:
                    #选中一个网域数据
                    ele1="td[title=\""+olddomianname+"\"]"
                    TestWebDriver.driver.find_element_by_css_selector(ele1).click()
                    time.sleep(2)
                except Exception as e:
                    print "选择网域数据失败：",('%s' % e)
                #点击修改按钮
                try:
                    TestWebDriver.driver.find_element_by_css_selector("span.ui-icon.ui-icon-pencil").click()
                    time.sleep(2) 
                except Exception as e:
                    print "打开修改网域页面失败：",('%s' % e)
                #修改网域名称
                if newdomianname is not None:
                    TestWebDriver.driver.find_element_by_id("gridModel.name").clear()
                    TestWebDriver.driver.find_element_by_id("gridModel.name").send_keys(newdomianname)                
                #修改办公楼信息
                if OfficeBui is not None:
                    TestWebDriver.driver.find_element_by_id("gridModel.building").clear()
                    TestWebDriver.driver.find_element_by_id("gridModel.building").send_keys(OfficeBui)
                #修改楼层信息
                if floor is not None:
                    TestWebDriver.driver.find_element_by_id("gridModel.floor").clear()
                    TestWebDriver.driver.find_element_by_id("gridModel.floor").send_keys(floor)
                #修改管理员
                if manager is not None:
                    TestWebDriver.driver.find_element_by_id("gridModel.manager").clear()
                    TestWebDriver.driver.find_element_by_id("gridModel.manager").send_keys(manager)
                #修改联系电话
                if telephone is not None:
                    TestWebDriver.driver.find_element_by_id("gridModel.tel").clear()
                    TestWebDriver.driver.find_element_by_id("gridModel.tel").send_keys(telephone)
                #点击提交按钮
                TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
                time.sleep(2)
                #点击确定按钮
                TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
            #退出iframe
            TestWebDriver.driver.switch_to_default_content()
    def DeleteDomain(self,testsuite,testcase,inputdata,expectdata):
        if inputdata.get("operaUnitName")==u"删除":
            #若有未退出iframe，需先退出
            TestWebDriver.driver.switch_to_default_content()
            #定位iframe
            TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))
            #选中第二个网域数据
#             try:
            e=TestWebDriver.driver.find_element_by_class_name("ui-jqgrid-btable")
            e.find_element_by_xpath("//tbody/tr[3]").click()
            time.sleep(3)
            #点击删除按钮
            TestWebDriver.driver.find_element_by_css_selector("span.ui-icon.ui-icon-trash").click()
            #点击确定按钮
            TestWebDriver.driver.find_element_by_id("popup_ok").click()
#             except Exception as e:
#                 print "删除数据异常",('%s' % e)
            #退出iframe
            TestWebDriver.driver.switch_to_default_content()