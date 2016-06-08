import json
#import twisted_server
#from twisted.web.http_headers import Headers
import utils
from pydblite import Base

class Service6Srv(object):
    @classmethod
    def do_Get (self, result, request, args):
 
        #######    Replace this section by your logic   #######
        db = Base('database_service6.pdl')
        db.create('testId', 'testMessage', mode="open")
        result = db(testId = int(args['testId']))
        
        if len(result) == 0:
            responseCode = 404 #ResponseCode.Ok
            responseBody = json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            responseCode = 200 #ResponseCode.Ok
            responseBody = json.dumps(result[0], sort_keys=True, indent=4, separators=(',', ': '))
        #######    Replace this section by your logic   #######


        request.setResponseCode(responseCode)
        resp = utils.serviceResponse(responseCode, responseBody)
        
        return resp
    
    @classmethod
    def do_Post (self, result, request, args):
        def transfomType(x):
            if isinstance(x, unicode): return str(x)
            else: return x
    
        requestBody = args['requestContent']
        
        #######    Replace this section by your logic   #######
        vTestId = transfomType(json.loads(requestBody)['testId'])
        vTestMessage = transfomType(json.loads(requestBody)['testMessage'])
    
        responseCode = 200 #ResponseCode.Ok
 
       
        db = Base('database_service6.pdl')
        db.create('testId', 'testMessage', mode="open")
        db.insert(testId = vTestId, testMessage = vTestMessage)
        db.commit()

        result = []

        responseBody = json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))
        #######    Replace this section by your logic   #######


        request.setResponseCode(responseCode)
        resp = utils.serviceResponse(responseCode, responseBody)
        
        return resp
    
    @classmethod
    def do_Delete (self, result, request, args):
        def transfomType(x):
            if isinstance(x, unicode): return str(x)
            else: return x
    
        #######    Replace this section by your logic   #######
        db = Base('database_service6.pdl')
        db.create('testId', 'testMessage', mode="open")
        result = db(testId = int(args['testId']))
        
        if len(result) == 0:
            responseCode = 404 #ResponseCode.Ok
            responseBody = json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            responseCode = 200 #ResponseCode.Ok
            responseBody = json.dumps(result[0], sort_keys=True, indent=4, separators=(',', ': '))
            db.delete(result[0])
            db.commit()
        #######    Replace this section by your logic   #######


        request.setResponseCode(responseCode)
        resp = utils.serviceResponse(responseCode, responseBody)
        
        return resp