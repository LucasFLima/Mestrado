import json
#import twisted_server
from twisted.web.http_headers import Headers
from twisted.internet import defer, reactor
from serviceObject import serviceResponse
from dbcCondition import HandleOtherwise
from service6_dbc import Service6Dbc
from time import sleep

 
class GetRequestParameters(object):
    def __init__ (self, xxx, yyy, zzz):
        self.xxx = xxx
        self.yyy = yyy
        self.zzz = zzz

        
class Resource(object): 
 
    @classmethod
    def getCore (self, result, request, args):
        if result.finish:
            return result
        else:
            responseCode = 300 #ResponseCode.Ok
     
            #######    Replace this section by your logic   #######
            result = {}
            result ['method'] = 'get'
            result ['path'] = request.path
            result ['arguments'] = request.args
            result ['return'] = {'body': 'fail'}
            responseBody = json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))
            #######    Replace this section by your logic   #######

    
            request.setResponseCode(responseCode)
            resp = serviceResponse(responseCode, responseBody)
            
            return resp
    
    @classmethod
    def postCondition(cls, result, agent, request, args):
        print 'postCondition'
        return result
    
    @classmethod
    def get(cls, result, agent, request, args):

        d = defer.Deferred()
        
        preCondLst = Service6Dbc()
        l = preCondLst.preConditionList(args)
        for dbc in l:
            d.addCallback(dbc.checkCondition, agent, request, args)
        
        d.addCallback(Resource.getCore,      request, args)
        
        #d.addCallback(Resource.postCondition, agent, request, args)
        postCondLst = Service6Dbc()
        l = postCondLst.postConditionList(args)
        for dbc in l:
            d.addCallback(dbc.checkCondition, agent, request, args)        
        
        d.addErrback (HandleOtherwise.handle, request)
        
        d.callback(serviceResponse())
        #reactor.callLater(int(args['tempo']), d.callback, serviceResponse())
        
        return d
        