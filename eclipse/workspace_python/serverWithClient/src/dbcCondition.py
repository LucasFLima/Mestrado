from abc import ABCMeta, abstractmethod
from twisted.web.http_headers import Headers
from twisted.internet import defer
from serviceObject import serviceResponse
from twisted.internet.defer import FAILURE
from twisted.python.failure import Failure

class DbcException(Exception):
    def __init__(self, srvResp):
        self.serviceResponse = srvResp


class DbcCheck(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def checkCondition(self, result, agent, request, args): pass
    
class DbcCheckBasic (DbcCheck):
    def __init__(self, arg, value, excptVal, test = '==' ):
        self.arg = arg
        self.test = test
        self.value = value
        self.excptVal = excptVal
        
    def checkValue (self, argVar):
        if self.test == '==': return argVar == self.value
        if self.test == '<>': return argVar <> self.value
        if self.test == '>' : return int(argVar) >  int(self.value)
        if self.test == '>=': return int(argVar) >= int(self.value)
        if self.test == '<' : return int(argVar) <  int(self.value)
        if self.test == '<=': return int(argVar) <= int(self.value)
        return False


    def checkCondition(self, result, agent, request, args):
        if self.checkValue(args[self.arg]):
            request.setResponseCode(self.excptVal)
            resp = serviceResponse(self.excptVal, 'Falhou precondicao ('+self.arg+' '+self.test+' '+self.value+')', True)
            #return resp
            raise DbcException(resp)
            
        return result


class DbcCheckService (DbcCheck):
    def __init__(self, url, rtn, excpt):
        self.url = url
        self.rtn = rtn
        self.excpt = excpt

    def checkCondition(self, result, agent, request, args):
        def cbResponse (response, request):
            if str(response.code) == self.rtn:
                request.setResponseCode(self.excpt)
                resp = serviceResponse(self.excpt, 'Falhou precondicao (GET '+self.url+' == '+self.rtn+')', True)
                return resp
            else:
                return result
            
        d = agent.request('GET', self.url, Headers({}), None)
        
        d.addCallback(cbResponse, request)
        return d

#class handleOtherwise():
#    @classmethod
#    def handle (self, result, request):
#        request.setResponseCode(result.value.serviceResponse.code)
#        return result.value.serviceResponse
