filepath = 'input.txt'


program_listing = []


def load_listing():
    file = open(filepath)
    text = file.readline()
    index_count = 0
    index_old = 0

    for i in range(0, len(text)):
        if text[i] == ',':
            program_listing.append(int(text[index_old:i]))
            index_old = i+1
            index_count += 1   

    program_listing.append(int(text[index_old:len(text)]))
    index_count += 1 


def opcode_1(PC: int):
    # indirect addressing:
    #   each parameter of opcode (3 next cells) holds adress to:
    #       1st param - A value
    #       2nd param - B value
    #       3rd param - result of A + B
    # for some reason this makes more sense to me than assigning each value to different variable
    program_listing [ program_listing [PC+3] ] = program_listing [ program_listing [PC+1] ] + program_listing [ program_listing [PC+2] ] 


def opcode_2(PC: int):
    # indirect addressing:
    #   each parameter of opcode (3 next cells) holds adress to:
    #       1st param - A value
    #       2nd param - B value
    #       3rd param - result of A * B
    # for some reason this makes more sense to me than assigning each value to different variable
    program_listing [ program_listing [PC+3] ] = program_listing [ program_listing [PC+1] ] * program_listing [ program_listing [PC+2] ] 


def opcode_99():
    print('\n\tTHE END')
    print('\n\tLeft at position 0: {}\n\n'.format(program_listing[0]))



def task_1():
    program_listing[1] = 12
    program_listing[2] = 2
    for i in range(0, len(program_listing), 4):
        if program_listing[i] == 1:
            opcode_1(i)
        elif program_listing[i] == 2:
            opcode_2(i)
        elif program_listing[i] == 99:
            break
        else:
            print('Wrong opcode on index {}!'.format(i))
    opcode_99()


if __name__ == '__main__':
    load_listing()
    task_1()