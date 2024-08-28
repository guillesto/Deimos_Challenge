import os


def writeLastDates(csvAbsPathStr):
    """
    Creates a file with the last dates of each Matricula sorted descending.
    :param csvAbsPathStr:
    :return:
    """
    import pandas as pd

    csvAsDF = pd.read_csv(csvAbsPathStr)
    uniqueMatriculasStrLst = csvAsDF.Matricula.unique()

    matriculaAndTimeDctLst = []
    for uniqueMatriculasStr in uniqueMatriculasStrLst:
        matriculaDF = csvAsDF[csvAsDF["Matricula"] == uniqueMatriculasStr]
        sortedMatriculaDF = matriculaDF.sort_values(by=["Pos_date"], ascending=[False])
        lastPostDate = sortedMatriculaDF["Pos_date"].iloc[0]
        matriculaAndTimeDctLst.append({"matricula": uniqueMatriculasStr, "lastDate": lastPostDate})

    from operator import itemgetter
    orderedDctLst = sorted(matriculaAndTimeDctLst, key=itemgetter('lastDate'), reverse=True)

    import datetime
    linesStrLst = []
    for orderedDct in orderedDctLst:
        lastDatetime = datetime.datetime.fromtimestamp(orderedDct["lastDate"] / 1000)
        formatedDatetime = lastDatetime.strftime('%d/%m/%Y %H:%M:%S')
        linesStrLst.append("Matricula: " + orderedDct["matricula"] + "; lastDatetime: " + str(formatedDatetime))

    outputPath = os.path.dirname(__file__) + "\\dates.txt"
    with open(outputPath, "a") as file:
        for i in range(len(linesStrLst)):
            file.write(linesStrLst[i] + "\n")


if __name__ == "__main__":
    thisModulePathStr = os.path.dirname(__file__)
    lastSlashIndex = thisModulePathStr.rfind("\\")
    csvAbsPathStr = thisModulePathStr[:lastSlashIndex] + "\\input\\reto.csv"

    writeLastDates(csvAbsPathStr)
