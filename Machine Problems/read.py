'''
(0,0)
(175,175)
(10,10),(20,10),(20,20),(10,20),(5,15)
(50,50),(30,50),(30,40)
(100,50),(20,80),(120,80)
'''

import re
filename = 'in.txt'
file = open (filename, 'r+', encoding='utf-8')
point = r'([\d]+,[\d]+)'

start_x, start_y = re.search(point, file.readline())[0].split(',')
goal_x, goal_y = re.search(point, file.readline())[0].split(',')


shapes = []
for line in file:
    shape = []
    for x in re.findall(point, line):
        point_i = map(int, x.split(','))
        shape.append(list(point_i))
    # print(shape)
    shapes.append(shape)

# print(shapes)

file.close()

