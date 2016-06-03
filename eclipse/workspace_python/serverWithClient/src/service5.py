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
    def requestSrv5 (self, result, agent, request, args):
        if result.finish:
            return result
        else:
            def cbResponse (response, request):
                if response.code == 404:
                    request.setResponseCode(401)
                    resp = serviceResponse(401, 'Falhou precondicao requestSrv5', True)
                    return resp
                else:
                    return result
            
            d = agent.request('GET', 'http://localhost/'+args['site']+'.html', Headers({}), None)
            
            d.addCallback(cbResponse, request)
            return d
    
    @classmethod
    def requestBsc5 (self, result, agent, request, args):
        if result.finish:
            return result
        else:
            if args['storeId'] == '0':
                request.setResponseCode(400)
                resp = serviceResponse(400, 'Falhou precondicao resquestBsc5', True)
                return resp
            else:
                return result
                
    @classmethod
    def getCore (self, result, request):
        if result.finish:
            return result
        else:
            responseCode = 300 #ResponseCode.Ok
     
            #######    Replace this section by your logic   #######
            result = {}
            result ['method'] = 'get'
            result ['path'] = request.path
            result ['arguments'] = request.args
            responseBody = json.dumps(result, sort_keys=False, indent=4, separators=(',', ': '))
            #######    Replace this section by your logic   #######
    
            request.setResponseCode(responseCode)
            resp = serviceResponse(responseCode, responseBody)
            return resp
    
    @classmethod
    def get(cls, result, agent, request, args):

        #print 'Service 3 - site local'
        #d = agent.request('GET', "http://localhost/site.html", Headers({}), None)
        
        resp = serviceResponse(None, None)
        
        d = defer.Deferred()
        d.addCallback(Resource.requestSrv5, agent, request, args)
        d.addCallback(Resource.requestBsc5, agent, request, args)
        d.addCallback(Resource.getCore,     request)
        
        
        d.callback(resp)
        
        return d
        