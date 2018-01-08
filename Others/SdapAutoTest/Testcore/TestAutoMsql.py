#encding:utf-8
import GetMsqlCon
getcon=GetMsqlCon.GetMsqlCon()
db=getcon.getCon()
cursor=db.cursor()