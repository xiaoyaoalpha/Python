#encoding:utf-8
import time
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Firefox()
driver.get("http://192.168.0.30:8089/sdap")
time.sleep(10)
driver.find_element_by_id("userName").send_keys("root")
driver.find_element_by_id("password").send_keys("111111")
driver.find_element_by_id("loginBtn").click()
time.sleep(10)
elementlists=driver.find_elements_by_xpath("//div[@class='shortcuts']/ul/li/a/span[1]")
for element in elementlists:
    if element.text==u'管理':
        if element.is_displayed():
            element.click()
            print "一级菜单打开成功：",element.text
            elementlists1=driver.find_elements_by_xpath("//div[@class='mainnav']/ul/li/a")
            for element1 in elementlists1:
                if element1.text==u'客户信息管理':
                    if element1.is_displayed():
                        element1.click()
                        print "二级菜单打开成功：",element1.text
                        elementlists2=driver.find_elements_by_xpath("//ul[@class='sub']/li/a")
                        for element2 in elementlists2:
                            if element2.text==u'客户管理':
                                if element2.is_displayed():
                                    element2.click()
                                    print "三级菜单打开成功：",element2.text
                                    break
                                else:
                                    print "三级菜单打开失败：",element2.text
                                    break  
                    else:
                        print "二级菜单打开失败：",element1.text
        else:
            print "一级菜单打开失败：",element.text
driver.switch_to_frame(driver.find_element_by_id("mainFrame"))
time.sleep(2)
driver.find_element_by_id("add_gridTable").click()
driver.find_element_by_id("gridModel.name").send_keys("kehu1")
#下拉选框---字典列表难点
menu=driver.find_element_by_id("gridModelprovinceNam")
ActionChains(driver).click(menu).perform()
ActionChains(driver).move_by_offset(0,100).perform()
ActionChains(driver).click().perform()





