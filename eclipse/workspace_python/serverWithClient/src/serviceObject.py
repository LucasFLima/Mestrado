class serviceResponse (object):
    
    def __init__(self, code, body, endSignal = False):
        self.code = code
        self.body = body
        self.finish = endSignal