'''
(0,0)
(175,175)
(10,10),(20,10),(20,20),(10,20),(5,15)
(50,50),(30,50),(30,40)
(100,50),(20,80),(120,80)
'''

import re

def read_input(filename):
    file = open (filename, 'r+', encoding='utf-8')
    point = r'([\d]+,[\d]+)'

    start = tuple(map(int, re.search(point, file.readline())[0].split(',')))
    goal  = tuple(map(int, re.search(point, file.readline())[0].split(',')))

    shapes = []
    for line in file:
        shape = []
        for point_i in re.findall(point, line):
            point_int = map(int, point_i.split(','))
            shape.append(list(point_int))
        # print(shape)
        shapes.append(shape)

    # print(shapes)
    file.close()
    return start, goal, shapes