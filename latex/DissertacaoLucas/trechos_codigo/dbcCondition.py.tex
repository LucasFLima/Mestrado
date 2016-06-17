from abc import ABCMeta, abstractmethod
from twisted.web.http_headers import Headers
from twisted.internet import defer
import utils

import json, re

# Class to handle the exceptions of dbc conditions
class DbcException(Exception):
    def __init__(self, srvResp):
        self.serviceResponse = srvResp

class HandleOtherwise():
    @classmethod
    def handle (cls, result, request):
        request.setResponseCode(result.value.serviceResponse.code)
        return result.value.serviceResponse

# Class to define constants used in DbcCondition*
class ValuesSource:
    argument = 'argument'
    requestBody = 'requestBody'
    responseBody = 'responseBody'

class DbcConditionType:
    PreCondition = 'Pre condition'
    PostCondition = 'Post condition'

class OperationType:
    GET = 'GET'
    POST = 'POST'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'

# Abstract class of dbcCheck. This class is implemented by DbcCheckBasic and DbcCheckService
class DbcCheck(object):
    __metaclass__ = ABCMeta
    
    #This method is used to validate the DbCCondition (generic)
    @abstractmethod
    def checkCondition(self, result, agent, request, args): pass

    #This method is used in filter of types of dbcCondition (require and ensure) and Http method (GET, POST, DELETE, UPDATE)
    def checkOperationAndType(self, operation, conditionType):
        if (self.operationType == operation and self.conditionType == conditionType):
            return True
        return False

    #This method compares the value retrived from request/response (argVar) and the value expected for dbccondition (self.value)
    def checkValue (self, argVar):
        if self.testType == '==': return     argVar  == self.value
        if self.testType == '<>': return     argVar  <> self.value
        if self.testType == '>' : return int(argVar) >  int(self.value)
        if self.testType == '>=': return int(argVar) >= int(self.value)
        if self.testType == '<' : return int(argVar) <  int(self.value)
        if self.testType == '<=': return int(argVar) <= int(self.value)
        return False
    
    # This util method find a value on a json structure using a string dotted argument ('field1.field2')
    # It supports up to five levels
    def jsonValueOfStringId (self, jsonBody, stringId):
        index = stringId.split(".")
        if len(index) == 1: return str(json.loads(jsonBody)[index[0]])
        if len(index) == 2: return str(json.loads(jsonBody)[index[0]][index[1]])
        if len(index) == 3: return str(json.loads(jsonBody)[index[0]][index[1]][index[2]])
        if len(index) == 4: return str(json.loads(jsonBody)[index[0]][index[1]][index[2]][index[3]])
        if len(index) == 5: return str(json.loads(jsonBody)[index[0]][index[1]][index[2]][index[3]][index[4]])
 
        
class DbcCheckBasic (DbcCheck):
    """Class to check a basic precondition, i. e., direct check arguments (from request or response) values"""
    
    def __init__(self, arg,  testType, value, excptVal, checkType, conditionType, operationType):
        """Constructor of a basic dbc condition check.
    
        Keyword arguments:
        arg -- The name of argument to be compared. (Example: 'fieldId', 'field.id')
        testType -- Type of comparation. (Example: '==', '<>', '>=')
        value -- The value to be tested with argument value
        checkType -- The source of values. It may be request URI, request Body and response Body (See ValuesSource())
        excptVal -- If the dbc condition fail, this value is returned to client (HTTP status value)
        conditionType -- Indicate if is pre or post condition (See DbcConditionType())
        operationType -- Indicate the type of HTTP operation (See OperationType())
        """
        self.arg = arg
        self.testType = testType
        self.value = value
        self.checkType = checkType
        self.excptVal = excptVal    
        self.conditionType = conditionType
        self.operationType = operationType    


    def checkCondition(self, result, agent, request, args):
        """ Method to check if value expected by dbc condition occurrs """
        
        if self.checkType == ValuesSource.argument:
            """ Case 1: Value of argument is in request URI """
            if not self.checkValue(args[self.arg]):
                request.setResponseCode(self.excptVal)
                resp = utils.serviceResponse(self.excptVal, self.conditionType + ' failure ('+self.arg+' '+self.testType+' '+self.value+'; Value of attribute '+self.arg+' is '+args[self.arg]+')')
                raise DbcException(resp)
        
        
        elif self.checkType == ValuesSource.requestBody:
            """ Case 2: Value of argument is in the request body (json format) """
            requestBody = args['requestContent'];
            
            if requestBody <> '[]':
                valueOfArg = self.jsonValueOfStringId(requestBody, self.arg)
                
                if not self.checkValue(valueOfArg):
                    request.setResponseCode(self.excptVal)
                    resp = utils.serviceResponse(self.excptVal, self.conditionType + ' failure ('+self.arg+' '+self.testType+' '+self.value+'; Value of attribute '+self.arg+' is '+valueOfArg+')')
                    raise DbcException(resp)
                        
        
        elif self.checkType == ValuesSource.responseBody:
            """ Case 3: Value of argument is in the response body (json format) """
            if result.body <> '[]':
                valueOfArg = self.jsonValueOfStringId(result.body, self.arg)
                
                if not self.checkValue(valueOfArg):
                    request.setResponseCode(self.excptVal)
                    resp = utils.serviceResponse(self.excptVal, self.conditionType + ' failure ('+self.arg+' '+self.testType+' '+self.value+'; Value of attribute '+self.arg+' is '+valueOfArg+')')
                    raise DbcException(resp)
                
        return result





class DbcCheckService (DbcCheck):
    """Class to check a basic precondition, i. e., direct check arguments (from request or response) values"""
    
    def __init__(self, url, testType, value, excpt, checkType, conditionType, operationType):
        """Constructor dbc condition check based on a service.
    
        Keyword arguments:
        url -- The URL of the service. Variable are enclosed by '{' and '}'. (Example: 'http://localhost/srv1/{id}')
        testType -- Type of comparation. (Example: '==', '<>', '>=')
        value -- The value to be tested with argument value
        checkType -- The source of values. It may be request URI, request Body and response Body (See ValuesSource())
        excptVal -- If the dbc condition fail, this value is returned to client (HTTP status value)
        conditionType -- Indicate if is pre or post condition (See DbcConditionType())
        operationType -- Indicate the type of HTTP operation (See OperationType())
        """
        self.url = url
        self.testType = testType
        self.value = value
        self.checkType = checkType
        self.excpt = excpt
        self.conditionType = conditionType
        self.operationType = operationType

    def checkCondition(self, result, agent, request, args):
        """ Method to check if value expected by dbc condition occurrs """
        
        
        def cbResponse (response, request, getUrl):
            """ Callback function of request. On Twisted, request are asynchronous """
            if not self.checkValue(str(response.code)):
                request.setResponseCode(self.excpt)
                resp = utils.serviceResponse(self.excpt, self.conditionType + ' failure (GET '+getUrl+' '+self.testType+' '+self.value+'; Request returns '+str(response.code)+')')
                raise DbcException(resp)
            else:
                return result
        
        # Arguments to be replaced are enclosed between '{' and '}'
        splitUrl = re.split('\\{|\\}', self.url)
        
        getUrl = ''
        if self.checkType == ValuesSource.argument:
            """ Case 1: Value of argument is in request URI """
            # The odd elements in the splited url are elements to be replaced with its efective values
            for i in range(0, len(splitUrl)):
                if i % 2 == 1:
                    getUrl += args[splitUrl[i]]
                else:
                    getUrl += splitUrl[i]
                    
        elif self.checkType == ValuesSource.requestBody:
            """ Case 2: Value of argument is in the request body (json format) """
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



class DbcConditionList(object):
    """ Class that process a list of DbcConditions. Used on service operations filters"""
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def __init__(self): pass
    
    def getListByType(self, operation, dbcType):
        """ Retrives from the list the conditions of a specific type and for a specific operation"""
        rtn = []
        for dbc in self.list:
            if dbc.checkOperationAndType(operation, dbcType):
                rtn.append(dbc)
        return rtn
     
    def addFilterCondition(self, d, operation, dbcType, agent, request, args):
        """ Add to a callback chain dbc conditions of a specific type and for a specific operation """
        dbc = self.getListByType(operation, dbcType)
        for f in dbc:
            d.addCallback(f.checkCondition, agent, request, args)
