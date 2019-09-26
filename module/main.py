import os
from module.xmlReader import readXML

def getAbsPath(argsPath):
  currentDir = os.getcwd()
  path = ''
  if os.path.isabs(argsPath):
    path = argsPath
  else:
    path = os.path.join(currentDir, argsPath)
  return path

def main(path):
  absPath = getAbsPath(path)
  xmlObject = readXML(absPath)


