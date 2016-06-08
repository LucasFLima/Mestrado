import json

class Service6(object):
    def __init__(self, codigo, mensagem):
        self.codigo = codigo
        self.mensagem = mensagem
    
    #@classmethod
    #def transfomType(cls, x):
    #    if isinstance(x, unicode): return str(x)
    #    else: return x
    #
    #def jsonLoad (self, jsonData):
    #    self.codigo = self.transfomType(json.loads(jsonData)['testId'])
    #    self.mensagem = self.transfomType(json.loads(jsonData)['testMessage'])