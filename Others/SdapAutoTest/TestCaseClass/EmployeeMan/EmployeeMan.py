#coding:utf-8
'''
Created on 2017年1月20日

@author: *******
'''
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from Testcore.TestCase import TestCase
from Testcore.TestStep import TestStep
from Testcore.TestSuite import TestSuite
from Testcore.TestPlan import TestPlan
from Testcore.TestWebDriver import TestWebDriver

class EmployeeMan(object):
    testcase=TestCase()
    testsuite=TestSuite()
    testplan=TestPlan()
    teststep=TestStep()
    inputdata={}
    expectData={}
    def AddEmployee(self,testsuite,testcase,inputdata,expectdata):
        #----------员工信息---------------
        Employeename=inputdata.get("Employeename")
        Employeenum=inputdata.get("Employeenum")
        Employeepost=inputdata.get("Employeepost")
        ipv4=inputdata.get("ipv4")
        mac=inputdata.get("mac")
        phone=inputdata.get("phone")
        telephone=inputdata.get("telephone")
        mail=inputdata.get("mail")
        if inputdata.get("operaUnitName")==u"添加":
            #若有未退出iframe，需先退出
            TestWebDriver.driver.switch_to_default_content()
            #定位iframe
            TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))
            try:
                #点击添加按钮
                TestWebDriver.driver.find_element_by_css_selector("span.ui-icon.ui-icon-plus").click()
            except Exception as e:
                print "打开添加员工对话框失败",('%s' % e)
            #选择所属组织--第一个组织
            TestWebDriver.driver.find_element_by_id("gridModelorgIdNam").click()
            time.sleep(2)
            TestWebDriver.driver.find_element_by_id("treeDemo_1_span").click()
            time.sleep(1)
            #选择所属部门
            TestWebDriver.driver.find_element_by_id("gridModeldepartmentNam").click()
            time.sleep(2)
            e=TestWebDriver.driver.find_element_by_id("gridModeldepartmentNam")
            n=2
            for i in range(0,n):
                e.send_keys(Keys.DOWN)
                time.sleep(1)
            ActionChains(TestWebDriver.driver).key_down(Keys.TAB).perform()
            time.sleep(1)
            #输入员工姓名
            if Employeename is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.name").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.name").send_keys(Employeename)
                time.sleep(1)
            #输入员工编号
            if Employeenum is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.empno").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.empno").send_keys(Employeenum)
                time.sleep(1)
            #输入岗位
            if Employeepost is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.post").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.post").send_keys(Employeepost)
                time.sleep(1)
            #输入ipv4
            if ipv4 is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.ipv4").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.ipv4").send_keys(ipv4)
                time.sleep(1)
            #输入mac
            if mac is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.mac").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.mac").send_keys(mac)
                time.sleep(1)
            #输入邮箱地址
            if mail is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.email").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.email").send_keys(mail)
                time.sleep(1)
            #输入手机号
            if phone is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.phone").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.phone").send_keys(phone)
                time.sleep(1)
            #输入固定电话
            if telephone is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.tel").clear()
                TestWebDriver.driver.find_element_by_id("gridModel.tel").send_keys(telephone)
                time.sleep(1)
            #点击提交按钮
            TestWebDriver.driver.find_element_by_css_selector("button[type=\"button\"]").click()
            time.sleep(2)
            #点击确定按钮
            TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
            #退出iframe
            TestWebDriver.driver.switch_to_default_content()
    def EditEmployee(self,testsuite,testcase,inputdata,expectdata):
        #----------员工信息---------------
        Employeename=inputdata.get("Employeename")
        Employeenum=inputdata.get("Employeenum")
        Employeepost=inputdata.get("Employeepost")
        ipv4=inputdata.get("ipv4")
        mac=inputdata.get("mac")
        phone=inputdata.get("phone")
        telephone=inputdata.get("telephone")
        mail=inputdata.get("mail")
        if inputdata.get("operaUnitName")==u"修改":
            #若有未退出iframe，需先退出
            TestWebDriver.driver.switch_to_default_content()
            #定位iframe
            TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))            
            try:
                #选中第2个数据
                e=TestWebDriver.driver.find_element_by_class_name("ui-jqgrid-btable")
                e.find_element_by_xpath("//tbody/tr[2]").click()
                time.sleep(3)
                #点击修改按钮
                TestWebDriver.driver.find_element_by_css_selector("span.ui-icon.ui-icon-pencil").click()
                time.sleep(2)
                #修改员工姓名
                if Employeename is not None:
                    TestWebDriver.driver.find_element_by_id("gridModel.name").clear()
                    TestWebDriver.driver.find_element_by_id("gridModel.name").send_keys(Employeename)
                    time.sleep(1)
                #修改员工岗位职称
                if Employeepost is not None:
                    TestWebDriver.driver.find_element_by_id("gridModel.post").clear()
                    TestWebDriver.driver.find_element_by_id("gridModel.post").send_keys(Employeepost)
                    time.sleep(1)
                #修改员工号
                if Employeenum is not None:
                    TestWebDriver.driver.find_element_by_id("gridModel.empno").clear()
                    TestWebDriver.driver.find_element_by_id("gridModel.empno").send_keys(Employeenum)
                    time.sleep(1)
                #点击提交按钮
                TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
                time.sleep(2)
                #点击确定按钮
                TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
            except Exception as e:
                print "修改失败",('%s' % e)
            #退出iframe
            TestWebDriver.driver.switch_to_default_content()
    def QueryEmployee(self,testsuite,testcase,inputdata,expectdata):
        #----------查询条件---------------
        Employeename=inputdata.get("Employeename")
        Employeenum=inputdata.get("Employeenum")
        Employeepost=inputdata.get("Employeepost")
        ipv4=inputdata.get("ipv4")
        mac=inputdata.get("mac")
        phone=inputdata.get("phone")
        telephone=inputdata.get("telephone")
        mail=inputdata.get("mail")
        if inputdata.get("operaUnitName")==u"查询":
            #若有未退出iframe，需先退出
            TestWebDriver.driver.switch_to_default_content()
            #定位iframe
            TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))            
            #选择查询条件：所属组织
            try:
                TestWebDriver.driver.find_element_by_id("queryModelorgIdNam").click()
                time.sleep(2)
                TestWebDriver.driver.find_element_by_id("treeDemoQuery_1_span").click()
                time.sleep(1)
            except Exception as e:
                print "所属组织选择失败",('%s' % e)
            #输入查询条件：姓名
            if Employeename is not None:
                TestWebDriver.driver.find_element_by_id("queryModel.name").clear()
                TestWebDriver.driver.find_element_by_id("queryModel.name").send_keys(Employeename)
                time.sleep(1)
            #输入查询条件：员工号
            if Employeenum is not None:
                TestWebDriver.driver.find_element_by_id("queryModel.empno").clear()
                TestWebDriver.driver.find_element_by_id("queryModel.empno").send_keys(Employeenum)
                time.sleep(1)
            #点击查询按钮
            TestWebDriver.driver.find_element_by_id("queryButFlag").click()
            #退出iframe
            TestWebDriver.driver.switch_to_default_content()    
    def DeteleEmployee(self,testsuite,testcase,inputdata,expectdata):
        Employeename=inputdata.get("Employeename")
        if inputdata.get("operaUnitName")==u"删除":
            #若有未退出iframe，需先退出
            TestWebDriver.driver.switch_to_default_content()
            #定位iframe
            TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))
            #选中员工数据
            ele1="td[title=\""+Employeename+"\"]"
            TestWebDriver.driver.find_element_by_css_selector(ele1).click()
            time.sleep(2)
            #点击删除按钮
            TestWebDriver.driver.find_element_by_css_selector("span.ui-icon.ui-icon-trash").click()
            time.sleep(2)
            #点击确定按钮
            TestWebDriver.driver.find_element_by_id("popup_ok").click()
        #退出iframe
            TestWebDriver.driver.switch_to_default_content()