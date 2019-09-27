class Properties():
  def __init__(
    self,
    surfaceId,
    kakuchiId,
    chibanId,
    chiban,
    OAza,
    Aza,
    Area
  ):
    self.surfaceId: str = surfaceId
    self.kakuchiId: str = kakuchiId
    self.chibanId: str = chibanId
    self.chiban: str = chiban
    self.OAza: str = OAza
    self.Aza: str = Aza
    self.Area: float = Area


class Feature():
  def __init__(self, properties, geometory):
    self.properties: Properties = properties
    self.geometry: list = geometory
