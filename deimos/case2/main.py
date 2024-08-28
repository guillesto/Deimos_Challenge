def printSomeCSVLinesAsJSON(csvAbsPathStr):
    """
    Reads a given csv and prints all its lines in JSON format.
    :param csvAbsPathStr:
    :return:
    """
    import pandas as pd
    import json

    csvAsDF = pd.read_csv(csvAbsPathStr)
    csvAsDctLst = csvAsDF.to_dict(orient="records")
    for csvDct in csvAsDctLst:
        jsonStr = json.dumps(csvDct)
        print(jsonStr)


if __name__ == "__main__":
    import os

    thisModulePathStr = os.path.dirname(__file__)
    lastSlashIndex = thisModulePathStr.rfind("\\")
    csvAbsPathStr = thisModulePathStr[:lastSlashIndex] + "\\input\\reto.csv"

    printSomeCSVLinesAsJSON(csvAbsPathStr)
