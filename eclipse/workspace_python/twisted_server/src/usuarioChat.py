import json
import twisted_server
from twisted_server import ResponseCode
import callService
from httplib import HTTPConnection

class Recibo (object):
    def __init__(self, destinatario,dataHora):
        self.destinatario = destinatario
        self.dataHora = dataHora

class GetRequestParameters:
    def __init__ (self, token, nomeInstancia, idUsuarioDestino):
        self.token = token
        self.nomeInstancia = nomeInstancia
        self.idUsuarioDestino = idUsuarioDestino

class Chamada (object):
    retorno = ''
    
    def __init__ (self, url = None):
        self.url = url
        
    def call(self):
        r=HTTPConnection("127.0.0.1", 8080)
        r.request('GET', '/hello')
        res = r.getresponse()
        self.retorno = res.status
        

class Resource(object):
    @classmethod
    def processaChamada (rCode):
        
        rCode = rCode
    
    @classmethod
    def get(cls, request):
        
        #set variables used in capability
        responseCode = ResponseCode.Ok
        getRequestParameters = GetRequestParameters (request.args['t'], request.args['nomeInstancia'], request.args['idUsuarioDestino'])
        
        if getRequestParameters.token == 'TOKEN':
            responseCode = ResponseCode.InvalidPrecondition
            return responseCode, 'Invalid Precondition'
        
        if getRequestParameters.idUsuarioDestino != "usuarioY":
            responseCode = ResponseCode.Unauthorized
            return responseCode, 'Unauthorized User'
        
        #url1 = 'http://localhost:8080/usuariosChat/instancia/instanciaX/mensagem/usuarioX/usuarios?t=TOKENOK'
        #callService(url1, Resource.processaChamada)
#         try:
#             r=HTTPConnection("127.0.0.1", 8080, timeout=2)
#             r.request('GET', '/hello')
#             res = r.getresponse()
#             statusCode = res.status
#         except Exception as e:
#             print e
#             statusCode = 0
        x = Chamada()
        x.call()
      
        #######    Replace this section by your logic   #######
        result = {}
        result ['method'] = 'GET'
        result ['path'] = request.path
        result ['arguments'] = request.args
        result ['statusCode'] = x.retorno
        
        return responseCode, json.dumps(result, sort_keys=False, indent=4, separators=(',', ': '))
        #######    Replace this section by your logic   #######
        
    
    @classmethod
    def post(cls, request):
        
#         print 'Pre request'
#         r=HTTPConnection('localhost:8080')
#         r.request('GET', '/usuariosChat/instancia/instanciaX/mensagem/usuarioX/usuarios?t=TOKENOK')
#         print 'request'
#         try:
#             res = r.getresponse()
#         except:
#             print 'exception'
# 
#         print 'response ', res.status
             
        
        #######    Replace this section by your logic   #######
        result = {}
        result ['method'] = 'POST'
        result ['path'] = request.path
        result ['arguments'] = request.args
        #result ['statusCode'] = res.status
        
        return responseCode, json.dumps(result, sort_keys=False, indent=4, separators=(',', ': '))
    
    @classmethod
    def put(cls, request):
        
        result = {}
        result ['method'] = 'PUT'
        result ['path'] = request.path
        result ['arguments'] = request.args
        
        return responseCode, json.dumps(result, sort_keys=False, indent=4, separators=(',', ': '))
    
    @classmethod
    def delete(cls, request):
        
        result = {}
        result ['method'] = 'DELETE'
        result ['path'] = request.path
        result ['arguments'] = request.args
        
        return responseCode, json.dumps(result, sort_keys=False, indent=4, separators=(',', ': '))

    
