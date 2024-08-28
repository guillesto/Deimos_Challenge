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


def _getSomeMatriculaDctLst(uniqueMatriculasStr, csvAsDctLst):
    """
    Returns a list of dictionaries of the given uniqueMatriculasStr
    :param uniqueMatriculasStr:
    :param csvAsDctLst:
    :return:
    """
    uniqueMatriculaDctLst = []
    for csvDct in csvAsDctLst:
        if csvDct["Matricula"] == uniqueMatriculasStr:
            uniqueMatriculaDctLst.append(csvDct)

    return uniqueMatriculaDctLst


def printTotalDistancesUsingLatitudeAndLong(csvAbsPathStr):
    """
    Reads a given csv and prints the total distances of each vehicle.
    :param csvAbsPathStr:
    :return:
    """
    import pandas as pd
    import geopy.distance

    csvAsDF = pd.read_csv(csvAbsPathStr)
    csvAsDctLst = csvAsDF.to_dict(orient="records")
    uniqueMatriculasStrLst = _getUniqueMatriculasLst(csvAsDctLst)
    for uniqueMatriculasStr in uniqueMatriculasStrLst:
        totalDistance = 0
        thisMatriculaDctLst = _getSomeMatriculaDctLst(uniqueMatriculasStr, csvAsDctLst)
        for i in range(len(thisMatriculaDctLst) - 1):
            coordinatesStart = (thisMatriculaDctLst[i]["Latitud"], thisMatriculaDctLst[i]["Longitud"])
            coordinatesEnd = (thisMatriculaDctLst[i + 1]["Latitud"], thisMatriculaDctLst[i + 1]["Longitud"])

            totalDistance += geopy.distance.geodesic(coordinatesStart, coordinatesEnd).km

        print("Total distance of", uniqueMatriculasStr + ": ", str(totalDistance), "km")


if __name__ == "__main__":
    import os

    thisModulePathStr = os.path.dirname(__file__)
    lastSlashIndex = thisModulePathStr.rfind("\\")
    csvAbsPathStr = thisModulePathStr[:lastSlashIndex] + "\\input\\reto.csv"

    printTotalDistancesUsingLatitudeAndLong(csvAbsPathStr)
