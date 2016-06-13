class Resource(object): 
 
    @classmethod
    def get(cls, result, agent, request, args):

        d = defer.Deferred()
        dbcCondList = DbcConditionsList()
        
        # loads pre conditions filters
        dbcCondList.addFilterCondition(d, OperationType.GET, DbcConditionType.PreCondition, agent, request, args)
        # call Get operation
        d.addCallback(ServiceXSrv.do_Get,      request, args)
        # loads post conditions filters
        dbcCondList.addFilterCondition(d, OperationType.GET, DbcConditionType.PostCondition, agent, request, args)
        # errorBack to return otherwise value if some filter fails
        d.addErrback (HandleOtherwise.handle, request)
        
        d.callback(utils.serviceResponse())
        return d