from abc import ABCMeta, abstractmethod
from twisted.web.http_headers import Headers
from twisted.internet import defer
from serviceObject import serviceResponse
from twisted.internet.defer import FAILURE
from twisted.python.failure import Failure
import json

class DbcException(Exception):
    def __init__(self, srvResp):
        self.serviceResponse = srvResp


class HandleOtherwise():
    @classmethod
    def handle (cls, result, request):
        request.setResponseCode(result.value.serviceResponse.code)
        return result.value.serviceResponse


class DbcCheck(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def checkCondition(self, result, agent, request, args): pass

   
class PreDbcCheckBasic (DbcCheck):
    def __init__(self, arg, value, excptVal, test = '==' ):
        self.arg = arg
        self.test = test
        self.value = value
        self.excptVal = excptVal
        
    def checkValue (self, argVar):
        if self.test == '==': return     argVar  == self.value
        if self.test == '<>': return     argVar  <> self.value
        if self.test == '>' : return int(argVar) >  int(self.value)
        if self.test == '>=': return int(argVar) >= int(self.value)
        if self.test == '<' : return int(argVar) <  int(self.value)
        if self.test == '<=': return int(argVar) <= int(self.value)
        return False


    def checkCondition(self, result, agent, request, args):
        if self.checkValue(args[self.arg]):
            request.setResponseCode(self.excptVal)
            resp = serviceResponse(self.excptVal, 'Pre condition failure ('+self.arg+' '+self.test+' '+self.value+')', True)
            #return resp
            raise DbcException(resp)
            
        return result

class PostDbcCheckBasic (DbcCheck):
    def __init__(self, arg, value, excptVal, test = '==' ):
        self.arg = arg
        self.test = test
        self.value = value
        self.excptVal = excptVal
        
    def checkValue (self, argVar):
        if self.test == '==': return     argVar  == self.value
        if self.test == '<>': return     argVar  <> self.value
        if self.test == '>' : return int(argVar) >  int(self.value)
        if self.test == '>=': return int(argVar) >= int(self.value)
        if self.test == '<' : return int(argVar) <  int(self.value)
        if self.test == '<=': return int(argVar) <= int(self.value)
        return False

    def getValueByStringIndex (self, result):
        index = self.arg.split(".")
        if len(index) == 1: return str(json.loads(result.body)[index[0]])
        if len(index) == 2: return str(json.loads(result.body)[index[0]][index[1]])
        if len(index) == 3: return str(json.loads(result.body)[index[0]][index[1]][index[2]])
        if len(index) == 4: return str(json.loads(result.body)[index[0]][index[1]][index[2]][index[3]])
        if len(index) == 5: return str(json.loads(result.body)[index[0]][index[1]][index[2]][index[3]][index[4]])
 
    def checkCondition(self, result, agent, request, args):
        valueOfArg = self.getValueByStringIndex(result)
        
        if self.checkValue(valueOfArg):
            request.setResponseCode(self.excptVal)
            resp = serviceResponse(self.excptVal, 'Post condition failure ('+self.arg+' '+self.test+' '+self.value+')', True)
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
                resp = serviceResponse(self.excpt, 'Pre condition failure (GET '+self.url+' == '+self.rtn+')', True)
                raise DbcException(resp)
            else:
                return result
            
        d = agent.request('GET', self.url, Headers({}), None)
        
        d.addCallback(cbResponse, request)
        return d


