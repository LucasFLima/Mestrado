from twisted.web import server, resource
from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.web.server import NOT_DONE_YET
from twisted.internet.protocol import Protocol
from serviceObject import serviceResponse
import re
import utils
import json

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

class ServerResource(resource.Resource):
    isLeaf = True
    
    def __init__(self):
        with open('routes.json') as data_file:
            routes = json.load(data_file)
            self.routeTable = { }
            self.pathTable = { }
            for route in routes["routes"]:
                self.routeTable[route["pattern"]] = route["srv"]
                self.pathTable[route["pattern"]] = route["uri"]
    
    def createModuleAndArgs(self, request):
        """ An utility method for parsing an HTTP request. 
        """
        server = None
        for pattern in (self.routeTable.keys()):
            pathCheck = re.compile(pattern)
            if pathCheck.match(request.path):
                server =  self.routeTable.get(pattern)
                reqUri =  self.pathTable.get(pattern)
                reqPattern = pattern

        # in the case there is not a route for the request, 
        # we raise a LookupError exception. 
        if server == None:
            raise LookupError("Invalid route")

        # ok, we found a specific server. so we need to load 
        # the corresponding Python module. 
        moduleName  = str(server)
        module = __import__(moduleName[0:len(moduleName)-3])

        # finally, we populate a Request object from the 
        # HTTP request. This is not a cohesive module, but 
        # it helps to minimize code duplications. By the way,
        # it is just an utility method. 
        args = {} 
        for key, value in request.args.iteritems():
            args[key] = value[0]

        # extract values of arguments sent inside the request path
        pathArgs = utils.extractArgsFromPath(reqUri, reqPattern, request.path)
        for key, value in pathArgs.iteritems():
            args[key] = value
        
        args['requestContent'] = request.content.read()

        return module, args
    
    
    def render_GET(self, request):
        def cbResponse(response, request):
            request.setHeader("content-type", "text/html")
            
            if isinstance(response, str):
                request.finish()
            elif isinstance(response, serviceResponse):
                request.write(response.body)
                #request.setResponseCode(response.code)
                request.finish()
            else:
                response.deliverBody(HTTPReturner(request))
            
      
        srv, args = self.createModuleAndArgs(request)
        d = srv.Resource.get(None, agent, request, args)
        d.addCallback(cbResponse, request)
        
        return NOT_DONE_YET

    def render_POST(self, request):
        def cbResponse(response, request):
            request.setHeader("content-type", "text/html")
            
            if isinstance(response, str):
                request.finish()
            elif isinstance(response, serviceResponse):
                request.write(response.body)
                #request.setResponseCode(response.code)
                request.finish()
            else:
                response.deliverBody(HTTPReturner(request))
            
      
        srv, args = self.createModuleAndArgs(request)
        d = srv.Resource.post(None, agent, request, args)
        d.addCallback(cbResponse, request)
        
        return NOT_DONE_YET
    
    def render_DELETE(self, request):
        def cbResponse(response, request):
            request.setHeader("content-type", "text/html")
            
            if isinstance(response, str):
                request.finish()
            elif isinstance(response, serviceResponse):
                request.write(response.body)
                #request.setResponseCode(response.code)
                request.finish()
            else:
                response.deliverBody(HTTPReturner(request))
            
      
        srv, args = self.createModuleAndArgs(request)
        d = srv.Resource.delete(None, agent, request, args)
        d.addCallback(cbResponse, request)
        
        return NOT_DONE_YET

print 'Starting server at port 8081...'
reactor.listenTCP(8081, server.Site(ServerResource()))
reactor.run() 