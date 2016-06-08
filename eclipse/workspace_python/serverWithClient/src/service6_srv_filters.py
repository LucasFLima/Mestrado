#from twisted.web.http_headers import Headers
from twisted.internet import defer
from serviceObject import serviceResponse
from dbcCondition import HandleOtherwise
from dbcCondition import DbcCheckService, ValuesSource, DbcCheckBasic, DbcConditionType, OperationType, DbcConditionList
from service6_srv import Service6
 
class GetRequestParameters(object):
    def __init__ (self, xxx, yyy, zzz):
        self.xxx = xxx
        self.yyy = yyy
        self.zzz = zzz

class DbcConditionsList(DbcConditionList):
    def __init__(self):
        self.list = []
        self.list.append(DbcCheckBasic('testId', '<>', '5', 430, ValuesSource.argument, DbcConditionType.PreCondition, OperationType.GET))
        self.list.append(DbcCheckService('http://localhost:8081/store/{testId}?site=site', '==','300', 501, ValuesSource.argument, DbcConditionType.PreCondition, OperationType.GET))
        self.list.append(DbcCheckService('http://localhost/{site}.html', '==','200', 501, ValuesSource.argument, DbcConditionType.PreCondition, OperationType.GET))
        
        self.list.append(DbcCheckBasic('testMessage', '<>', 'fail', 460, ValuesSource.responseBody, DbcConditionType.PostCondition, OperationType.GET))
       
        self.list.append(DbcCheckBasic('testId', '<>', '20', 430, ValuesSource.requestBody, DbcConditionType.PreCondition, OperationType.POST))
        self.list.append(DbcCheckService('http://localhost:8081/test/{testId}?site=site', '==', '404', 501, ValuesSource.requestBody, DbcConditionType.PreCondition, OperationType.POST))

        self.list.append(DbcCheckService('http://localhost:8081/test/{testId}?site=site', '<>', '404', 501, ValuesSource.argument, DbcConditionType.PreCondition, OperationType.DELETE))

        
class Resource(object): 
 
    @classmethod
    def get(cls, result, agent, request, args):

        d = defer.Deferred()
        dbcCondList = DbcConditionsList()
        
        # loads pre conditions filters
        dbcCondList.addFilterCondition(d, OperationType.GET, DbcConditionType.PreCondition, agent, request, args)
  
        # call Get operation
        d.addCallback(Service6.do_Get,      request, args)
        
        # loads post conditions filters
        dbcCondList.addFilterCondition(d, OperationType.GET, DbcConditionType.PostCondition, agent, request, args)
  
        # errorBack to return otherwise value if some filter fails
        d.addErrback (HandleOtherwise.handle, request)
        
        d.callback(serviceResponse())
        
        return d

    
    @classmethod
    def post(cls, result, agent, request, args):

        d = defer.Deferred()
        dbcCondList = DbcConditionsList()
        
        # loads pre conditions filters
        dbcCondList.addFilterCondition(d, OperationType.POST, DbcConditionType.PreCondition, agent, request, args)
        
        # call Post operation
        d.addCallback(Service6.do_Post,      request, args)
        
        # loads post conditions filters
        dbcCondList.addFilterCondition(d, OperationType.POST, DbcConditionType.PostCondition, agent, request, args)
  
        # errorBack to return otherwise value if some filter fails
        d.addErrback (HandleOtherwise.handle, request)
        
        d.callback(serviceResponse())
        #reactor.callLater(int(args['tempo']), d.callback, serviceResponse())
        
        return d
    
    @classmethod
    def delete(cls, result, agent, request, args):

        d = defer.Deferred()
        dbcCondList = DbcConditionsList()
        
        # loads pre conditions filters
        dbcCondList.addFilterCondition(d, OperationType.DELETE, DbcConditionType.PreCondition, agent, request, args)
        
        # call Post operation
        d.addCallback(Service6.do_Delete,      request, args)
        
        # loads post conditions filters
        dbcCondList.addFilterCondition(d, OperationType.DELETE, DbcConditionType.PostCondition, agent, request, args)
  
        # errorBack to return otherwise value if some filter fails
        d.addErrback (HandleOtherwise.handle, request)
        
        d.callback(serviceResponse())
        #reactor.callLater(int(args['tempo']), d.callback, serviceResponse())
        
        return d