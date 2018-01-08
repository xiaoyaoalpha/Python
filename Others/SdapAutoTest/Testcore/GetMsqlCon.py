# -*- coding:utf-8 -*-
import MySQLdb
import GetTestConfig
getconf=GetTestConfig.GetTestConfig()
class GetMsqlCon:
    def getCon(self):
        self.Host1=str(getconf.getdb()[0])
        self.port1=str(getconf.getdb()[1])
        self.user1=str(getconf.getdb()[2])
        self.passwd1=str(getconf.getdb()[3])
        self.db1=str(getconf.getdb()[4])
        try:
            db=MySQLdb.connect(host=self.Host1,user=self.user1,passwd=self.passwd1,db=self.db1,charset='utf8')
        except TypeError:
            print "error"
        return db
    def closeCon(self):
        try:
            self.db.close()
        except TypeError:
            print "error"