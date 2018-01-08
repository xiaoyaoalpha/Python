#encoding:utf-8
import time
from Testcore.TestCase import TestCase
from Testcore.TestStep import TestStep
from Testcore.TestSuite import TestSuite
from Testcore.TestPlan import TestPlan
from Testcore.TestWebDriver import TestWebDriver
from django.template.defaultfilters import length
'''
Created on 2016年12月7日

@author: *******
'''
class SystemMange:
    testcase=TestCase()
    testsuite=TestSuite()
    testplan=TestPlan()
    teststep=TestStep()
    inputdata={}
    expectData={}
    #SDAP登陆系统ccwj@sdzc2016!
    def login(self,testsuite,testcase,inputdata,expectData):
        #登陆用户名
        username=inputdata.get("username")
        #登陆密码
        password=inputdata.get("password")
        #定位username元素，输入数据
        TestWebDriver.driver.find_element_by_id("userName").clear()
        if username is not None:
            TestWebDriver.driver.find_element_by_id("userName").send_keys(username)
        else:
            print "username数据为空"
        #定位password元素，输入数据
        TestWebDriver.driver.find_element_by_id("password").clear()
        if password is not None:
            TestWebDriver.driver.find_element_by_id("password").send_keys(password)
        else:
            print "password数据为空"
        #定位登陆按钮元素，点击登陆按钮
        TestWebDriver.driver.find_element_by_id("loginBtn").click()
        time.sleep(2)
        TestWebDriver.driver.find_element_by_id("platformDisp").click()
        time.sleep(5)
        TestWebDriver.driver.find_element_by_id("cd-nav-trigger").click()
        time.sleep(2)
        t=TestWebDriver.driver.find_element_by_xpath("//span[@class='txt']")
        #断言判断：是否登录成功
        assert t.text==username
        time.sleep(2)
        TestWebDriver.driver.find_element_by_id("cd-nav-trigger").click()
#         TestWebDriver.driver.find_element_by_id("cancelButFlag").click()
#         time.sleep(5)
    def logout(self,testsuite,testcase,inputdata,expectData):
        #定位注销导航栏
        TestWebDriver.driver.switch_to_default_content()
        time.sleep(2)
        TestWebDriver.driver.find_element_by_id("cd-nav-trigger").click()
        time.sleep(2)
        TestWebDriver.driver.find_element_by_link_text(u"退出").click()
        time.sleep(2)
        print "logout sucess!"
        