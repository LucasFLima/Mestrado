from dbcCondition import PreDbcCheckBasic, PostDbcCheckBasic, DbcCheckService

        
class Service6Dbc(object): 
 
    def preConditionList (self, args):

        rtn = []
        
        pre = PreDbcCheckBasic('testId', '30', 430, args['teste'][1:-1])
        rtn.append(pre)
        
        pre = DbcCheckService('http://localhost/'+args['site']+'.html','200',501)
        rtn.append(pre)

        return rtn
    
    
    def postConditionList (self, args):

        rtn = []
        
        post = PostDbcCheckBasic('return.body', 'success', 450, args['teste'][1:-1])
        rtn.append(post)
        
        post = PostDbcCheckBasic('return.body', 'fail', 460, args['teste'][1:-1])
        rtn.append(post)
       
        return rtn    