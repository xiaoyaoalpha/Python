# -*- coding:utf-8 -*-
import xlrd
import os.path
#测试启动时加载业务组件列表 解析 业务组件登记注册表.xls 到componentList，组合一个键值对的list
#打开excel文档
class TestCaseComponent:
    def __init__(self):
        self.componentList={}
        self.key=""
        self.value=""
    def __TestCaseComponent__(self):
        fdir=os.path.abspath("..")
        filedir=fdir+u"\\TestCaseClass\\业务组件登记注册表.xls"
        bk=xlrd.open_workbook(filedir)
        shlist=bk.sheets()
        for k in range(0,len(shlist)):
            sh=shlist[k]
            #获取行数
            nrows = sh.nrows
            #print cell_value
            row_list=[]
            testcasecom=TestCaseComponent()
            #获取sheet页中所有数据
            for i in range(1,nrows):
                row_data=sh.row_values(i)
                row_list.append(row_data)
            for j in range(0,nrows-1):
                key=row_list[j][0]
                value=row_list[j][1]+"->"+row_list[j][2]+"->"+row_list[j][3]
                componentList=testcasecom.componentList.fromkeys([key], value)
                self.componentList.update(componentList)
            self.__setcomponentList__(self.componentList)
    def __setcomponentList__(self,componentList):
        self.componentList=componentList
    def __getcomponentList__(self):
        return self.componentList