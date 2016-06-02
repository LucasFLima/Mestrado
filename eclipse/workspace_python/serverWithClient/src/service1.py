import json
#import twisted_server
from httplib import HTTPConnection
from twisted.internet import defer
from twisted.web.client import Response
from twisted.web.http_headers import Headers
 
class GetRequestParameters(object):
    def __init__ (self, xxx, yyy, zzz):
        self.xxx = xxx
        self.yyy = yyy
        self.zzz = zzz
 
class Resource(object): 
 
    @classmethod
    def createResponse(cls, request):
        responseCode = 201 #ResponseCode.Ok
 
        #######    Replace this section by your logic   #######
        result = {}
        result ['method'] = 'get'
        result ['path'] = request.path
        result ['arguments'] = request.args
        responseBody = json.dumps(result, sort_keys=False, indent=4, separators=(',', ': '))
        #######    Replace this section by your logic   #######
        #return responseCode, responseBody
        request.setResponseCode(responseCode)
        request.write(responseBody)
        
        
        
        resp = Response(('HTTP', 1, 1), 201, 'bla bla', Headers(), None)
        
        
        return resp
 
    @classmethod
    def get(cls, result, request, agent):
        
        d = defer.Deferred()
        d.addCallback(Resource.createResponse)
        d.callback(request)
        
        return d
        