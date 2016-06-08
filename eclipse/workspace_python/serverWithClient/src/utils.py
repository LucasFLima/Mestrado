import re

class serviceResponse (object):
    
    def __init__(self, code=None, body=None, endSignal = False):
        self.code = code
        self.body = body
        self.finish = endSignal

def extractArgsFromPath (uri, pattern, path):

    argList = { }
    qtdGroups = len(re.match(pattern, path, re.IGNORECASE).groups())
    for i in range (1, qtdGroups + 1):
        argList[re.match(pattern, uri).group(i)] = re.match(pattern, path).group(i)
    
    return argList

