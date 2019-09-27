import codecs
import xml.etree.ElementTree as ET

def readXML(path):
  # SIMAーJPGIS は規格上の文字コードがShift-JISに指定されている
  xmlStream = codecs.open(path, 'r', 'shift_jis', 'ignore')
  xmlString = ''.join(xmlStream)
  xmlData = ET.fromstring(xmlString)

  return xmlData[1]
