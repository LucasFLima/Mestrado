    from twisted.internet import reactor, defer
    from twisted.web.client import Agent
    from twisted.web.http_headers import Headers
    from __builtin__ import classmethod
     
    
    class Resource(object): 
         
    
        @classmethod
        # Function to do a request for another service
        def getRequest (self, result, request):
    
            print ">> getRequest"
            
            agent = Agent(reactor)
    
            d2 = agent.request('GET',
                               'http://localhost:8080/store/10',
                               Headers({'User-Agent': ['Twisted Web Client Example']}),
                               None)
            
            d2.addCallback(Resource.cbRequest)
            
            return d2
        
        # Function that extracts the response code of response and return it
        @classmethod
        def cbRequest(self, response):
            print 'Response code:', response.code
            print 'Response phrase:', response.phrase
    
            return response.code, response.phrase
        
        # Function only to show that the results of cbRequest arrived here (external callback)
        @classmethod
        def showResults(self, result):
            print 'Show results %s %s' % (result[0], result[1])
            return result[0], result[1]
        
      
        # Processo a render_get
        @classmethod
        def get(cls, request):
            
            dbc1 = defer.Deferred()
            dbc1.addCallback (Resource.getRequest, request)
            
            dbc1.addCallback (Resource.showResults)
            dbc1.callback(request)
            
            return dbc1.result[0], dbc1.result[1]
            #==> FAIL:  exceptions.AttributeError: Deferred instance has no attribute '__getitem__' 
            
            #return server.NOT_DONE_YET, server.NOT_DONE_YET
            #==> DONT FAIL, BUT THE CLIENT DON'T RECEIVE THE RESULTS (CLIENT WAITING)
            
