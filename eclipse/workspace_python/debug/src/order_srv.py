import json
from twisted_server import ResponseCode
from httplib import HTTPConnection
import pre_order_srv
from pre_order_srv import PreConditionOrder
from twisted.web.server import NOT_DONE_YET
from twisted.internet import reactor, defer
import teste3
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from __builtin__ import classmethod
 
class GetRequestParameters(object):
    def __init__ (self, xxx, yyy, zzz):
        self.xxx = xxx
        self.yyy = yyy
        self.zzz = zzz
 
class PostRequestParameters(object):
    def __init__ (self, xxx, yyy, zzz):
        self.xxx = xxx
        self.yyy = yyy
        self.zzz = zzz
 
class Resource(object): 
     
    @classmethod
    def preGetProcessing (self, result, request):
        #######    Replace this section by your logic   #######
        responseCode = ResponseCode.Ok
        
        print ">> preGetProcessing"
        resultData = {}
        resultData ['method'] = 'get'
        resultData ['path'] = request.path
        resultData ['arguments'] = request.args
        responseBody = json.dumps(resultData, sort_keys=False, indent=4, separators=(',', ': '))
        #######    Replace this section by your logic   #######
       
        # raise RuntimeError, "whoops! we encountered an error"

        return responseCode, responseBody


    @classmethod
    def getRequest (self, result, request, extDbc):
        responseCode = ResponseCode.Ok

        print ">> getRequest"
        
        agent = Agent(reactor)

        d2 = agent.request('GET',
                           'http://localhost:8080/store/10',
                           Headers({'User-Agent': ['Twisted Web Client Example']}),
                           None)
        
        d2.addCallback(Resource.cbRequest, extDbc)
        d2.addCallback(Resource.dummy)
        #extDbc.addCallback(d2)
        
        #d2.callback(d2.response)
        print 'Pos callback request'
        
        return NOT_DONE_YET
        #return d2
    
   
    @classmethod
    def cbRequest(self, response, extDbc2):
        print 'Response version:', response.version
        print 'Response code:', response.code
        print 'Response phrase:', response.phrase
        #print 'Response headers:'
        #print pformat(list(response.headers.getAllRawHeaders()))
        d = defer.Deferred()
        d.addCallback(Resource.cbBody)
        return d
        #return response.code
    
    @classmethod
    def cbBody(body):
        print 'Response body:'
        #print body
        return 111
    
    @classmethod
    def dummy(self, str):
        print 'Dummy: %s' % str
        return 404
    
    @classmethod
    def getProcessing (self, result, request):
        #######    Replace this section by your logic   #######
        responseCode = ResponseCode.Ok

        print ">> getProcessing"
        
        resultData = {}
        resultData ['method'] = 'get'
        resultData ['path'] = request.path
        resultData ['arguments'] = request.args
        responseBody = json.dumps(resultData, sort_keys=False, indent=4, separators=(',', ': '))
        #######    Replace this section by your logic   #######
       
        return responseCode, responseBody
    
#        request.write(message)
#        request.finish()
    
    
    @classmethod
    def get(cls, request):
        responseCode = ResponseCode.Ok
        
        dbc1 = defer.Deferred()
        #url =  'http://127.0.0.1:8080/store/getOrder/orderId/10/item/2'
        #dbc1 = PreConditionOrder.dbcCondition(url, PreConditionOrder.callbackSucess, 200)
        #dbc1.addCallback (Resource.preGetProcessing, request)
        #dbc1.addErrback     (Resource.preGetOtherwise, dbc1)
        #dbc1.addCallback (Resource.getProcessing, request)
        dbc1.addCallback (Resource.getRequest, request, dbc1)
        dbc1.addCallback(Resource.dummy)
        dbc1.addCallback(Resource.dummy)
        
        dbc1.callback(request)
        
        a = dbc1.result
        
        
        #print dbc1.result, 'ok'
                
        #return NOT_DONE_YET, NOT_DONE_YET
        #return dbc1.result[0], dbc1.result[1]
        
        
        print 'Result to external function'
        return dbc1.result, 'ok'
     
 
#    @classmethod
#    def post(cls, request):
#        responseCode = ResponseCode.Ok
# 
        #url =  'http://127.0.0.1:8080/store/getOrder/orderId/10/item/2'
        #dbc1 = PreConditionOrder.dbcCondition(url, PreConditionOrder.callbackSucess, 200)
        #dbc1.addCallback (self.postProcessing, request)
        
        #return NOT_DONE_YET
 

