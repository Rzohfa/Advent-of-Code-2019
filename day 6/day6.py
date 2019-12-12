import math


orbit_map = []


def load_map(file_path: str):
    with open(file_path) as file:
        line = file.readline()
        while line:
            for i in range(len(line)):
                if line[i] == ')':
                    if line[-1] == '\n':
                        orbit_map.append([line[0:i], line[i+1:-1]])
                    else:
                        orbit_map.append([line[0:i], line[i+1:]])
                    break
            line = file.readline()
    
    #print(*orbit_map, sep='\n')


def task_1():
    num_of_orbits = 0

    for i in range(len(orbit_map)-1, -1, -1):
        planet = orbit_map[i][1]
        while planet != 'COM':
            for j in range(len(orbit_map)-1, -1, -1):
                if orbit_map[j][1] == planet:
                    planet = orbit_map[j][0]
                    num_of_orbits += 1
                    break
        
        procent = math.floor(100*(len(orbit_map)-i)/len(orbit_map))
        print('{}%'.format(procent), end='\r')
    
    print('\n{}'.format(num_of_orbits))


def task_2():
    santa_route = []
    your_route = []
    route_len = -2

    planet = 'SAN'
    while planet != 'COM':
        for j in range(len(orbit_map)-1, -1, -1):
            if orbit_map[j][1] == planet:
                santa_route.append(orbit_map[j][0])
                planet = orbit_map[j][0]
                break
        
    planet = 'YOU'
    while planet != 'COM':
        for j in range(len(orbit_map)-1, -1, -1):
            if orbit_map[j][1] == planet:
                your_route.append(orbit_map[j][0])
                planet = orbit_map[j][0]
                break

    base_planet = []
    for santa_planet in santa_route:
        for your_planet in your_route:
            if your_planet == santa_planet:
                base_planet.append(your_planet)
                break

    planet = 'SAN'
    while planet != base_planet[0]:
        for j in range(len(orbit_map)-1, -1, -1):
            if orbit_map[j][1] == planet:
                route_len += 1
                planet = orbit_map[j][0]
                break

    planet = 'YOU'
    while planet != base_planet[0]:
        for j in range(len(orbit_map)-1, -1, -1):
            if orbit_map[j][1] == planet:
                route_len += 1
                planet = orbit_map[j][0]
                break

    print(route_len)


if __name__ == '__main__':
    load_map('input.txt')
    #task_1()
    task_2()