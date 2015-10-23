from twisted_server import *
from urlparse import urlparse
from cgi import parse_qs

class Resource(object):
    @classmethod
    def get(cls, request):
        
        #for k, v in list(params.items()):
        #    print k
        return "The local time is %s" % (request.args,) 
        #return "A lista de argumentos"


    
