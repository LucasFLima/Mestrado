from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.internet import reactor, defer

class Test (object):
       
       
    @classmethod
    def getRequest (self, result, extDefList):

        print "Function getRequest"

        agent = Agent(reactor)

        d2 = agent.request('GET',
                           'http://www.google.com',
                           Headers({'User-Agent': ['Twisted Web Client Example']}),
                           None)
        
        
        d2.addCallback(Test.cbResponse)
        
        # 1 st attempt: return the result of d2. Fail: exceptions.AttributeError: Deferred instance has no attribute 'result'
        #return d2.result            # --> line A
       
        # 2nd attempt: return only the deferr object d2. Don't fail, but I can't get the result of the above request
        return d2                   # --> line B
        
        # 3rd attemp: return None (without return). 
                                        # --> line C
                                        
        # 4th attemp: Add the current Deferred list to the master Deferred (main function)
        #defTmp = extDefList.chainDeferred(d2)
        #extDefList = defTmp
           
    
    @classmethod
    def cbResponse(response):
        
        print 'Function cbResponse %s', response.code
        # This is the return value I want to pass back to deferredChain function (called at line E)
        return response.code            # line D
    
    @classmethod
    def deferredChain(self):
        d = defer.Deferred()
        
        d.addCallback(Test.getRequest, d)  # line E
        d.callback("success")

        return d.result 
        
    

if __name__ == '__main__':
    #tst = Test()
    #rtn = tst.deferredChain()
    
    defA = defer.Deferred()
    defA.addCallback(Test.deferredChain)
    defA.callback("success")
    rtn = defA.result
    reactor.run()
    print "RTN: %s " % rtn