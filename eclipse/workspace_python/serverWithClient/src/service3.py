import json
#import twisted_server
from httplib import HTTPConnection
from twisted.web.http_headers import Headers
from twisted.python.util import println
 
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

        print 'Service 3 - site local'
        return agent.request('GET', "http://localhost/site.html", Headers({}), None)
        