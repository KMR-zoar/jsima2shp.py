from shapefile import shapefile

def createShapefile(chibanObject, path):
  shpPath = path.replace('.xml', '')

  shpWriter = shapefile.Writer(shpPath, shapeType=5)
  shpWriter.field('surfaceID','C', 15)
  shpWriter.field('kakuchiID', 'C', 15)
  shpWriter.field('chibanID', 'C', 15)
  shpWriter.field('chiban', 'C', 250)
  shpWriter.field('OAza', 'C', 50)
  shpWriter.field('Aza', 'C', 50)
  shpWriter.field('Area', 'C', 50)

  for chibanId in  chibanObject.keys():
    shpWriter.poly(chibanObject[chibanId].geometry)

    properties = chibanObject[chibanId].properties
    shpWriter.record(
      properties.surfaceId,
      properties.kakuchiId,
      properties.chibanId,
      properties.chiban,
      properties.OAza,
      properties.Aza,
      properties.Area
    )

  shpWriter.close()

  return True