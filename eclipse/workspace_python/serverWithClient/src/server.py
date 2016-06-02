from twisted.web import server, resource
from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.web.server import NOT_DONE_YET
from twisted.internet.protocol import Protocol

agent = Agent(reactor)

class HTTPReturner(Protocol):
    def __init__(self, request):
        self._request = request
        self._data = ""

    def dataReceived(self, input):
        self._data += input

    def connectionLost(self, reason):
        self._request.write(self._data)
        self._request.finish()

class HelloResource(resource.Resource):
    isLeaf = True
    
    def createModule(self, srv):
        #moduleName  = 'service1.py'
        #module = __import__(moduleName[0:len(moduleName)-3])
        module = __import__(srv[1:9])
        return module
    
    def render_GET(self, request):
        def cbResponse(response):
            request.setHeader("content-type", "text/html")
            #response.deliverBody(HTTPReturner(request))
            response.deliverBody()
    
      
        #d = agent.request('GET', "https://www.google.com/search?q=YOLO", Headers({}), None)
        #d.addCallback(cbResponse)
        #return NOT_DONE_YET
      
        #srv = self.createModule(request.uri)
        #responseCode, response = srv.Resource.get(request, agent)
        #request.setResponseCode(responseCode)
        #return response
      
        srv = self.createModule(request.uri)
        d = srv.Resource.get(None, request, agent)
        d.addCallback(cbResponse)
        
        return NOT_DONE_YET

print 'Starting server at port 8081...'
reactor.listenTCP(8081, server.Site(HelloResource()))
reactor.run() 