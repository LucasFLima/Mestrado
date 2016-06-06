from twisted.internet.defer import FAILURE
from twisted.internet import defer

class MyCustomException(Exception):
    def __init__(self, msg, code):
        self.code = code
        self.message = msg

class CodMsg(object):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

class Resource(object):
 
    @classmethod
    def checkCondition(cls, result):
        if result == "error":
            cdm = CodMsg(1, 'Error 1')
            raise MyCustomException('Message', 23)
        else:
            return "ok"
    
    @classmethod
    def erBackTst (cls, result):
        
        # How to get the value of cd here?
        print result.value.message
        print result.value.code
    
    
d = defer.Deferred()

d.addCallback(Resource.checkCondition)


d.addErrback(Resource.erBackTst)

d.callback("error")

print d.result
        