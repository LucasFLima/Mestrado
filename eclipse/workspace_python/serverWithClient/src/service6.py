import json
#import twisted_server
from twisted.web.http_headers import Headers
from twisted.internet import defer, reactor
from serviceObject import serviceResponse
from dbcCondition import HandleOtherwise
from service6_dbc import Service6Dbc
from pydblite import Base

 
class GetRequestParameters(object):
    def __init__ (self, xxx, yyy, zzz):
        self.xxx = xxx
        self.yyy = yyy
        self.zzz = zzz

        
class Resource(object): 
 
    @classmethod
    def getCore (self, result, request, args):
 
        #######    Replace this section by your logic   #######
        db = Base('database_service6.pdl')
        db.create('testId', 'testMessage', mode="open")
        result = db(testId = int(args['testId']))
        
        if len(result) == 0:
            responseCode = 404 #ResponseCode.Ok
            responseBody = json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            responseCode = 200 #ResponseCode.Ok
            responseBody = json.dumps(result[0], sort_keys=True, indent=4, separators=(',', ': '))
        #######    Replace this section by your logic   #######


        request.setResponseCode(responseCode)
        resp = serviceResponse(responseCode, responseBody)
        
        return resp
    

    
    @classmethod
    def get(cls, result, agent, request, args):

        d = defer.Deferred()
        
        preCondLst = Service6Dbc()
        l = preCondLst.get_PreconditionList()
        for dbc in l:
            d.addCallback(dbc.checkCondition, agent, request, args)
        
        d.addCallback(Resource.getCore,      request, args)
        
        
        postCondLst = Service6Dbc()
        l = postCondLst.get_PostconditionList()
        for dbc in l:
            d.addCallback(dbc.checkCondition, agent, request, args)        
        
        d.addErrback (HandleOtherwise.handle, request)
        
        d.callback(serviceResponse())
        #reactor.callLater(int(args['tempo']), d.callback, serviceResponse())
        
        return d
    
    @classmethod
    def postCore (self, result, request, args):
        def transfomType(x):
            if isinstance(x, unicode): return str(x)
            else: return x
    
        requestBody = request.content.read()
        
        vTestId = transfomType(json.loads(requestBody)['testId'])
        vTestMessage = transfomType(json.loads(requestBody)['testMessage'])
    
        responseCode = 200 #ResponseCode.Ok
 
        #######    Replace this section by your logic   #######
        db = Base('database_service6.pdl')
        db.create('testId', 'testMessage', mode="open")
        db.insert(testId = vTestId, testMessage = vTestMessage)
        db.commit()

        result = []

        responseBody = json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))
        #######    Replace this section by your logic   #######


        request.setResponseCode(responseCode)
        resp = serviceResponse(responseCode, responseBody)
        
        return resp
    
    @classmethod
    def post(cls, result, agent, request, args):

        d = defer.Deferred()
        
        preCondLst = Service6Dbc()
        l = preCondLst.post_PreconditionList()
        for dbc in l:
            d.addCallback(dbc.checkCondition, agent, request, args)
        
        d.addCallback(Resource.postCore,      request, args)
        
        
        #postCondLst = Service6Dbc()
        #l = postCondLst.post_PostconditionList(args)
        #for dbc in l:
        #    d.addCallback(dbc.checkCondition, agent, request, args)        
        
        d.addErrback (HandleOtherwise.handle, request)
        
        d.callback(serviceResponse())
        #reactor.callLater(int(args['tempo']), d.callback, serviceResponse())
        
        return d