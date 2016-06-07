class serviceResponse (object):
    
    def __init__(self, code=None, body=None, endSignal = False):
        self.code = code
        self.body = body
        self.finish = endSignal