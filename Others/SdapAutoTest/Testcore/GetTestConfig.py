#encoding:utf-8
import ConfigParser,os
cf=ConfigParser.ConfigParser()
confile=os.path.abspath("..")+"\\Testcore\\baseconfig.ini"
cf.read(confile)
class GetTestConfig:
    def geturl(self):
        self.url=cf.get("url","TEST_ENV_URL")
        return self.url
    def getdb(self):
        self.host=cf.get("db", "DB_HOST")
        self.port=cf.get("db", "DB_PORT")
        self.user=cf.get("db", "DB_USERNAME")
        self.passwd=cf.get("db", "DB_PASSWORD")
        self.db=cf.get("db", "DB_BASEDATA")
        return self.host,self.port,self.user,self.passwd,self.db
    
        