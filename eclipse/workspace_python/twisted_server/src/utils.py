import re

def extractArgsFromPath (uri, pattern, path):

    argList = { }
    qtdGroups = len(re.match(pattern, path, re.IGNORECASE).groups())
    for i in range (1, qtdGroups + 1):
        argList[re.match(pattern, uri).group(i)] = re.match(pattern, path).group(i)

    return argList
