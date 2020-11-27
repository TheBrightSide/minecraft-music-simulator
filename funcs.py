import json
import os

def readJsonFile(path):
    f = open(path)
    data = json.load(f)
    f.close()
    return data

def writeJsonFile(path, data):
    f = open(path, 'w')
    json.dump(data, f)
    f.close
    return

def addRootArray(array, root):
    for i, e in enumerate(array):
        array[i] = os.path.join(root, array[i])
    return array