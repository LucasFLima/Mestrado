import json
#import twisted_server
from httplib import HTTPConnection
from twisted.web.http_headers import Headers
from twisted.internet import defer

import service1, service2, service3
 
class GetRequestParameters(object):
    def __init__ (self, xxx, yyy, zzz):
        self.xxx = xxx
        self.yyy = yyy
        self.zzz = zzz
 
class Resource(object): 
 
    @classmethod
    def get(cls, result, request, agent):
#         responseCode = 203 #ResponseCode.Ok
#  
#         #######    Replace this section by your logic   #######
#         result = {}
#         result ['method'] = 'get'
#         result ['path'] = request.path
#         result ['arguments'] = request.args
#         responseBody = json.dumps(result, sort_keys=False, indent=4, separators=(',', ': '))
#         #######    Replace this section by your logic   #######
#         return responseCode, responseBody

        #print 'Service 4 - call unb'
        #return agent.request('GET', "http://www.unb.br", Headers({}), None)
        
        # chamada a outro service por meio de callback
        print 'Service 4 - call service3 por callback'
        d = defer.Deferred()
        d.addCallback(service3.Resource.get, request, agent)
        d.callback(request)
        
        return d
        