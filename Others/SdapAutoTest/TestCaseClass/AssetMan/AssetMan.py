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
Created on 2016.12.9

@author: ******
'''
class AssetMan:
    testcase=TestCase()
    testsuite=TestSuite()
    testplan=TestPlan()
    teststep=TestStep()
    inputdata={}
    expectData={}
    def AddAsset(self,testsuite,testcase,inputdata,expectdata):
        #------------客户信息基本信息---------------------
        assetname=inputdata.get('assetname')
        assetcode=inputdata.get('assetcode')
        assetuser=inputdata.get('assetuser')
        assetvers=inputdata.get('assetvers')
        engineRoom=inputdata.get('engineRoom')
        rackNumber=inputdata.get('rackNumber')
        rackPosition=inputdata.get('rackPosition')
        ipv4=inputdata.get('ipv4')
        mac=inputdata.get('mac')
        port=inputdata.get('port')
        #若有未退出iframe，需先退出
        TestWebDriver.driver.switch_to_default_content()
        #1.定位iframe
        TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))
        #打开添加资产对话框，并添加资产信息
        if inputdata.get("operaUnitName")==u"添加":
            #打开添加资产信息对话框
            TestWebDriver.driver.find_element_by_id("add_gridTable").click()
            #资产名称
            if assetname is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.name").send_keys(
                inputdata.get("assetname")) 
            #归属用户选择：下拉列表: 默认选择第一个选项
            TestWebDriver.driver.find_element_by_id("gridModelorgIdNam").click()
            time.sleep(2)
            e=TestWebDriver.driver.find_element_by_id("orgZtreeMenuContents_1_span")
            e.click()
            time.sleep(2)
            #使用者选择：下拉列表: 默认选择第一个选项
            TestWebDriver.driver.find_element_by_name("gridModel.owner_dropDownList").click()
            time.sleep(2)
            TestWebDriver.driver.find_element_by_xpath("//div[@rel='gridModel.owner']/ul/li[2]").click()
            time.sleep(2)
            #资产类型选择：下拉列表: 默认选择第一个选项
            TestWebDriver.driver.find_element_by_id("gridModeltypeIdNam").click()
            time.sleep(2)
            e=TestWebDriver.driver.find_element_by_id("ztreeMenuContents_2_span")
            e.click()
            time.sleep(2)
            #操作系统选择：下拉列表: 默认选择第一个选项
            TestWebDriver.driver.find_element_by_id("gridModelosIdNam").click()
            time.sleep(2)
            e=TestWebDriver.driver.find_element_by_id("gridModelosIdNam")
            e.send_keys(Keys.DOWN)
            ActionChains(TestWebDriver.driver).key_down(Keys.TAB).perform()
            time.sleep(2)
            #安全负责人信息
            if assetuser is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.riskOwnerAccount").send_keys(assetuser)
            #资产编号信息
            if assetcode is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.code").send_keys(assetcode)            
            #资产版本信息
            if assetvers is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.osVersion").send_keys(assetvers) 
            #------------客户位置信息---------------------
            #点击位置信息下拉按钮
            TestWebDriver.driver.find_element_by_xpath("//div[@id='accordion3']/div[2]").click()
            #网域名称选择，默认第一个
            TestWebDriver.driver.find_element_by_name("gridModel.domain_dropDownList").click()
            time.sleep(2)
            TestWebDriver.driver.find_element_by_xpath("//div[@rel='gridModel.domain']/ul/li[2]").click()
            time.sleep(2)
            #机房信息
            if engineRoom is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.engineRoom").send_keys(engineRoom) 
            if rackNumber is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.rackNumber").send_keys(rackNumber) 
            if rackPosition is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.rackPosition").send_keys(rackPosition) 
            #------------客户网络信息---------------------
            #点击网络信息下拉按钮
            TestWebDriver.driver.find_element_by_xpath("//div[@id='accordion3']/div[3]").click()
            #开放端口
            if port is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.port").send_keys(port) 
            #ip类型选择
            TestWebDriver.driver.find_element_by_id("gridModelassetNetPositionList[0].iptypeNam").click()
            time.sleep(2)
            e=TestWebDriver.driver.find_element_by_id("gridModelassetNetPositionList[0].iptypeNam")
            e.send_keys(Keys.DOWN)
            ActionChains(TestWebDriver.driver).key_down(Keys.TAB).perform()  
            time.sleep(2)          
            #ip
            if ipv4 is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.assetNetPositionList[0].ipv4").send_keys(ipv4) 
            #mac
            if mac is not None:
                TestWebDriver.driver.find_element_by_id("gridModel.assetNetPositionList[0].mac").send_keys(mac) 

            #保存资产信息，点击保存按钮
            TestWebDriver.driver.find_element_by_xpath('''//div[@class='ui-dialog-buttonset']/button[1]''').click()
            #资产添加确认
            #TestWebDriver.driver.find_element_by_xpath('''//span[contains(text(),u'确定')]/parent::*''').click()
            #退出iframe
            TestWebDriver.driver.switch_to_default_content()
    def EditAsset(self,testsuite,testcase,inputdata,expectdata):
        pass
    def DeleteAsset(self,testsuite,testcase,inputdata,expectdata):
        pass
    def QueryAsset(self,testsuite,testcase,inputdata,expectdata):
        #查询条件：资产编号 资产类型 IPV4 报废时间 安全负责人 使用人 
        assetcode=inputdata.get("assetcode")
        assettype=inputdata.get("assettype")
        ipv4=inputdata.get("ipv4")
        scrapDate=inputdata.get("scrapDate")
        safeowner=inputdata.get("safeowner")
        username=inputdata.get("username")
        #若有未退出iframe，需先退出
        TestWebDriver.driver.switch_to_default_content()
        #1.定位iframe
        #TestWebDriver.driver.switch_to_default_content()
        TestWebDriver.driver.switch_to_frame(TestWebDriver.driver.find_element_by_id("mainFrame"))
        #打开查询折叠框
        TestWebDriver.driver.find_element_by_xpath("//div[@class='heading']/span").click()
        time.sleep(2)
        #输入查询条件信息
        if assetcode is not None:
            try:
                js="document.getElementById('queryModel.code').value="+assetcode+";"
                TestWebDriver.driver.execute_script(js)
            except Exception as e:
                print('%s' % e)
        if assettype is not None:
            js="document.getElementById('queryModel.typeId').value="+assettype+";"
            TestWebDriver.driver.execute_script(js)
        if ipv4 is not None:
            js="document.getElementById('queryModel.assetNetPosition.ipv4').value="+ipv4+";"
            TestWebDriver.driver.execute_script(js)
        if scrapDate is not None:
            js="document.getElementById('queryModel.scrapDate').value="+scrapDate+";"
            TestWebDriver.driver.execute_script(js)
        if safeowner is not None:
            try:
                js="document.getElementById('queryModel.riskOwnerAccount').value="+safeowner+";"
                TestWebDriver.driver.execute_script(js)
            except Exception as e:
                print('%s' % e)
        if username is not None:
            js="document.getElementById('queryModel.owner').value="+username+";"
            TestWebDriver.driver.execute_script(js)
        #点击查询按钮queryButFlag
        try:
            js1="document.getElementById('queryButFlag').click();"
            TestWebDriver.driver.execute_script(js1)
            time.sleep(10)
            print "Query Succeeded!"
        except Exception as e:
            print "Query Failed!",('%s' % e)
