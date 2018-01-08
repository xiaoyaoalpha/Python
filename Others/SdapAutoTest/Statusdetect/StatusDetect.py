#-*- coding: UTF-8 -*-
from Testcore.GetMsqlCon import GetMsqlCon
getc=GetMsqlCon()
db=getc.getCon()
cursor=db.cursor()
sql="select * from node"
cursor.execute(sql)
node_list=cursor.fetchall()
#console注册成功
for i in range(len(node_list)):
    if  node_list[i][6]==u"管理平台":
        print  node_list[i][6]," register successed!","ip:",node_list[i][8]
        break
    elif i>=len(node_list)-1:
        print "管理平台  register failed!"
#dispatcher注册成功
i=0
for i in range(len(node_list)):
    if node_list[i][6]==u"系统分发器":
        print node_list[i][6]," register successed!"
        break
    elif i>=len(node_list)-1:
        print "系统分发器  register failed!"
#前置机注册成功
i=0
for i in range(len(node_list)):
    if node_list[i][6]==u"前置机":
        print node_list[i][6]," register successed!"
        break
    elif i>=len(node_list)-1:
        print "前置机  register failed!"
#数据预处理注册成功
i=0
for i in range(len(node_list)):
    if node_list[i][6]==u"数据预处理":
        print node_list[i][6]," register successed!"
        break
    elif i>=len(node_list)-1:
        print "数据预处理  register failed!"
#告警引擎注册成功
i=0
for i in range(len(node_list)):
    if node_list[i][6]==u"告警引擎":
        print node_list[i][6]," register successed!"
        break
    elif i>=len(node_list)-1:
        print "告警引擎  register failed!"
#情报分析引擎注册成功
i=0
for i in range(len(node_list)):
    if node_list[i][6]==u"情报分析引擎":
        print node_list[i][6]," register successed!"
        break
    elif i>=len(node_list)-1:
        print "情报分析引擎  register failed!"
#分析引擎注册成功
i=0
for i in range(len(node_list)):
    if node_list[i][6]==u"分析引擎":
        print node_list[i][6]," register successed!"
        break
    elif i>=len(node_list)-1:
        print "分析引擎  register failed!"
#代理中心注册成功
i=0
for i in range(len(node_list)):
    if node_list[i][6]==u"代理中心":
        print node_list[i][6]," register successed!"
        break
    elif i>=len(node_list)-1:
        print "代理中心  register failed!"
#收集器注册成功
i=0
for i in range(len(node_list)):
    if node_list[i][6]==u"收集器":
        print node_list[i][6]," register successed!"
        break
    elif i>=len(node_list)-1:
        print "收集器  register failed!"
#统计传感器总数
i=0
j=0
for i in range(len(node_list)):
    if  node_list[i][6]==u"传感器":
        j+=1
        continue
if  j==0:
    print "传感器数量为零!"
else:
    print "传感器的总数为",j