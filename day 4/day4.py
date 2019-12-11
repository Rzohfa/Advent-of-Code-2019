def task_1(input_low: int, input_high: int):
    answers = []
    for number in range(input_low, input_high+1):
        num_str = str(number)
        adjacent = False
        not_smaller = True
        for i in range(1, len(num_str)):
            if num_str[i] == num_str[i-1]:
                adjacent = True
            elif int(num_str[i]) < int(num_str[i-1]):
                not_smaller = False
        if adjacent and not_smaller:
            answers.append(number)

    print(len(answers))


def task_2(input_low: int, input_high: int):
    answers = []
    for number in range(input_low, input_high+1):
        num_str = str(number)
        adjacent = 0
        not_smaller = True
        for i in range(1, len(num_str)):
            if num_str[i] == num_str[i-1]:
                adjacent +=1
                if i>1 and num_str[i-2] == num_str[i]:
                    adjacent -= 1
                elif i<len(num_str)-1 and num_str[i] == num_str[i+1]:
                    adjacent -= 1
                    
            if int(num_str[i]) < int(num_str[i-1]):
                not_smaller = False
        
        if adjacent > 0 and not_smaller:
            answers.append(number)

    print(len(answers))


if __name__ == '__main__':
    #task_1(153517, 630395)
    task_2(153517, 630395)
    #task_2(122332, 122334)