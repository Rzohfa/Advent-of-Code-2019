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

    return result


def task2():

    filepath = 'input.txt'
    result = 0

    with open(filepath) as file:
        lineText = file.readline()
        while lineText:
            tempResult = int(lineText)
            while tempResult > 0:
                tempResult = math.floor(tempResult/3)
                tempResult -= 2
                result += tempResult
            result -= tempResult
            lineText = file.readline()

    return result


if __name__ == '__main__':
    print('Task 1:')
    print("\t{}\n".format(task1()))
    print('Task 2:')
    print("\t{}\n".format(task2()))