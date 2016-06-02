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
    def byPass(cls, result):
        print 'byPass'
        print result
        return result
    
    @classmethod
    def get(cls, result, request, agent):


        #print 'Service 4 - call unb'
        #return agent.request('GET', "http://www.unb.br", Headers({}), None)
        
        # chamada a outro service por meio de callback
        print 'Service 4 - call service3 por callback'
        d = defer.Deferred()
        d.addCallback(service3.Resource.get, request, agent)
        
        d.addCallback(Resource.byPass)
        
        

        d.callback(request)
        
        return d
        