import math


filepath = 'input.txt'
#filepath = 'ex1.txt'


cable_1 = []
cable_2 = []


def load_cables():
    file = open(filepath)
    text = file.readline()
    index_old = 0

    for i in range(0, len(text)):
        if text[i] == ',':
            cable_1.append(text[index_old:i])
            index_old = i+1

    cable_1.append(text[index_old:len(text)-1])
    text = file.readline()
    index_old = 0

    for i in range(0, len(text)):
        if text[i] == ',':
            cable_2.append(text[index_old:i])
            index_old = i+1

    cable_2.append(text[index_old:len(text)])


def crosses(a1: [], a2: [], b1: [], b2: []):
    if a1[0] > b1[0] and a1[0] < b2[0]:
        if a2[0] > b1[0] and a2[0] < b2[0]:
            if b1[1] > a1[1] and b1[1] < a2[1]:
                if b1[1] > a1[1] and b1[1] < a2[1]:
                    return True

    if a1[0] < b1[0] and a1[0] > b2[0]:
        if a2[0] < b1[0] and a2[0] > b2[0]:
            if b1[1] < a1[1] and b1[1] > a2[1]:
                if b1[1] < a1[1] and b1[1] > a2[1]:
                    return True

    if a1[0] > b1[0] and a1[0] < b2[0]:
        if a2[0] > b1[0] and a2[0] < b2[0]:
            if b1[1] < a1[1] and b1[1] > a2[1]:
                if b1[1] < a1[1] and b1[1] > a2[1]:
                    return True

    if a1[0] < b1[0] and a1[0] > b2[0]:
        if a2[0] < b1[0] and a2[0] > b2[0]:
            if b1[1] > a1[1] and b1[1] < a2[1]:
                if b1[1] > a1[1] and b1[1] < a2[1]:
                    return True    

    return False


def find_traces(cable: []):
    trace = []
    trace.append([0,0])
    for i in range(0, len(cable)):
        if cable[i][0] == 'U':
            trace.append([trace[i][0], trace[i][1]+int(cable[i][1:])])
        elif cable[i][0] == 'D':
            trace.append([trace[i][0], trace[i][1]-int(cable[i][1:])])
        elif cable[i][0] == 'L':
            trace.append([trace[i][0]-int(cable[i][1:]), trace[i][1]])
        elif cable[i][0] == 'R':
            trace.append([trace[i][0]+int(cable[i][1:]), trace[i][1]])

    ### DEBUG PRINTS ###

    #print('trace cable 1')
    #for i in trace_cable_1:
    #    print(i)
    #print('trace cable 2')
    #for i in trace_cable_2:
    #    print(i)

    return trace


def calc_crossings(trace_1: [], trace_2: []):
    crossings = []
    for i in range(1, len(trace_1)):
        for j in range(1, len(trace_2)):
            if crosses(trace_1[i-1], trace_1[i], trace_2[j-1], trace_2[j]):
                crossings.append([trace_1[i][0], trace_2[j][1]])

    for i in range(1, len(trace_2)):
        for j in range(1, len(trace_1)):
            if crosses(trace_2[i-1], trace_2[i], trace_1[j-1], trace_1[j]):
                crossings.append([trace_2[i][0], trace_1[j][1]])

    ### DEBUG ###

    #print(crossings)        

    return crossings


def task_1():
    trace_cable_1 = find_traces(cable_1)
    trace_cable_2 = find_traces(cable_2)

    crossings = calc_crossings(trace_cable_1, trace_cable_2)
        
    lengths = []
    for cross in crossings:
        lengths.append(abs(cross[0])+abs(cross[1]))
    
    ### DEBUG PRINTS ###

    #print (lengths)
    #print(crossings)

    res = 0
    for i in range(0, len(lengths)):
        if lengths[i] < lengths[res]:
            res = i

    print(lengths[res])


def task_2():
    pass


if __name__ == '__main__':
    load_cables()
    task_1()