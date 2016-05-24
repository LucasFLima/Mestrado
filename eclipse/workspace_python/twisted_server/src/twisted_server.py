import json
import re
import utils

from twisted.web import server, resource
from twisted.internet import reactor

# class Resource(object):
#     __metaclass__ = abc.ABCMeta

#     @abc.abstractmethod
#     def get(self, request):
#         """ expected method for handling GET requests""" 
#         return

#     @abc.abstractmethod
#     def post(self, request):
#         """ expected method for handling POST requests""" 
#         return

class Request:
    def __init__(self, path = None, args = None, body = None):
        self.path = path
        self.args = args
        self.body = body

class Response:
    def __init__(self, code = 200, body = None):
        self.code = code
        self.body = body 

class ResponseCode:
    Ok = 200
    Created = 201
    BadRequest = 400
    Unauthorized = 401
    InvalidPrecondition = 412
    InternalServerError = 500
    

class TwistedServer(resource.Resource):
    """ Implements an HTTP Server for handling REST APIs. 
    """
    isLeaf = True
    
    def __init__(self):
        with open('routes.json') as data_file:
            routes = json.load(data_file)
            self.routeTable = { }
            self.pathTable = { }
            for route in routes["routes"]:
                self.routeTable[route["pattern"]] = route["srv"]
                self.pathTable[route["pattern"]] = route["uri"]
    
    def createModuleAndRequest(self, request):
        """ An utility method for parsing an HTTP request. 
        """ 
        server = None
        #server = self.routeTable.get(request.path, None)
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
        
        return module, Request(request.path, args)
 

    def render_GET(self, request):
        """ Deals with HTTP GET requests. 
                
        Args:
           request: an HTTP request from the twisted API

        Returns:
           A reponse to the HTTP request. Ideally, this response should be 
           in JSON format. As a side effect, if something goes wrong, 
           it is necessary to set the correct HTTP response code. For 
           instance, if the route does not exist, we set the BadRequest 
           response code. 
        """
        print request.path
        
        try:
            module, aRequest = self.createModuleAndRequest(request)
            responseCode, response = module.Resource.get(aRequest)
            request.setResponseCode(responseCode)
            return response
        except LookupError as e:
            request.setResponseCode(ResponseCode.BadRequest)
            return ResponseCode.BadRequest
 #       except:
 #           request.setResponseCode(ResponseCode.InternalServerError)
 #           return ResponseCode.BadRequest

    
    def render_POST(self, request):
        """ Deals with HTTP POST requests.
        
        Args:
           request: an HTTP Request from the twisted API

        Returns:
          A response to the HTTP request. Please, for more details, 
          see the documentation of render_GET.
        """
        try:
            module, aRequest = self.createModuleAndRequest(request)
            responseCode, response = module.Resource.post(aRequest)
            request.setResponseCode(responseCode)
            return response
        except LookupError as e:
            request.setResponseCode(ResponseCode.BadRequest)
            return ResponseCode.BadRequest
        except:
            request.setResponseCode(ResponseCode.InternalServerError)
            return ResponseCode.BadRequest

    def render_DELETE(self, request):
        """ Deals with HTTP DELETE requests.
        
        Args:
           request: an HTTP Request from the twisted API

        Returns:
          A response to the HTTP request. Please, for more details, 
          see the documentation of render_GET.
        """
        try:
            module, aRequest = self.createModuleAndRequest(request)
            responseCode, response = module.Resource.delete(aRequest)
            request.setResponseCode(responseCode)
            return response
        except LookupError as e:
            request.setResponseCode(ResponseCode.BadRequest)
            return ResponseCode.BadRequest
        except:
            request.setResponseCode(ResponseCode.InternalServerError)
            return ResponseCode.BadRequest
        
    def render_PUT(self, request):
        """ Deals with HTTP PUT requests.
        
        Args:
           request: an HTTP Request from the twisted API

        Returns:
          A response to the HTTP request. Please, for more details, 
          see the documentation of render_GET.
        """
        try:
            module, aRequest = self.createModuleAndRequest(request)
            responseCode, response = module.Resource.put(aRequest)
            request.setResponseCode(responseCode)
            return response
        except LookupError as e:
            request.setResponseCode(ResponseCode.BadRequest)
            return ResponseCode.BadRequest
        except:
            request.setResponseCode(ResponseCode.InternalServerError)
            return ResponseCode.BadRequest
            
if __name__ == "__main__" :
    print 'Starting server at port 8080...' 
    server.NOT_DONE_YET
    site = server.Site(TwistedServer())
    reactor.listenTCP(8080, site)
    reactor.run()
