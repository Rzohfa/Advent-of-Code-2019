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


def opcode_99(fancy_output: bool):
    if fancy_output:
        print('\n\tTHE END')
        print('\n\tOutput: {}\n\n'.format(program_listing[0]))
    return program_listing[0]


def intcode_computer(fancy_output: bool):
    for i in range(0, len(program_listing), 4):
        if program_listing[i] == 1:
            opcode_1(i)
        elif program_listing[i] == 2:
            opcode_2(i)
        elif program_listing[i] == 99:
            break
        else:
            print('Wrong opcode on index {}!'.format(i))
    return opcode_99(fancy_output)


def task_1(fancy_output: bool):
    load_listing()
    program_listing[1] = 12
    program_listing[2] = 2
    intcode_computer(fancy_output)


def task_2(fancy_output: bool):
    result = ()
    for noun in range(0, 100):
        for verb in range(0, 100):
            load_listing()
            program_listing[1] = noun
            program_listing[2] = verb
            if intcode_computer(fancy_output) == 19690720:
                result = (noun, verb)
                break
            program_listing.clear()
    print(result)
    out = 100 * result[0] + result[1]
    print(out)


if __name__ == '__main__':
    task_1(True)
    task_2(False)