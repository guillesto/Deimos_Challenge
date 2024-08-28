def _getUniqueMatriculasLst(csvAsDctLst):
    """
    Given a csvAsDctLst returns a list with the unique Matriculas
    :param csvAsDctLst:
    :return:
    """
    uniqueMatriculasLst = []
    for csvDct in csvAsDctLst:
        someMatriculaStr = csvDct["Matricula"]
        if someMatriculaStr not in uniqueMatriculasLst:
            uniqueMatriculasLst.append(someMatriculaStr)

    return uniqueMatriculasLst


def printTotalDistances(csvAbsPathStr):
    """
    Reads a given csv and prints the total distances of each vehicle.
    :param csvAbsPathStr:
    :return:
    """
    import pandas as pd

    csvAsDF = pd.read_csv(csvAbsPathStr)
    csvAsDctLst = csvAsDF.to_dict(orient="records")
    uniqueMatriculasStrLst = _getUniqueMatriculasLst(csvAsDctLst)
    for uniqueMatriculasStr in uniqueMatriculasStrLst:
        totalDistance = 0
        for csvDct in csvAsDctLst:
            if csvDct["Matricula"] == uniqueMatriculasStr:
                totalDistance += csvDct["Distance"]

        print("Total distance of", uniqueMatriculasStr + ": ", str(totalDistance))


if __name__ == "__main__":
    import os

    thisModulePathStr = os.path.dirname(__file__)
    lastSlashIndex = thisModulePathStr.rfind("\\")
    csvAbsPathStr = thisModulePathStr[:lastSlashIndex] + "\\input\\reto.csv"

    printTotalDistances(csvAbsPathStr)
