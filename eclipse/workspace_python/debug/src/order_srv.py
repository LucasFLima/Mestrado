import json
import twisted_server
from twisted_server import ResponseCode
from httplib import HTTPConnection
import pre_order_srv
from pre_order_srv import PreConditionOrder
from twisted.web.server import NOT_DONE_YET
 
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
 
    def getProcessing (self, message, request):
        #######    Replace this section by your logic   #######
        responseCode = ResponseCode.Ok
        
        result = {}
        result ['method'] = 'post'
        result ['path'] = request.path
        result ['arguments'] = request.args
        responseBody = json.dumps(result, sort_keys=False, indent=4, separators=(',', ': '))
        #######    Replace this section by your logic   #######
        return responseCode, responseBody
    
#        request.write(message)
#        request.finish()
        
    def postProcessing (self, message, request):
        #######    Replace this section by your logic   #######
        responseCode = ResponseCode.Ok
        
        result = {}
        result ['method'] = 'post'
        result ['path'] = request.path
        result ['arguments'] = request.args
        responseBody = json.dumps(result, sort_keys=False, indent=4, separators=(',', ': '))
        #######    Replace this section by your logic   #######
        return responseCode, responseBody
        
#        request.write(message)
#        request.finish()
    
    @classmethod
    def get(cls, request):
        responseCode = ResponseCode.Ok
        
        url =  'http://127.0.0.1:8080/store/getOrder/orderId/10/item/2'
        dbc1 = PreConditionOrder.dbcCondition(url, PreConditionOrder.callbackSucess, 200)
        dbc1.addCallback (self.getProcessing, request)
        
        return NOT_DONE_YET
 
#         
#         if not ( request.args['orderId'] <> '0' ) :
#             responseCode = ResponseCode.InvalidPrecondition
#             return responseCode, "InvalidPrecondition"
#         
#         
#         #######    Replace this section by your logic   #######
#         result = {}
#         result ['method'] = 'get'
#         result ['path'] = request.path
#         result ['arguments'] = request.args
#         responseBody = json.dumps(result, sort_keys=False, indent=4, separators=(',', ': '))
#         #######    Replace this section by your logic   #######
#         return responseCode, responseBody
 
    @classmethod
    def post(cls, request):
        responseCode = ResponseCode.Ok
 
        url =  'http://127.0.0.1:8080/store/getOrder/orderId/10/item/2'
        dbc1 = PreConditionOrder.dbcCondition(url, PreConditionOrder.callbackSucess, 200)
        dbc1.addCallback (self.postProcessing, request)
        
        return NOT_DONE_YET
 

