from abc import ABCMeta, abstractmethod
from twisted.web.http_headers import Headers
from twisted.internet import defer
from serviceObject import serviceResponse

import json, re

class DbcException(Exception):
    def __init__(self, srvResp):
        self.serviceResponse = srvResp


class HandleOtherwise():
    @classmethod
    def handle (cls, result, request):
        request.setResponseCode(result.value.serviceResponse.code)
        return result.value.serviceResponse

class CheckType:
    argument = 'argument'
    requestBody = 'requestBody'
    responseBody = 'responseBody'

class DbcConditionType:
    PreCondition = 'Pre condition'
    PostCondition = 'Post condition'

class DbcCheck(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def checkCondition(self, result, agent, request, args): pass


    def checkValue (self, argVar):
        if self.testType == '==': return     argVar  == self.value
        if self.testType == '<>': return     argVar  <> self.value
        if self.testType == '>' : return int(argVar) >  int(self.value)
        if self.testType == '>=': return int(argVar) >= int(self.value)
        if self.testType == '<' : return int(argVar) <  int(self.value)
        if self.testType == '<=': return int(argVar) <= int(self.value)
        return False
    

    def jsonValueOfStringId (self, jsonBody, stringId):
        index = stringId.split(".")
        if len(index) == 1: return str(json.loads(jsonBody)[index[0]])
        if len(index) == 2: return str(json.loads(jsonBody)[index[0]][index[1]])
        if len(index) == 3: return str(json.loads(jsonBody)[index[0]][index[1]][index[2]])
        if len(index) == 4: return str(json.loads(jsonBody)[index[0]][index[1]][index[2]][index[3]])
        if len(index) == 5: return str(json.loads(jsonBody)[index[0]][index[1]][index[2]][index[3]][index[4]])
 


class DbcCheckBasic (DbcCheck):
    def __init__(self, arg,  value, excptVal, checkType, testType, conditionType):
        self.arg = arg
        self.testType = testType
        self.value = value
        self.checkType = checkType
        self.excptVal = excptVal    
        self.conditionType = conditionType    


    def checkCondition(self, result, agent, request, args):
        if self.checkType == CheckType.argument:
            if self.checkValue(args[self.arg]):
                request.setResponseCode(self.excptVal)
                resp = serviceResponse(self.excptVal, self.conditionType + ' failure ('+self.arg+' '+self.testType+' '+self.value+'; Value of attribute '+self.arg+' is '+args[self.arg]+')')
                raise DbcException(resp)
        
        elif self.checkType == CheckType.requestBody:
            requestBody = args['requestContent'];
            
            if requestBody <> '[]':
                valueOfArg = self.jsonValueOfStringId(requestBody, self.arg)
                
                if self.checkValue(valueOfArg):
                    request.setResponseCode(self.excptVal)
                    resp = serviceResponse(self.excptVal, self.conditionType + ' failure ('+self.arg+' '+self.testType+' '+self.value+'; Value of attribute '+self.arg+' is '+valueOfArg+')')
                    raise DbcException(resp)
                        
        elif self.checkType == CheckType.responseBody:
            if result.body <> '[]':
                valueOfArg = self.jsonValueOfStringId(result.body, self.arg)
                
                if self.checkValue(valueOfArg):
                    request.setResponseCode(self.excptVal)
                    resp = serviceResponse(self.excptVal, self.conditionType + ' failure ('+self.arg+' '+self.testType+' '+self.value+'; Value of attribute '+self.arg+' is '+valueOfArg+')')
                    raise DbcException(resp)
                
        return result





class DbcCheckService (DbcCheck):
    def __init__(self, url, value, excpt, checkType, testType, conditionType):
        self.url = url
        self.testType = testType
        self.value = value
        self.checkType = checkType
        self.excpt = excpt
        self.conditionType = conditionType

    def checkCondition(self, result, agent, request, args):
        def cbResponse (response, request, getUrl):
            if self.checkValue(str(response.code)):
                request.setResponseCode(self.excpt)
                resp = serviceResponse(self.excpt, self.conditionType + ' failure (GET '+getUrl+' '+self.testType+' '+self.value+'; Request returns '+str(response.code)+')')
                raise DbcException(resp)
            else:
                return result
        
        # Arguments to be replaced are enclosed between '{' and '}'
        splitUrl = re.split('\\{|\\}', self.url)
        
        getUrl = ''
        if self.checkType == CheckType.argument:
            # The odd elements in the splited url are elements to be replaced with its efective values
            for i in range(0, len(splitUrl)):
                if i % 2 == 1:
                    getUrl += args[splitUrl[i]]
                else:
                    getUrl += splitUrl[i]
                    
        elif self.checkType == CheckType.requestBody:
            requestBody = args['requestContent'];
            
            if requestBody <> '[]':
                
                # The odd elements in the splited url are elements to be replaced with its efective values
                for i in range(0, len(splitUrl)):
                    if i % 2 == 1:
                        getUrl += self.jsonValueOfStringId(requestBody, splitUrl[i])
                    else:
                        getUrl += splitUrl[i]
                
        
        d = agent.request('GET', getUrl, Headers({}), None)
            
        d.addCallback(cbResponse, request, getUrl)
        return d


