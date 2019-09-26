import os
from module.xmlReader import readXML
from module.jpgisObjectCreator import createPointObject, createCurveObject, createSurfaceObject

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

  pointObject = createPointObject(xmlObject)
  curveObject = createCurveObject(xmlObject, pointObject)
  surfaceObject = createSurfaceObject(xmlObject, curveObject)


