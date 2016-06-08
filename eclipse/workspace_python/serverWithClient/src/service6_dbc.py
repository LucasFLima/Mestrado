from dbcCondition import DbcCheckService, CheckType, DbcCheckBasic, DbcConditionType

        
class Service6Dbc(object): 
 
    def get_PreconditionList (self):

        rtn = []
        rtn.append(DbcCheckBasic('testId', '30', 430, CheckType.argument, '==', DbcConditionType.PreCondition))
        rtn.append(DbcCheckService('http://localhost:8081/store/{testId}?site=site','200', 501, CheckType.argument, '<>', DbcConditionType.PreCondition))
        
        return rtn
    
    
    def get_PostconditionList (self):

        rtn = []
        rtn.append(DbcCheckBasic('testMessage', 'fail', 460, CheckType.responseBody, '==', DbcConditionType.PostCondition))
       
        return rtn    
    
    def post_PreconditionList (self):

        rtn = []
        rtn.append(DbcCheckBasic('testId', '20', 430, CheckType.requestBody, '==', DbcConditionType.PreCondition))
        rtn.append(DbcCheckService('http://localhost:8081/test/{testId}','200',501,CheckType.requestBody, '<>', DbcConditionType.PreCondition))
        
        return rtn