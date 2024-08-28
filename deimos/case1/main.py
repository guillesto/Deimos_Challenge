import csv


def printSomeCSVLines(csvAbsPathStr):
    """
    Reads a given csv and prints all its lines
    :param csvAbsPathStr:
    :return:
    """
    with open(csvAbsPathStr, "r") as csvFile:
        csvReader = csv.reader(csvFile)
        for row in csvReader:
            print(row)


if __name__ == "__main__":
    import os

    thisModulePathStr = os.path.dirname(__file__)
    lastSlashIndex = thisModulePathStr.rfind("\\")
    csvAbsPathStr = thisModulePathStr[:lastSlashIndex] + "\\input\\reto.csv"

    printSomeCSVLines(csvAbsPathStr)
