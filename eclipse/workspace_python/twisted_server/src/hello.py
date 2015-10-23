from twisted_server import *
from time import sleep
from httplib import HTTPConnection

class Resource(object):
    @classmethod
    def get(cls, request):
        message = ""
#         r=HTTPConnection('www.unb.br')
#         r.request('GET', '/')
#         res = r.getresponse()
#         
#         message = "hello "+str(res.status)

        sleep(10)

        return 200, message 


    
