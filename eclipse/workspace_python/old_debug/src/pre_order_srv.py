from twisted.web import resource
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.internet import reactor

class PreConditionOrder(resource.Resource):
    isLeaf = True 
 
    def dbcConditionCheck(self,  response, codeCheck=200, equal=True):
        if (equal and response.code == codeCheck) or (not equal and response.code != codeCheck):
                return ''
        else:
            raise RuntimeError, "Error "
        
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