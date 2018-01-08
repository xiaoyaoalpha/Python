#encoding:utf-8
from Testcore.TestGeneId import TestGeneid
class TestStep:
    #测试步骤id
    id=""
    #所属测试用例ID
    testcaseId=""
    #测试用例名称
    testcasename=""
    #测试用例描述
    dec=""
    #作者
    createuser=""
    #创建时间
    createtime=""
    #测试用例步骤名称
    testcasestep=""
    #调用业务组件名称
    componentName=""
    #输入数据
    inputdata=""
    #预期结果
    expectData=""
    #是否执行
    isrun=""
    #执行开始时间
    starttime=""
    #执行结束时间
    endtime=""
    #执行结果
    result=0
    #执行报错信息
    errorMessage=None
    #错误图片日志
    errorpic=None
    #定义所有属性的获取设置方法
    def __setId__(self,id):
        self.id=id
    def __getId__(self):
        return self.id
    def __settestcaseId__(self,testcaseId):
        self.testcaseId=testcaseId
    def __gettestcaseId__(self):
        return self.testcaseId
    def __settestcasename__(self,testcasename):
        self.testcasename=testcasename
    def __gettestcasename__(self):
        return self.testcasename
    def __settestcasestep__(self,testcasestep):
        self.testcasestep=testcasestep
    def __gettestcasestep__(self):
        return self.testcasestep
    def __setcomponentName__(self,componentName):
        self.componentName=componentName
    def __getcomponentName__(self):
        return self.componentName
    def __setinputdata__(self,inputdata):
        self.inputdata=inputdata
    def __getinputdata__(self):
        return self.inputdata
    def __setexpectData__(self,expectData):
        self.expectData=expectData
    def __getexpectData__(self):
        return self.expectData
    def __setisrun__(self,isrun):
        self.isrun=isrun
    def __getisrun__(self):
        return self.isrun
    def __settestcasestepstarttime__(self,starttime):
        self.starttime=starttime
    def __gettestcasestepstarttime__(self):
        return self.starttime
    def __settestcasestependtime__(self,starttime):
        self.starttime=starttime
    def __gettestcasestependtime__(self):
        return self.starttime
    def __setresult__(self,result):
        self.result=result
    def __getresult__(self):
        return self.result
    def __setErrorMessage__(self,errorMessage):
        self.errorMessage=errorMessage
    def __getErrorMessage__(self):
        return self.errorMessage
    def __setErrorpic__(self,errorpic):
        self.errorpic=errorpic
    def __getErrorpic__(self):
        return self.errorpic
        