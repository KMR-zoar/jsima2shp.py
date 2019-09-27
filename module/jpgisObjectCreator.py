from module.classes.feature import Properties, Feature

def createPointObject(xmlObject):
  gmPointEleStr = '{http://www.gsi.go.jp/GIS/jpgis/standardSchemas2.1_2009-05}GM_Point'

  pointObject = {}

  for pointElement in xmlObject.findall(gmPointEleStr):
    # SIMA-JPGIS(X,Y) => GIS(Y,X)
    # SIMA-JPGIS と GIS では X,Y が逆
    pointObject[pointElement.attrib['id']] = [
      float(pointElement[1][0].text.split(' ')[1]),
      float(pointElement[1][0].text.split(' ')[0])
    ]
  
  return pointObject

def createCurveObject(xmlObject, pointObject):
  gmCurveEleStr = '{http://www.gsi.go.jp/GIS/jpgis/standardSchemas2.1_2009-05}GM_Curve'
  segmentEleStr = '{http://www.gsi.go.jp/GIS/jpgis/standardSchemas2.1_2009-05}segment'

  curveObject = {}

  for curveElement in xmlObject.findall(gmCurveEleStr):
    curveId = curveElement.attrib['id']
    segmentElement = curveElement.find(segmentEleStr)
    curveObject[curveId] = [
      pointObject[segmentElement[0][1][0][0][0].attrib['idref']],
      pointObject[segmentElement[0][1][1][0][0].attrib['idref']]
    ]

    curveObject['_' + curveId] = list(reversed(curveObject[curveId]))

  return  curveObject

def createSurfaceObject(xmlObject, curveObject):
  gmSurfaceEleStr = '{http://www.gsi.go.jp/GIS/jpgis/standardSchemas2.1_2009-05}GM_Surface'
  generatorEleStr = '{http://www.gsi.go.jp/GIS/jpgis/standardSchemas2.1_2009-05}generator'

  surfaceObject = {}

  for surfaceElement in xmlObject.findall(gmSurfaceEleStr):
    geometry = []

    for lineRef in surfaceElement[2][0][1][1].findall(generatorEleStr):
      geometry.append(curveObject[lineRef.attrib['idref']][0])

    # SIMA-JPGIS では始点と終点が自動で結ばれるが
    # GIS では始点と終点を同じ点にするため、始点座標をもう一度追加する
    geometry.append(geometry[0])

    surfaceId = surfaceElement.attrib['id']
    surfaceProp = Properties(surfaceId, None, None, None, None, None, None)
    feature = Feature(surfaceProp, [geometry])
    surfaceObject[surfaceId] = feature

  return surfaceObject
