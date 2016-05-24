from twisted.web import server, resource
from twisted.internet import reactor
from twisted.web.server import NOT_DONE_YET
from pre_order_srv import PreConditionOrder

class SimpleServer(resource.Resource):
    isLeaf = True 
   
    def getProcessing(self, message, request):
        request.write(message)
        request.finish()
   
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