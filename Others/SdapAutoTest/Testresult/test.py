# -*- coding: utf-8 -*-
#
# author: oldj <oldj.wu@gmail.com>
#
import os,time
from selenium  import webdriver
driver=webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.baidu.com")
dd=os.path.abspath("..")+"\\Testresult\\ErrorPic\\"+"sds.png"
print dd
driver.save_screenshot(dd)
time.sleep(10)
driver.quit()