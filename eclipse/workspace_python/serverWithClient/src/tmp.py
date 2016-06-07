from twisted.internet.defer import FAILURE
from twisted.internet import defer
from pydblite import Base
import pydblite

class MyCustomException(Exception):
    def __init__(self, msg, code):
        self.code = code
        self.message = msg

class CodMsg(object):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

class Resource(object):
 
    @classmethod
    def checkCondition(cls, result):
        if result == "error":
            return "erro"
        else:
            
            db = Base('database_service1.pdl')
            db.create('cod', 'message', mode="open")
            db.insert(cod='1', message='valid')
            db.insert(cod='2', message='not valid')
            db.commit()
            #for rec in (db("age") > 30):
            for rec in db:
                print rec["cod"] +' '+ rec["message"]
            
            
            
            return "ok"
    
d = defer.Deferred()

d.addCallback(Resource.checkCondition)

d.callback("asdlfkj")

print d.result
        