program_listing = []

# Loads listing
def load_listing(filepath: str):
    file = open(filepath)
    text = file.readline()
    index_old = 0

    for i in range(0, len(text)):
        if text[i] == ',':
            program_listing.append(int(text[index_old:i]))
            index_old = i+1

    #print(program_listing[255] + program_listing[6])

    program_listing.append(int(text[index_old:len(text)])) 

# Addition
def opcode_1(PC: int, imm_1: bool, imm_2: bool, imm_3: bool):
    # indirect addressing:
    #   each parameter of opcode (3 next cells) holds adress to:
    #       1st param - A value
    #       2nd param - B value
    #       3rd param - result of A + B
    # for some reason this makes more sense to me than assigning each value to different variable and doing whole operation in steps
    if imm_1:
        param_1 = int(program_listing[PC+1])
    else:
        param_1 = int(program_listing [ program_listing [PC+1] ])
    if imm_2:
        param_2 = int(program_listing[PC+2])
    else:
        param_2 = int(program_listing [ program_listing [PC+2] ])
    if imm_3:
        param_3 = int(program_listing[PC+3])
    else:
        param_3 = int(program_listing [ program_listing [PC+3] ])
    #print('{}, {}, {}'.format(imm_1,imm_2,imm_3))
    program_listing [ program_listing [PC+3] ] = param_1 + param_2

# Multiply
def opcode_2(PC: int, imm_1: bool, imm_2: bool, imm_3: bool):
    # indirect addressing:
    #   each parameter of opcode (3 next cells) holds adress to:
    #       1st param - A value
    #       2nd param - B value
    #       3rd param - result of A * B
    # for some reason this makes more sense to me than assigning each value to different variable and doing whole operation in steps

    if imm_1:
        param_1 = int(program_listing[PC+1])
    else:
        param_1 = int(program_listing [ program_listing [PC+1] ])
    if imm_2:
        param_2 = int(program_listing[PC+2])
    else:
        param_2 = int(program_listing [ program_listing [PC+2] ])
    if imm_3:
        param_3 = int(program_listing[PC+3])
    else:
        param_3 = int(program_listing [ program_listing [PC+3] ])
    #print('{}, {}, {}'.format(imm_1,imm_2,imm_3))
    program_listing [ program_listing [PC+3] ] = param_1 * param_2

# EOP
def opcode_99(fancy_output: bool):
    # End of program
    if fancy_output:
        print('\n\tTHE END')
        print('\n\tOutput: {}\n\n'.format(program_listing[0]))
    return program_listing[0]

# Input
def opcode_3(PC: int, imm_1: bool):
    # input from user
    print('Waiting for input:')
    user_input = input()
    program_listing[ program_listing[PC+1] ] = user_input

# Output
def opcode_4(PC: int, imm_1: bool):
    if(imm_1):
        output = program_listing[PC+1]
    else:
        output = program_listing[ program_listing[PC+1] ]
    #print('output @ {}: {}, @PC+1 was {}, @[PC+1] was {}'.format(PC+1, output, program_listing[PC+1], program_listing[ program_listing[PC+1] ]))
    print('output @ {}: {}'.format(PC, output))

# Jmp if true
def opcode_5(PC: int, imm_1: bool, imm_2: bool):
    # Jump if true
    if imm_1:
        param_1 = int(program_listing[PC+1])
    else:
        param_1 = int(program_listing [ program_listing [PC+1] ])
    if imm_2:
        param_2 = int(program_listing[PC+2])
    else:   
        param_2 = int(program_listing [ program_listing [PC+2] ])

    if param_1 != 0:
        return param_2
    else:
        return PC+3

# Jmp if false
def opcode_6(PC: int, imm_1: bool, imm_2: bool):
    # Jump if false
    if imm_1:
        param_1 = int(program_listing[PC+1])
    else:
        param_1 = int(program_listing [ program_listing [PC+1] ])
    if imm_2:
        param_2 = int(program_listing[PC+2])
    else:   
        param_2 = int(program_listing [ program_listing [PC+2] ])

    if param_1 == 0:
        return param_2
    else:
        return PC+3

# Less
def opcode_7(PC: int, imm_1: bool, imm_2: bool, imm_3: bool):
    # Less than
    if imm_1:
        param_1 = int(program_listing[PC+1])
    else:
        param_1 = int(program_listing [ program_listing [PC+1] ])
    if imm_2:
        param_2 = int(program_listing[PC+2])
    else:
        param_2 = int(program_listing [ program_listing [PC+2] ])
    if imm_3:
        param_3 = int(program_listing[PC+3])
    else:
        param_3 = int(program_listing [ program_listing [PC+3] ])
    if param_1 < param_2:
        program_listing[ program_listing [PC+3] ] = 1
    else:
        program_listing[ program_listing [PC+3] ] = 0

# Equals
def opcode_8(PC: int, imm_1: bool, imm_2: bool, imm_3: bool):
    # Equals
    if imm_1:
        param_1 = int(program_listing[PC+1])
    else:
        param_1 = int(program_listing [ program_listing [PC+1] ])
    if imm_2:
        param_2 = int(program_listing[PC+2])
    else:
        param_2 = int(program_listing [ program_listing [PC+2] ])
    if imm_3:
        param_3 = int(program_listing[PC+3])
    else:
        param_3 = int(program_listing [ program_listing [PC+3] ])
    if param_1 == param_2:
        program_listing[ program_listing [PC+3] ] = 1
    else:
        program_listing[ program_listing [PC+3] ] = 0

# Main loop
def intcode_computer(fancy_output: bool):
    i = 0
    #print('len: {}'.format(program_listing.count))
    while i < len(program_listing):
        #print('{}: {}'.format(i, program_listing[i]))
        imm_1 = False
        imm_2 = False
        imm_3 = False
        if len(str(program_listing[i])) > 1:
            instruction = str(program_listing[i])
            if int(instruction[-1:]) == 1:
                for j in range(3,len(instruction)+1):
                    if j-3 == 0 and int(instruction[-j]) == 1:
                        imm_1 = True
                    if j-3 == 1 and int(instruction[-j]) == 1:
                        imm_2 = True
                    if j-3 == 2 and int(instruction[-j]) == 1:
                        imm_3 = True
                opcode_1(i, imm_1, imm_2, imm_3)
                i += 4
            elif int(instruction[-1:]) == 2:
                for j in range(3,len(instruction)+1):
                    if j-3 == 0 and int(instruction[-j]) == 1:
                        imm_1 = True
                    if j-3 == 1 and int(instruction[-j]) == 1:
                        imm_2 = True
                    if j-3 == 2 and int(instruction[-j]) == 1:
                        imm_3 = True
                opcode_2(i, imm_1, imm_2, imm_3)
                i += 4
            elif int(instruction[-1:]) == 3:
                for j in range(3,len(instruction)+1):
                    if j-3 == 0 and int(instruction[-j]) == 1:
                        imm_1 = True
                opcode_3(i, imm_1)
                i += 2
            elif int(instruction[-1:]) == 4:
                for j in range(3,len(instruction)+1):
                    if j-3 == 0 and int(instruction[-j]) == 1:
                        imm_1 = True
                opcode_4(i, imm_1)
                i += 2
            elif int(instruction[-1:]) == 5:
                for j in range(3,len(instruction)+1):
                    if j-3 == 0 and int(instruction[-j]) == 1:
                        imm_1 = True
                    if j-3 == 1 and int(instruction[-j]) == 1:
                        imm_2 = True
                i = opcode_5(i, imm_1, imm_2)
            elif int(instruction[-1:]) == 6:
                for j in range(3,len(instruction)+1):
                    if j-3 == 0 and int(instruction[-j]) == 1:
                        imm_1 = True
                    if j-3 == 1 and int(instruction[-j]) == 1:
                        imm_2 = True
                i = opcode_6(i, imm_1, imm_2)
            elif int(instruction[-1:]) == 7:
                for j in range(3,len(instruction)+1):
                    if j-3 == 0 and int(instruction[-j]) == 1:
                        imm_1 = True
                    if j-3 == 1 and int(instruction[-j]) == 1:
                        imm_2 = True
                    if j-3 == 2 and int(instruction[-j]) == 1:
                        imm_3 = True
                opcode_7(i, imm_1, imm_2, imm_3)
                i += 4
            elif int(instruction[-1:]) == 8:
                for j in range(3,len(instruction)+1):
                    if j-3 == 0 and int(instruction[-j]) == 1:
                        imm_1 = True
                    if j-3 == 1 and int(instruction[-j]) == 1:
                        imm_2 = True
                    if j-3 == 2 and int(instruction[-j]) == 1:
                        imm_3 = True
                opcode_8(i, imm_1, imm_2, imm_3)
                i += 4
            elif int(instruction[-2:]) == 99:
                opcode_99(fancy_output)
                break
        elif len(str(program_listing[i])) == 1:
            if program_listing[i] == 1:
                opcode_1(i, False, False, False)
                i+=4
            elif program_listing[i] == 2:
                opcode_2(i, False, False, False)
                i+=4
            elif program_listing[i] == 3:
                opcode_3(i, False)
                i+=2
            elif program_listing[i] == 4:
                opcode_4(i, False)
                i+=2
            elif program_listing[i] == 5:
                opcode_5(i, False, False)
            elif program_listing[i] == 6:
                opcode_6(i, False, False)
            elif program_listing[i] == 7:
                opcode_7(i, False, False, False)
                i+=4
            elif program_listing[i] == 8:
                opcode_8(i, False, False, False)
                i+=4
            else:
                print('Wrong opcode on index {}!'.format(i))
                break
    
    return opcode_99(fancy_output)