def createKakuchiObject(xmlObject, surfaceObject):
  kakuchiEleStr = '{http://www.jsima.or.jp/JSIMASchema/201206}Kakuchi'
  chibanEleStr = '{http://www.jsima.or.jp/JSIMASchema/201206}Name'
  surfaceRefStr = '{http://www.jsima.or.jp/JSIMASchema/201206}RefSurface'

  kakuchiObject = {}

  for kakuchiElement in xmlObject.findall(kakuchiEleStr):
    kakuchiId = kakuchiElement.attrib['id']
    surfaceRefId = kakuchiElement.find(surfaceRefStr).attrib['idref']
    kakuchiObject[kakuchiId] = surfaceObject[surfaceRefId]
    kakuchiObject[kakuchiId]['properties']['kakuchiId'] = kakuchiId
    kakuchiObject[kakuchiId]['properties']['chiban'] = kakuchiElement.find(chibanEleStr).text

  return kakuchiObject

def createChibanObject(xmlObject, kakuchiObject):
  chibanEleStr = '{http://www.jsima.or.jp/JSIMASchema/201206}Chiban'
  oazaEleStr = '{http://www.jsima.or.jp/JSIMASchema/201206}OAza'
  azaEleStr = '{http://www.jsima.or.jp/JSIMASchema/201206}Aza'
  areaEleStr = '{http://www.jsima.or.jp/JSIMASchema/201206}Area'
  kakuchiRefStr = '{http://www.jsima.or.jp/JSIMASchema/201206}RefKakuchi'

  chibanObject = {}

  for chibanElement in xmlObject.findall(chibanEleStr):
    chibanId = chibanElement.attrib['id']
    kakuchiRefId = chibanElement.find(kakuchiRefStr).attrib['idref']
    chibanObject[chibanId] = kakuchiObject[kakuchiRefId]

    oazaElement = chibanElement.find(oazaEleStr)
    chibanObject[chibanId]['properties']['OAza'] = oazaElement.text if oazaElement != None else None

    azaElement = chibanElement.find(azaEleStr)
    chibanObject[chibanId]['properties']['Aza'] = azaElement.text if azaElement != None else None

    areaElement = chibanElement.find(areaEleStr)
    chibanObject[chibanId]['properties']['Area'] = areaElement.text if areaElement != None else None
    chibanObject[chibanId]['properties']['chibanId'] = chibanId

  return chibanObject
