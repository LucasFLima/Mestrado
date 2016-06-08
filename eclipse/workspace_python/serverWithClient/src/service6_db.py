import json
from pydblite import Base

class Simple_db(object):

    def __init__ (self, dataClass):
        self.data = dataClass
        self.className = dataClass.__class__.__name__
        self.keys = dataClass.__dict__.keys()
    
    def insert (self):
        db = Base(self.className + '.pdl')
        self.dinamicCreate(db)
        #db.create('testId', 'testMessage', mode="open")
        #db.insert(testId = vTestId, testMessage = vTestMessage)
        db.insert(self.data)
        db.commit()
        
    def select (self):
        db = Base(self.className + '.pdl')
        db.open()
        for iten in db:
            print iten["codigo"]

    def dinamicCreate(self, db):
        if len(self.keys) == 1:
            db.create(self.keys[0], mode="open")
        elif len(self.keys) == 2:
            db.create(self.keys[0], self.keys[1],
                      mode="open")
        elif len(self.keys) == 3:
            db.create(self.keys[0], self.keys[1],
                      self.keys[2], mode="open")
        elif len(self.keys) == 4:
            db.create(self.keys[0], self.keys[1],
                      self.keys[2], self.keys[3],
                      mode="open")
        elif len(self.keys) == 5:
            db.create(self.keys[0], self.keys[1],
                      self.keys[2], self.keys[3],
                      self.keys[4], mode="open")
        
        
        
        
        
        
        
        
        
        
        
#     def transfomType(x):
#         if isinstance(x, unicode): return str(x)
#         else: return x
# 
#     requestBody = args['requestContent']
#     
#     #######    Replace this section by your logic   #######
#     vTestId = transfomType(json.loads(requestBody)['testId'])
#     vTestMessage = transfomType(json.loads(requestBody)['testMessage'])
# 
#     responseCode = 200 #ResponseCode.Ok
# 
#    
#     db = Base('database_service6.pdl')
#     db.create('testId', 'testMessage', mode="open")
#     db.insert(testId = vTestId, testMessage = vTestMessage)
#     db.commit()
# 
#     result = []
# 
#     responseBody = json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))
#     #######    Replace this section by your logic   #######
# 
# 
#     request.setResponseCode(responseCode)
#     resp = utils.serviceResponse(responseCode, responseBody)
#     
#     return resp