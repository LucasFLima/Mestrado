from dbcCondition import DbcCheckBasic, DbcCheckService

        
class Service6Dbc(object): 
 
    def preConditionList (self, args):

        rtn = []
        
        pre = DbcCheckBasic('testId', '30', 430, args['teste'][1:-1])
        rtn.append(pre)
        
        pre = DbcCheckService('http://localhost/'+args['site']+'.html','200',501)
        rtn.append(pre)

        return rtn
        