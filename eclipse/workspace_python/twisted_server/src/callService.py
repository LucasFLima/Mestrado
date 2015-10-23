from pprint import pformat

from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from posix import wait
from time import sleep

#See: http://twistedmatrix.com/documents/current/web/howto/client.html
#See: http://twistedmatrix.com/documents/12.0.0/core/howto/defer.html#auto1

# class BeginningPrinter(Protocol):
#     def __init__(self, finished):
#         self.finished = finished
#         self.remaining = 1024 * 10
# 
#     def dataReceived(self, bytes):
#         if self.remaining:
#             display = bytes[:self.remaining]
#             print 'Some data received:'
#             print display
#             self.remaining -= len(display)
# 
#     def connectionLost(self, reason):
#         print 'Finished receiving body:', reason.getErrorMessage()
#         self.finished.callback(None)

def callService(url, f):
    agent = Agent(reactor)
    var1 = ''
    d = agent.request(
        'GET',
        url,
        Headers({'User-Agent': ['Twisted Web Client Example']}),
        None)
    
    def cbRequest(response):
        print 'Response code:', response.code
        f(response.code)
        finished = Deferred()
        reactor.stop()
        return finished
    
    def erRequest (ignored):
        print 'Unable to process request'
    
    #Back = cbRequest
    d.addCallback(cbRequest)
    d.addErrback(erRequest)
    
    def cbShutdown(response):
        reactor.stop()
    d.addBoth(cbShutdown)
    
    #reactor.callLater(1, reactor.stop)
    reactor.run()
    
    
    
    #return response.code

#def func(rCode):
#    print 'teste ', rCode
#    return rCode
#
#print 'antes callService'
#url='http://localhost:8080/usuariosChat/instancia/instanciaX/mensagem/usuarioY/usuarios?t=TOKENOK'
#callService(url, func)
#
#print 'depois callService'

