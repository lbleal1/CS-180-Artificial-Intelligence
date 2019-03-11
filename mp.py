from numpy import zeros, ones, vstack, arange
from numpy.linalg import lstsq

DIM_Y = 20
DIM_X = 20

def getx(x):
    return int(DIM_X / 2) + x

def gety(y):
    return -(int(DIM_Y / 2) + y + 1) % DIM_Y 

grid = zeros((DIM_Y, DIM_X))
print(grid)
# https://stackoverflow.com/questions/21565994/method-to-return-the-equation-of-a-straight-line-given-two-points

points = [(0,0),(2,7)]
x_coords, y_coords = zip(*points)
A = vstack([x_coords,ones(len(x_coords))]).T
m, c = lstsq(A, y_coords)[0]

for x in arange(0, 2, 0.1): # with granularity of 0.1
    grid[gety(int(round(m*x + c)))][getx(int(x))] = 1
    print(int(x), int(round(m*x + c) ))
    #print(getx(x), gety(int(round(m*x + c) ) ) )
    #print(1)

print(grid)


'''
for x in grid[x]:
    for y in grid[x][y]:
        grid[x][y] = 0

for x in grid[x]:
    for y in grid[x][y]:
        print(grid[x][y])
'''