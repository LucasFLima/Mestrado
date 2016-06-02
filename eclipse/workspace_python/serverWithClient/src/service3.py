import json
#import twisted_server
from httplib import HTTPConnection
from twisted.web.http_headers import Headers
from twisted.internet import defer
from serviceObjects import serviceResponse
 
class GetRequestParameters(object):
    def __init__ (self, xxx, yyy, zzz):
        self.xxx = xxx
        self.yyy = yyy
        self.zzz = zzz
 
class Resource(object): 
 
    @classmethod
    def requestSrv3 (self, result, request, agent):
        print 'requestSrv3'
        d = agent.request('GET', "http://localhost/site.html", Headers({}), None)
        
        d.addCallback(Resource.cbResponse, request)
        return d
    
    @classmethod
    def cbResponse (self, response, request):
        #print 'cbResponse'
        #res = serviceResponse(response.code, 'ok')
        #return res
        
        
        
        print 'cbResponse'
        request.write('cbResponse - ok')
        request.setResponseCode(response.code)
        return response
        
    
    @classmethod
    def get(cls, result, request, agent):

        #print 'Service 3 - site local'
        #d = agent.request('GET', "http://localhost/site.html", Headers({}), None)
        
        d = defer.Deferred()
        d.addCallback(Resource.requestSrv3, request, agent)
        
        d.callback(request)
        
        return d
        