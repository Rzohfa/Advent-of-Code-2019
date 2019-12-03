import math


def task1():

    filepath = 'input.txt'
    result = 0

    with open(filepath) as file:
        lineText = file.readline()
        while lineText:
            tempResult = int(lineText)
            tempResult = math.floor(tempResult/3)
            tempResult -= 2
            result += tempResult
            lineText = file.readline()

    print(result)