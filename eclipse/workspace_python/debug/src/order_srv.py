import json
from twisted_server import ResponseCode, server
from httplib import HTTPConnection
import pre_order_srv
from pre_order_srv import PreConditionOrder
from twisted.web.server import NOT_DONE_YET
from twisted.internet import reactor, defer
import teste3
from twisted.web.client import Agent, getPage
from twisted.web.http_headers import Headers
from __builtin__ import classmethod
from requests.api import request
 
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
     
    @classmethod
    def preGetProcessing (self, result, request):
        #######    Replace this section by your logic   #######
        responseCode = ResponseCode.Ok
        
        print ">> preGetProcessing"
        resultData = {}
        resultData ['method'] = 'get'
        resultData ['path'] = request.path
        resultData ['arguments'] = request.args
        responseBody = json.dumps(resultData, sort_keys=False, indent=4, separators=(',', ': '))
        #######    Replace this section by your logic   #######
       
        # raise RuntimeError, "whoops! we encountered an error"

        return responseCode, responseBody


    @classmethod
    def getRequest (self, result, request, extDbc):
        responseCode = ResponseCode.Ok

        print ">> getRequest"
        
        agent = Agent(reactor)

        d2 = agent.request('GET',
                           'http://localhost:8080/store/10',
                           Headers({'User-Agent': ['Twisted Web Client Example']}),
                           None)
        
        d2.addCallback(Resource.cbRequest, extDbc)
        #extDbc.pause()

        d2.callback(request)
        print 'Pos callback request'
        
        return d2
    
   
    @classmethod
    def cbRequest(self, response, extDbc2):
        print 'Response version:', response.version
        print 'Response code:', response.code
        print 'Response phrase:', response.phrase
        #print 'Response headers:'
        #print pformat(list(response.headers.getAllRawHeaders()))
        #d = defer.Deferred()
        #d.addCallback(Resource.cbBody)
        #extDbc2.resume()
        
        #return d
        return response.code, response.phrase
    
    @classmethod
    def cbBody(body):
        print 'Response body:'
        #print body
        return 2
    
    @classmethod
    def dummy(self, result):
        print 'Show results %s %s' % (result[0], result[1])
        print result
        #print output
        return result[0], result[1]
   
    @classmethod
    def endRequest(self, result, request):
        print 'end Request'
        request.finish()
        return 10, 'ok-10'
        
    
    @classmethod
    def basicReturn(self, request):
        print 'basicReturn'
        return [200, 'Chamada completa']
    
    @classmethod
    def basicReturnDef(self, request):
        d3 = defer.Deferred()
        d3.addCallback(Resource.basicReturn)
        
        #return 10, 'ok-10'
        return d3

    @classmethod
    def basicReturnDefYield(self, request):
        r1, r2 = yield Resource.basicReturn(request)
        defer.returnValue(r1, r2)
        #return 10, 'ok-10'
        #return d3
        
    
    @classmethod
    def getProcessing (self, result, request):
        #######    Replace this section by your logic   #######
        responseCode = ResponseCode.Ok

        print ">> getProcessing"
        
        resultData = {}
        resultData ['method'] = 'get'
        resultData ['path'] = request.path
        resultData ['arguments'] = request.args
        responseBody = json.dumps(resultData, sort_keys=False, indent=4, separators=(',', ': '))
        #######    Replace this section by your logic   #######
       
        return responseCode, responseBody
    
#        request.write(message)
#        request.finish()
    
    
    @classmethod
    @defer.inlineCallbacks
    def pre_get_goole(self):
        tst = yield  Resource.get_google()
        #
        print 'pre_get_google'
        defer.returnValue(tst)
    
    @classmethod
    @defer.inlineCallbacks
    def get_google(self):
        #body = yield getPage("http://www.google.com/")
        #defer.returnValue(body)
        
        
        agent = Agent(reactor)
        resp = yield agent.request('GET', 'http://www.google.com/')
        print 'get_google'
        defer.returnValue(resp)
    
    
    @classmethod
    #@defer.inlineCallbacks
    def get(cls, aRequest):
        responseCode = ResponseCode.Ok
        
        #dget = getPage('http://localhost:8080/store/10')
        #dget.addCallback (Resource.dummy)
        #dget.callback(request)
        

        dbc1 = defer.Deferred()
        
        dbc1.addCallback (Resource.getRequest, request, dbc1)
        return dbc1
        
        
        #dbc1.addCallback(Resource.basicReturn)
        #dbc1.addCallback(Resource.basicReturnDef)
        #dbc1.addCallback(Resource.basicReturnDefYield)
        
       
       
        #dbc1.addCallback (Resource.dummy)
        #dbc1.addBoth(Resource.endRequest, request)
        
        #dbc1.callback(request)
        
   
        #tst = yield  Resource.pre_get_goole()
        
        print 'After agent'
        #print tst
#         
        
        #res = yield Resource.basicReturn(request)
        #res2 = yield Resource.test_smth()
        
        #res2 = None
        #print 'get function return'
        #defer.returnValue(res)
        #return defer.returnValue(a), 'Teste'
        #defer.returnValue(tst)
        #defer.returnValue(tst)
        
        print 'get function return'
        
        
        #return dbc1.result[0], dbc1.result[1]
        #return server.NOT_DONE_YET, server.NOT_DONE_YET
        #return dbc1
        #server.NOT_DONE_YET