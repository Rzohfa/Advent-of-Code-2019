import math


file_path = 'input.txt'


def task_1():

    result = 0

    with open(file_path) as file:
        line_text = file.readline()
        while line_text:
            temp_result = int(line_text)
            temp_result = math.floor(temp_result/3)
            temp_result -= 2
            result += temp_result
            line_text = file.readline()

    return result


def task_2():

    result = 0

    with open(file_path) as file:
        line_text = file.readline()
        while line_text:
            temp_result = int(line_text)
            while temp_result > 0:
                temp_result = math.floor(temp_result/3)
                temp_result -= 2
                result += temp_result
            result -= temp_result
            line_text = file.readline()

    return result


if __name__ == '__main__':
    print('Task 1:')
    print("\t{}\n".format(task_1()))
    print('Task 2:')
    print("\t{}\n".format(task_2()))