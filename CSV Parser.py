# csv reader
import csv


def findVal(row, col, csv_file):
    with open(csv_file) as file:
        csv_reader = csv.reader(file, delimiter=',')
        rowCount = 0
        for curRow in csv_reader:
            if (rowCount == row):
                return (curRow[col])

            rowCount = rowCount + 1


# only works from Q1 - 19
def findQuestionValue(recordVal, question, csv):
    if question <= 5:
        return findVal(recordVal + 1, question - 1, csv)
    elif question == 6:
        retVal = findVal(1, 5, csv) + ": " + findVal(recordVal + 1, 5, csv)
        retVal = retVal + "\n" + findVal(1, 6, csv) + ": " + findVal(recordVal + 1, 6, csv)
        retVal = retVal + "\n" + findVal(1, 7, csv) + ": " + findVal(recordVal + 1, 7, csv)
        retVal = retVal + "\n" + findVal(1, 8, csv) + ": " + findVal(recordVal + 1, 8, csv)
        return retVal
    elif question == 7 or question == 8:
        return findVal(recordVal + 1, question + 2, csv)
    elif question == 9:
        return multiCellFindVal(recordVal, 9 - 1, 9 + 15, csv)


def multiCellFindVal(recordVal, StartCol, EndCol, csv):
    retVal = " "
    for x in range(StartCol, EndCol):
        retVal = retVal + findVal(1, x, csv) + ": " + findVal(recordVal + 1, x, csv) + "\n"
    return retVal
