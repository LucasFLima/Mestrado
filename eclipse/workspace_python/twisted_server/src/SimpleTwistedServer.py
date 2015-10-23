from twisted.web import server, resource
from twisted.internet import reactor, defer, threads
from twisted.internet.defer import Deferred
from twisted.web.server import NOT_DONE_YET
from twisted.web.client import Agent
from twisted.web.http_headers import Headers

class SimpleServer(resource.Resource):
    isLeaf = True 
   
    def getProcessing(self, message, request):
        request.write(message)
        request.finish()
    
    def dbcConditionCheck(self,  response, codeCheck=200, equal=True):
        if (equal and response.code == codeCheck) or (not equal and response.code != codeCheck):
                return ''
        else:
            raise RuntimeError, "Error"
        
    def dbcCondition (self, url, callbackChain, rCode, eqTest = True):
        agent = Agent(reactor)
        d = agent.request(
            'GET',
            url,
            Headers({'User-Agent': ['Twisted Web Client']}),
            None)
                    
        # The following callback verifies the response code of agent request
        d.addCallback (self.dbcConditionCheck, codeCheck=rCode, equal=eqTest)
        
        # If the previous callback throws on error, callbackFail is called. Otherwise, callbackSuccess is.
        d.addCallbacks(callbackChain, self.callbackFail)

        return d

    def callbackSucess(self, result):
        print 'callbackSucess called'
        return 'callbackSucess called'
    
    def callbackFail(self, result):
        print 'callbackFail called' 
        return 'callbackFail called' 
        
    def render_GET(self, request):
         
        if request.path == '/success':
            request.setResponseCode(200)
            return 'success'
        
        if request.path == '/fail':
            request.setResponseCode(400)
            return 'fail'
        
        if request.path == '/check':
           
            url = 'http://127.0.0.1:8082/'+str(request.args['target1'][0])
            
            dbc1 = self.dbcCondition(url, self.callbackSucess, 200)
            
            url = 'http://127.0.0.1:8082/'+str(request.args['target2'][0])
            
            dbc1 = self.dbcCondition(url, self.callbackSucess, 200)
            
            # The last callback process the main get request 
            dbc1.addCallback (self.getProcessing, request)
            
            return NOT_DONE_YET
            
        else:
            return 'Unknown site'

site = server.Site(SimpleServer())
porta = 8082
print 'Running server on port ' + str(porta)
reactor.listenTCP(porta, site)
reactor.run()