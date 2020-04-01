import csv


def getCSVData(filename):
    dataList = []
    csvFile = open(filename, "r")
    readcsv = csv.reader(csvFile)

    # skip the headers
    next(readcsv)

    for row in readcsv:
        dataList.append(row)
    return dataList