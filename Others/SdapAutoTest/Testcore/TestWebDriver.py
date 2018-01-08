#encoding:utf-8
import time
from selenium import webdriver
from Testcore.GetTestConfig import GetTestConfig
class TestWebDriver:
    getconf=GetTestConfig()
    url=getconf.geturl()
    driver=webdriver.Firefox()
    driver.maximize_window()
    def startFirefoxDriver(self):
        try:
            self.driver.get(self.url)
            time.sleep(3)
        except Exception:
            print "webdriver start Error!"
        #获取截图
    def printScreen(self,save_fn):
        self.driver.execute_script("""
        (function () {
          var y = 0;
          var step = 100;
          window.scroll(0, 0);
     
          function f() {
            if (y < document.body.scrollHeight) {
              y += step;
              window.scroll(0, y);
              setTimeout(f, 50);
            } else {
              window.scroll(0, 0);
              document.title += "scroll-done";
            }
          }
     
          setTimeout(f, 1000);
        })();
      """)
 
        for i in xrange(30):
            if "scroll-done" in self.driver.title:
                break
            time.sleep(1)
        self.driver.save_screenshot(save_fn)
    def closeFirefoxDriver(self):        
        try:
            self.driver.quit()
        except Exception:
            print "webdriver end Error!"