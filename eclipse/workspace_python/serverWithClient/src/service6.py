import json
#import twisted_server
from httplib import HTTPConnection
from twisted.web.http_headers import Headers
from twisted.internet import defer
from serviceObject import serviceResponse
from dbcCondition import DbcCheckBasic, DbcCheckService
from service6_dbc import Service6Dbc

 
class GetRequestParameters(object):
    def __init__ (self, xxx, yyy, zzz):
        self.xxx = xxx
        self.yyy = yyy
        self.zzz = zzz

        
class Resource(object): 
 
    @classmethod
    def getCore (self, result, request):
        if result.finish:
            return result
        else:
            responseCode = 300 #ResponseCode.Ok
     
            #######    Replace this section by your logic   #######
            result = {}
            result ['method'] = 'get'
            result ['path'] = request.path
            result ['arguments'] = request.args
            responseBody = json.dumps(result, sort_keys=False, indent=4, separators=(',', ': '))
            #######    Replace this section by your logic   #######
    
            request.setResponseCode(responseCode)
            resp = serviceResponse(responseCode, responseBody)
            return resp
    
    @classmethod
    def get(cls, result, agent, request, args):

        resp = serviceResponse(None, None)
        
        d = defer.Deferred()
        
        preCondLst = Service6Dbc()
        l = preCondLst.preConditionList(args)
        for dbc in l:
            d.addCallback(dbc.checkCondition, agent, request, args)
        
        
        #tst = DbcCheckBasic('testId', '30', 430, args['teste'][1:-1])
        #d.addCallback(tst.checkCondition, agent, request, args)
        #
        #srv = DbcCheckService('http://localhost/'+args['site']+'.html','200',501)
        #d.addCallback(srv.checkCondition, agent, request, args)
        
        d.addCallback(Resource.getCore,     request)
        
        #lst = []
        #for x in range (1, 4):
        #    pre = DoRequest('msg'+str(x))
        #    lst.append(pre)
        # 
        #for l in lst:
        #    l.printMsg()
        
        d.callback(resp)
        
        return d
        