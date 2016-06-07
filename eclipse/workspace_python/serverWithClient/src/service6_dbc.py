from dbcCondition import PreDbcCheckBasic, PostDbcCheckBasic, DbcCheckService

        
class Service6Dbc(object): 
 
    def getPreconditionList (self, args):

        rtn = []
        
        pre = PreDbcCheckBasic('testId', '30', 430, '==')
        rtn.append(pre)
        
        pre = PreDbcCheckBasic('testId', '100', 430, '>')
        rtn.append(pre)
        
        pre = DbcCheckService('http://localhost/'+args['site']+'.html','200',501,'<>')
        rtn.append(pre)

        return rtn
    
    
    def getPostconditionList (self, args):

        rtn = []
        
        post = PostDbcCheckBasic('testMessage', 'success', 450, '==')
        rtn.append(post)
        
        #post = PostDbcCheckBasic('return.body', 'fail', 460, args['teste'][1:-1])
        #rtn.append(post)
       
        return rtn    
    
    def postPreconditionList (self, args):

        rtn = []
        
        post = PostDbcCheckBasic('testId', '20', 430, '==')
        rtn.append(post)
        
        return rtn