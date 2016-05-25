from twisted.web import resource
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.internet import reactor, defer

# A callback that unpacks and prints the results of a DeferredList
def printResult(result):
    for (success, value) in result:
        if success:
            print 'Success:', value
        else:
            print 'Failure:', value.getErrorMessage()

# Create three deferreds.
deferred1 = defer.Deferred()
deferred2 = defer.Deferred()
deferred3 = defer.Deferred()

# Pack them into a DeferredList
dl = defer.DeferredList([deferred1, deferred2, deferred3], consumeErrors=True)

# Add our callback
dl.addCallback(printResult)

# Fire our three deferreds with various values.
deferred1.callback('one')
deferred2.errback(Exception('bang!'))
deferred3.callback('three')

# At this point, dl will fire its callback, printing:
#    Success: one
#    Failure: bang!
#    Success: three
# (note that defer.SUCCESS == True, and defer.FAILURE == False)