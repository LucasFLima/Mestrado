import json
#import twisted_server
from httplib import HTTPConnection
from twisted.web.http_headers import Headers
from twisted.internet import defer
from serviceObject import serviceResponse
 
class GetRequestParameters(object):
    def __init__ (self, xxx, yyy, zzz):
        self.xxx = xxx
        self.yyy = yyy
        self.zzz = zzz
 
class Resource(object): 
 
    @classmethod
    def requestSrv3 (self, result, agent, request, args):
        print 'requestSrv3'
        d = agent.request('GET', "http://localhost/site2.html", Headers({}), None)
        
        d.addCallback(Resource.cbResponse, request)
        return d
    
    @classmethod
    def cbResponse (self, response, request):
        
        #print 'cbResponse'
        #request.write('cbResponse - ok')
        #request.setResponseCode(response.code)
        #return response
        
        request.setResponseCode(response.code)
        resp = serviceResponse(response.code, 'Retorno do servico 3')
        return resp
    
    @classmethod
    def get(cls, result, agent, request, args):

        #print 'Service 3 - site local'
        #d = agent.request('GET', "http://localhost/site.html", Headers({}), None)
        
        d = defer.Deferred()
        d.addCallback(Resource.requestSrv3, agent, request, args)
        
        d.callback(request)
        
        return d
        