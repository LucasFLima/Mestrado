import json
from twisted_server import ResponseCode
from httplib import HTTPConnection
import pre_order_srv
from pre_order_srv import PreConditionOrder
from twisted.web.server import NOT_DONE_YET
from twisted.internet import reactor, defer
import teste3
 
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
       
        #raise RuntimeError, "whoops! we encountered an error"

        return responseCode, responseBody

    @classmethod
    def preGetOtherwise (self, f, dbc1):
        #######    Replace this section by your logic   #######
        responseCode = ResponseCode.InternalServerError
        
        f.trap(RuntimeError)
        
        print ">> preGetOthewise"
        responseBody = "Falha"
        #######    Replace this section by your logic   #######
        dbc1.callbacks = []
        return responseCode, responseBody


    
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
        dbc1.addCallback (Resource.preGetProcessing, request)
        dbc1.addErrback     (Resource.preGetOtherwise, dbc1)
        dbc1.addCallback (Resource.getProcessing, request)
        
        dbc1.callback(request)
                
        return dbc1.result[0], dbc1.result[1]
        
    
     
 
#    @classmethod
#    def post(cls, request):
#        responseCode = ResponseCode.Ok
# 
        #url =  'http://127.0.0.1:8080/store/getOrder/orderId/10/item/2'
        #dbc1 = PreConditionOrder.dbcCondition(url, PreConditionOrder.callbackSucess, 200)
        #dbc1.addCallback (self.postProcessing, request)
        
        #return NOT_DONE_YET
 

