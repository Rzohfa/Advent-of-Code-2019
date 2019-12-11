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


def find_full_traces(cable: []):
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


def find_trace_len_to_point(cable: [], point: ()):
    trace_len = 0
    loc = [0,0]
    for i in range(0, len(cable)):
        if cable[i][0] == 'U':
            for j in range(0, int(cable[i][1:])):
                loc[1] += 1
                trace_len += 1
                if loc[0] == point[0] and loc[1] == point[1]:
                    #print('to point: {}, {}: {}\n'.format(point[0], point[1], trace_len))
                    return trace_len
        elif cable[i][0] == 'D':
            for j in range(0, int(cable[i][1:])):
                loc[1] -= 1
                trace_len += 1
                if loc[0] == point[0] and loc[1] == point[1]:
                    #print('to point: {}, {}: {}\n'.format(point[0], point[1], trace_len))
                    return trace_len
        elif cable[i][0] == 'L':
            for j in range(0, int(cable[i][1:])):
                loc[0] -= 1
                trace_len += 1
                if loc[0] == point[0] and loc[1] == point[1]:
                    #print('to point: {}, {}: {}\n'.format(point[0], point[1], trace_len))
                    return trace_len
        elif cable[i][0] == 'R':
            for j in range(0, int(cable[i][1:])):
                loc[0] += 1
                trace_len += 1
                if loc[0] == point[0] and loc[1] == point[1]:
                    #print('to point: {}, {}: {}\n'.format(point[0], point[1], trace_len))
                    return trace_len
        
        #return trace_len
    
    return -1


#def find_trace_len_to_point(cable: [], point: int):
#    trace_len = 0
#    
#    for i in range(0, point):
#        trace_len += int(cable[i][1:])
#    
#    print(trace_len)
#    return trace_len


def calc_crossings(trace_1: [], trace_2: [], ij: bool):
    crossings = []
    for i in range(1, len(trace_1)):
        for j in range(1, len(trace_2)):
            if crosses(trace_1[i-1], trace_1[i], trace_2[j-1], trace_2[j]):
                if ij:
                    crossings.append([1, trace_1[i][0], trace_2[j][1]])
                else:
                    crossings.append([trace_1[i][0], trace_2[j][1]])

    for i in range(1, len(trace_2)):
        for j in range(1, len(trace_1)):
            if crosses(trace_2[i-1], trace_2[i], trace_1[j-1], trace_1[j]):
                if ij:
                    crossings.append([2, trace_2[i][0], trace_1[j][1]])
                else:
                    crossings.append([trace_2[i][0], trace_1[j][1]])

    ### DEBUG ###

    #print(crossings)        

    return crossings


#def calc_crossings(trace_1: [], trace_2: [], ij: bool):
#    crossings = []
#    for i in range(1, len(trace_1)):
#        for j in range(1, len(trace_2)):
#            if crosses(trace_1[i-1], trace_1[i], trace_2[j-1], trace_2[j]):
#                if ij:
#                    crossings.append([1, i, j])
#                else:
#                    crossings.append([trace_1[i][0], trace_2[j][1]])
#
#    for i in range(1, len(trace_2)):
#        for j in range(1, len(trace_1)):
#            if crosses(trace_2[i-1], trace_2[i], trace_1[j-1], trace_1[j]):
#                if ij:
#                    crossings.append([2, i, j])
#                else:
#                    crossings.append([trace_2[i][0], trace_1[j][1]])
#
#    ### DEBUG ###
#
#    #print(crossings)        
#
#    return crossings


def task_1():
    trace_cable_1 = find_full_traces(cable_1)
    trace_cable_2 = find_full_traces(cable_2)

    crossings = calc_crossings(trace_cable_1, trace_cable_2, False)
        
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
    trace_cable_1 = find_full_traces(cable_1)
    trace_cable_2 = find_full_traces(cable_2)

    crossings = calc_crossings(trace_cable_1, trace_cable_2, True)

    lengths = []

    for cross in crossings:
        if cross[0] == 1:
            lengths.append(find_trace_len_to_point(cable_1, (cross[1], cross[2])) + find_trace_len_to_point(cable_2, (cross[1], cross[2])))
        elif cross[0] == 2:
            lengths.append(find_trace_len_to_point(cable_2, (cross[1], cross[2])) + find_trace_len_to_point(cable_1, (cross[1], cross[2])))

    #print(lengths)

    ret = 0
    for i in range(0, len(lengths)):
        if lengths[i] < lengths[ret]:
            ret = i

    print(lengths[ret])


if __name__ == '__main__':
    load_cables()
    #task_1()
    task_2()


#def find_full_traces(cable: []):
#    trace = []
#    trace.append([0,0])
#    for i in range(0, len(cable)):
#        if cable[i][0] == 'U':
#            trace.append([trace[i][0], trace[i][1]+int(cable[i][1:])])
#        elif cable[i][0] == 'D':
#            trace.append([trace[i][0], trace[i][1]-int(cable[i][1:])])
#        elif cable[i][0] == 'L':
#            trace.append([trace[i][0]-int(cable[i][1:]), trace[i][1]])
#        elif cable[i][0] == 'R':
#            trace.append([trace[i][0]+int(cable[i][1:]), trace[i][1]])
#
#    ### DEBUG PRINTS ###
#
#    #print('trace cable 1')
#    #for i in trace_cable_1:
#    #    print(i)
#    #print('trace cable 2')
#    #for i in trace_cable_2:
#    #    print(i)
#
#    return trace
#

#
#
#def task_1():
#    trace_cable_1 = find_full_traces(cable_1)
#    trace_cable_2 = find_full_traces(cable_2)
#
#    crossings = calc_crossings(trace_cable_1, trace_cable_2, False)
#        
#    lengths = []
#    for cross in crossings:
#        lengths.append(abs(cross[0])+abs(cross[1]))
#    
#    ### DEBUG PRINTS ###
#
#    #print (lengths)
#    #print(crossings)
#
#    res = 0
#    for i in range(0, len(lengths)):
#        if lengths[i] < lengths[res]:
#            res = i
#
#    print(lengths[res])
#
#
#def task_2():
#    trace_cable_1 = find_full_traces(cable_1)
#    trace_cable_2 = find_full_traces(cable_2)
#
#    crossings = calc_crossings(trace_cable_1, trace_cable_2, True)
#
#    lengths = []
#
#    for cross in crossings:
#        if cross[0] == 1:
#            lengths.append(find_trace_len_to_point(cable_1, cross[0]) + find_trace_len_to_point(cable_2, cross[1]))
#        elif cross[0] == 2:
#            lengths.append(find_trace_len_to_point(cable_2, cross[0]) + find_trace_len_to_point(cable_1, cross[1]))
#
#    ret = 0
#    for i in range(0,len(lengths)):
#        if lengths[i] < lengths[ret]:
#            ret = i
#
#    print(lengths[i])
#
#