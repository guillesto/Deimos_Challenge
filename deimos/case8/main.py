from flask import Flask, request
import mysql.connector

app = Flask(__name__)


def _getLastDateTimeFromDB(matriculaStr):
    """
    Returns the last datetime of a given matriculaStr
    :param matriculaStr:
    :return:
    """
    thisMPS = "#@ main:_getLastDateTimeFromDB:"

    queryStr = "SELECT lastDatetime from vehicles WHERE matricula = %s" \
               "ORDER BY id DESC LIMIT 1"

    try:
        myConnection = mysql.connector.connect(user="user", password="password", host="127.0.0.1",
                                               database="mydb")
        myCursor = myConnection.cursor()
        myCursor.execute(queryStr, (matriculaStr,))
        latestDateTime = myCursor.fetchone()[0]
        myConnection.close()
        return latestDateTime

    except Exception as exc:
        print(thisMPS,
              "**Warning! Error while retrieving some matricula lastDatetime. Returning empty String. Exception:",
              str(exc))
        return ""


def _returnLastMatriculaDatetime(matriculaStr):
    """
    Given some matricula as String, returns the last datetime if found, else returns empty String.
    :param matriculaStr:
    :return:
    """
    thisMPS = "#@ main:_returnLastMatriculaDatetime:"

    outputPath = os.path.dirname(__file__) + "\\dates.txt"

    with open(outputPath, "r") as file:
        linesStrLst = file.readlines()

    try:
        for linesStr in linesStrLst:
            if matriculaStr in linesStr:
                return linesStr.split("lastDatetime:")[1].strip()

        return ""

    except Exception as exc:
        print(thisMPS, "**Warning! Error retrieving some matricula last datetime. Returning empty String. Exception:",
              str(exc))


@app.route('/', methods=['GET'])
def getLastDateOfMatricula():
    if not "id" in request.args:
        return "ID not specified. Please use format '?id=XXX'"

    matriculaStr = str(request.args["id"])
    lastDatetime = _returnLastMatriculaDatetime(matriculaStr)

    if lastDatetime == "":
        return "Matricula not found"
    else:
        return lastDatetime
