#encoding:utf-8
import time
from Testcore.TestCase import TestCase
from Testcore.TestStep import TestStep
from Testcore.TestSuite import TestSuite
from Testcore.TestPlan import TestPlan
from Testcore.TestWebDriver import TestWebDriver
'''
Created on 2016.12.9

@author: Administrator
'''
class CommonComponent:
    testcase=TestCase()
    testsuite=TestSuite()
    testplan=TestPlan()
    teststep=TestStep()
    inputdata={}
    expectData={}
    #打开菜单页面--menuName=管理->客户信息管理->客户管理
    def openMainMenu(self,testsuite,testcase,inputdata,expectData):
        menu=inputdata.get("menuName").split("->")
        firstmenul=menu[0]
        elementlists=TestWebDriver.driver.find_elements_by_xpath("//div[@id='sidebar']/div/ul/li/a/span")
        for element in elementlists:
            if element.text==firstmenul:
                element.click()
                print "一级菜单打开成功：",element.text
        for i in range(1,len(menu)):
            TestWebDriver.driver.find_element_by_link_text(menu[i]).click()
            print "菜单打开成功：",menu[i]
            time.sleep(2)
    #打开操作单元--添加、修改对话框,删除
    def openOperaUnit(self,testsuite,testcase,inputdata,expectData):
        #1.定位iframe
        TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))
        #打开添加或修改对话框
        if inputdata.get("operaUnitName")=="添加":
            TestWebDriver.driver.find_element_by_id("add_gridTable").click()          
        elif inputdata.get("operaUnitName")=="修改":
            TestWebDriver.driver.find_element_by_id("edit_gridTable").click()
        elif inputdata.get("operaUnitName")=="删除":
            TestWebDriver.driver.find_element_by_id("edit_gridTable").click()
        
        
        
            