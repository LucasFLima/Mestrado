import json
#import twisted_server
from httplib import HTTPConnection
from twisted.web.http_headers import Headers
 
class GetRequestParameters(object):
    def __init__ (self, xxx, yyy, zzz):
        self.xxx = xxx
        self.yyy = yyy
        self.zzz = zzz
 
class Resource(object): 
 
    @classmethod
    def get(cls, result, agent, request, args):

        print '''
        Service 2
        '''

        #return agent.request('GET', "http://www.unb.br", Headers({}), None)
        print 'Service 2 - call service3'
        return agent.request('GET', "http://localhost:8081/service3", Headers({}), None)

