from twisted.internet import defer
from twisted.python import failure, util

"""
Here we have the simplest case, a single callback and a single errback.
"""
from twisted.web.server import NOT_DONE_YET
from twisted.internet.defer import FAILURE


class Teste2 (object):
    
    @classmethod
    def handleFailure(self, f):
        print "errback"
        #print "we got an exception: %s" % (f.getTraceback(),)
        f.trap(RuntimeError)
        return False, '0', 'erro'
     
    @classmethod
    def handleResult(self, result, message):
        global num; num += 1
        print "callback %s" % (num,)
        print "\tmessage %s" % (message,)
        print "\tgot result: %s" % (result,)
        return "yay! handleResult was successful!"
    
    @classmethod
    def doisRetornos(self, result):
        if result[0]:
            print "doisRetornos\n\tresults: %s" % result[0]
            return 'val1', 'val2'
        else:
            return result[1], result[2]
    
    @classmethod
    def doisRetornosX(self, result):
        print "doisRetornosX\n\tresults: %s %s" % (result[0],result[1])
        return result[0], result[1]
    
       
    @classmethod
    def getProcessing (self, result, request):
        #######    Replace this section by your logic   #######
        responseCode = 200
        
        resultData = {}
        resultData ['method'] = 'get'
        resultData ['path'] = 'path'
        resultData ['arguments'] = 'request.args'
        responseBody = 'body'
        #######    Replace this section by your logic   #######
        raise RuntimeError, "whoops! we encountered an error"

       
        return responseCode, responseBody
     
    
    @classmethod
    def deferredExample(self):
        d = defer.Deferred()
        d.addCallback(Teste2.getProcessing, 'request')
        d.addCallback(Teste2.handleResult, 'mensagem 1')
        d.addCallback(Teste2.handleResult, 'mensagem 2')
        d.addCallback(Teste2.handleResult, 'mensagem 3')
        d.addErrback (Teste2.handleFailure, d)
        d.addCallback(Teste2.doisRetornos)
        d.addCallback(Teste2.doisRetornosX)
    
        d.callback("success")
        return d.result[0], d.result[1]
        
    

if __name__ == '__main__':
#    behindTheScenes("success")
    print "\n-------------------------------------------------\n"
    global num; num = 0
    tst = Teste2()
    rtn1, rtn2 = tst.deferredExample()
    print "RTN: %s %s" % (rtn1, rtn2)