from numpy import zeros, ones, vstack
from numpy.linalg import lstsq


DIM_Y = 10
DIM_X = 20


def getx(x):
    return int(DIM_Y / 2) + x - 1

def gety(y):
    return int(DIM_X / 2) + y - 1

grid = zeros((DIM_Y, DIM_X))
print(grid)
# https://stackoverflow.com/questions/21565994/method-to-return-the-equation-of-a-straight-line-given-two-points

points = [(0,0),(7,6)]
x_coords, y_coords = zip(*points)
A = vstack([x_coords,ones(len(x_coords))]).T
m, c = lstsq(A, y_coords)[0]

for x in range(1, 5):
    grid[gety(int(round(m*x+c)))][getx(x)] = 1
    print(getx(x), gety(int(round(m*x + c) ) ) )

print(grid)
'''



print(getM(-3, 3, 3, -1))

print(gety(1))

#print(A)

'''

'''
for x in grid[x]:
    for y in grid[x][y]:
        grid[x][y] = 0

for x in grid[x]:
    for y in grid[x][y]:
        print(grid[x][y])
'''