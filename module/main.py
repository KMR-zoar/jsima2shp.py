import os
from module.xmlReader import readXML
from module.jpgisObjectCreator import createPointObject, createCurveObject, createSurfaceObject
from module.jsimaObjectCreator import createKakuchiObject, createChibanObject, extractCoordSys
from module.createShapefile import createShapefile
from module.proj import copyProjFile

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

  pointObject = createPointObject(xmlObject[1])
  curveObject = createCurveObject(xmlObject[1], pointObject)
  surfaceObject = createSurfaceObject(xmlObject[1], curveObject)

  kakuchiObject = createKakuchiObject(xmlObject[1], surfaceObject)
  chibanObject = createChibanObject(xmlObject[1], kakuchiObject)

  coordSys = extractCoordSys(xmlObject[0])
  copyProjFile(coordSys, absPath)
  createShapefile(chibanObject, absPath)
