import shutil

projNames = {
  "1": "6669.prj",
  "2": "6670.prj",
  "3": "6671.prj",
  "4": "6672.prj",
  "5": "6673.prj",
  "6": "6674.prj",
  "7": "6675.prj",
  "8": "6676.prj",
  "9": "6677.prj",
  "10": "6678.prj",
  "11": "6679.prj",
  "12": "6680.prj",
  "13": "6681.prj",
  "14": "6682.prj",
  "15": "6683.prj",
  "16": "6684.prj",
  "17": "6685.prj",
  "18": "6686.prj",
  "19": "6687.prj",
}

def copyProjFile(coodSystem, path):
  projPath = path.replace(".xml", ".prj")
  shutil.copyfile('./proj/' + projNames[coodSystem], projPath)

  return True
