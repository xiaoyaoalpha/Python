#encoding:utf-8
import time
from selenium.webdriver.common.keys import Keys   
#要使用鼠标操作，首先需要引入ActionChains包    
from selenium.webdriver.common.action_chains import ActionChains  
from Testcore.TestCase import TestCase
from Testcore.TestStep import TestStep
from Testcore.TestSuite import TestSuite
from Testcore.TestPlan import TestPlan
from Testcore.TestWebDriver import TestWebDriver
'''
Created on 2016-12-09

@author: *******
'''
class CustomMan:
    testcase=TestCase()
    testsuite=TestSuite()
    testplan=TestPlan()
    teststep=TestStep()
    inputdata={}
    expectData={}
    def AddCustom(self,testsuite,testcase,inputdata,expectdata):
        #客户信息基本信息
        clientname=inputdata.get('clientname')
        clientn=inputdata.get('clientn')
        province=inputdata.get('province')
        city=inputdata.get('city')
        district=inputdata.get('district')
        clientdec=inputdata.get('clientdec')
        #若有未退出iframe，需先退出
        TestWebDriver.driver.switch_to_default_content()
        #1.定位iframe
        TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))
        #打开添加客户对话框，并添加客户信息
        if inputdata.get("operaUnitName")==u"添加":
            #打开添加客户信息对话框
            TestWebDriver.driver.find_element_by_id("add_gridTable").click()
            #客户名称
            if clientname is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.name").send_keys(
                inputdata.get("clientname")) 
            #客户简称     
            if clientn is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.shortname").send_keys(
                inputdata.get("clientn"))
            #省份选择：下拉列表: 默认选择第一个选项
            TestWebDriver.driver.find_element_by_id("gridModelprovinceNam").click()
            time.sleep(2)
            e=TestWebDriver.driver.find_element_by_id("gridModelprovinceNam")
            e.send_keys(Keys.DOWN)
            ActionChains(TestWebDriver.driver).key_down(Keys.TAB).perform()
            #市选择：下拉列表: 默认选择第一个选项
            TestWebDriver.driver.find_element_by_id("gridModelcityNam").click()
            time.sleep(2)
            e=TestWebDriver.driver.find_element_by_id("gridModelcityNam")
            e.send_keys(Keys.DOWN)
            ActionChains(TestWebDriver.driver).key_down(Keys.TAB).perform()
            #区选择：下拉列表: 默认选择第一个选项
            TestWebDriver.driver.find_element_by_id("gridModelzoneNam").click()
            time.sleep(2)
            e=TestWebDriver.driver.find_element_by_id("gridModelzoneNam")
            e.send_keys(Keys.DOWN)
            ActionChains(TestWebDriver.driver).key_down(Keys.TAB).perform()
            #描述信息
            if clientdec is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.descript").send_keys(clientdec)
            #保存客户信息，点击保存按钮
            TestWebDriver.driver.find_element_by_xpath('''//div[@class='ui-dialog-buttonset']/button[1
    ]''').click()
            #点击确认按钮
            TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
            #断言判断：是否添加成功
            fe=TestWebDriver.driver.find_element_by_id("gridTable")
            els=fe.find_elements_by_tag_name("span")
            flag=False
            for e in els:
                if e.text==clientname:
                    flag=True
                    break
            assert flag
            #退出iframe
            TestWebDriver.driver.switch_to_default_content()
    def EditCustom(self,testsuite,testcase,inputdata,expectdata):
        #客户信息
        clientname=inputdata.get('clientname')
        clientn=inputdata.get('clientn')
        clientdec=inputdata.get('clientdec')
        #若有未退出iframe，需先退出
        TestWebDriver.driver.switch_to_default_content()
        #1.定位iframe
        TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))
        #打开添加客户对话框，并添加客户信息
        if inputdata.get("operaUnitName")==u"编辑":
            #选中客户信息列表中第一个客户信息
            el1=TestWebDriver.driver.find_element_by_id("gridTable")
            el1.find_element_by_xpath("//tbody/tr[2]/td[2]").click()
            #点击编辑按钮,打开编辑客户信息对话框
            TestWebDriver.driver.find_element_by_id("edit_gridTable").click()
            time.sleep(2)
            #修改客户名称
            if clientname is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.name").clear()
                time.sleep(2)
                TestWebDriver.driver.find_element_by_id("gridModel.name").send_keys(inputdata.get("clientname"))
                time.sleep(2)
            #保存客户信息，点击更新按钮
            TestWebDriver.driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[2]").click()    
            #点击确认按钮
            TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
            #断言判断，编辑客户名称是否成功
            fe=TestWebDriver.driver.find_element_by_id("gridTable")
            els=fe.find_elements_by_tag_name("span")
            flag=False
            for e in els:
                if e.text==clientname:
                    flag=True
                    break
            assert flag
            #退出iframe
            TestWebDriver.driver.switch_to_default_content()
    def DeleteCustom(self,testsuite,testcase,inputdata,expectdata):
        clientname=inputdata.get('clientname')
        #若有未退出iframe，需先退出
        TestWebDriver.driver.switch_to_default_content()
        #1.定位iframe
        TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))
        #打开添加客户对话框，并添加客户信息
        if inputdata.get("operaUnitName")==u"删除":
            #选中客户信息列表中客户信息
            try:
                TestWebDriver.driver.find_element_by_css_selector("td[title=\""+clientname+"\"]").click()
            except Exception as e:
                print "未选中数据：",('%s' % e)
            #点击删除按钮,弹出删除客户信息提示框
            TestWebDriver.driver.find_element_by_id("del_gridTable").click()
            time.sleep(5)
            #退出iframe
            TestWebDriver.driver.switch_to_default_content()
            TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))
            #点击确定删除按钮
            TestWebDriver.driver.find_element_by_xpath("//div[@id='popup_panel']/input[1]").click()
            time.sleep(5)
            #点击确认按钮
            TestWebDriver.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
            #退出iframe
            TestWebDriver.driver.switch_to_default_content()