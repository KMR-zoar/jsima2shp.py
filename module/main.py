import os
from module.xmlReader import readXML
from module.jpgisObjectCreator import createPointObject, createCurveObject, createSurfaceObject
from module.jsimaObjectCreator import createKakuchiObject, createChibanObject
from module.createShapefile import createShapefile

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

  kakuchiObject = createKakuchiObject(xmlObject, surfaceObject)
  chibanObject = createChibanObject(xmlObject, kakuchiObject)

  createShapefile(chibanObject, absPath)
