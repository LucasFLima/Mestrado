from twisted.internet import defer
from twisted.python import failure, util


class Test (object):
    
    @classmethod
    def handleFailure(self, f, d):
        print "handleFailure"
        f.trap(RuntimeError)
        d.callbacks = []
        return '0', 'erro'
     
    @classmethod
    def handleResult(self, result, message):
        print "handleResult of %s. Old results %s, %s: " % (message, result[0], result[1])
        return 1, 'ok'
    
    @classmethod
    def doFailure (self, result, message):
        print "handleResult of %s. Old results %s, %s: " % (message, result[0], result[1])
        raise RuntimeError, "whoops! we encountered an error"
     
    
    @classmethod
    def deferredExample(self):
        d = defer.Deferred()
        # 1o. call without error
        d.addCallback(Test.handleResult, 'call 1')
        # 2o. call without error
        d.addCallback(Test.handleResult, 'call 1')
        # 3o. call causes the failure
        d.addCallback(Test.doFailure,    'call 3')
        # the failure calls the error back 
        d.addErrback (Test.handleFailure, d) # - A -
        # after error back, the next call back is called
        d.addCallback(Test.handleResult, 'call 4')
        # and the last call back is called
        d.addCallback(Test.handleResult, 'call 5')
        
        d.callback("success")
        return d.result[0], d.result[1]
        
    

if __name__ == '__main__':
#    behindTheScenes("success")
    print "\n-------------------------------------------------\n"
    global num; num = 0
    tst = Test()
    rtn1, rtn2 = tst.deferredExample()
    print "RTN: %s %s" % (rtn1, rtn2)