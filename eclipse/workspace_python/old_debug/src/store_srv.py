import json
import twisted_server
from twisted_server import ResponseCode
from httplib import HTTPConnection
 
class GetRequestParameters(object):
    def __init__ (self, xxx, yyy, zzz):
        self.xxx = xxx
        self.yyy = yyy
        self.zzz = zzz
 
class Resource(object): 
 
    @classmethod
    def get(cls, request):
        responseCode = ResponseCode.Ok
 
        #######    Replace this section by your logic   #######
        result = {}
        result ['method'] = 'get'
        result ['path'] = request.path
        result ['arguments'] = request.args
        responseBody = json.dumps(result, sort_keys=False, indent=4, separators=(',', ': '))
        #######    Replace this section by your logic   #######
        return responseCode, responseBody
