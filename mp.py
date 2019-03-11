from numpy import zeros, ones, vstack, arange
from numpy.linalg import lstsq

DIM_Y = 10
DIM_X = 10

def getx(x):
    return int(DIM_X / 2) + x

def gety(y):
    return -(int(DIM_Y / 2) + y + 1) % DIM_Y 

grid = zeros((DIM_Y, DIM_X))

# https://stackoverflow.com/questions/21565994/method-to-return-the-equation-of-a-straight-line-given-two-points

def drawpath(x1, y1, x2, y2):
    points = [(x1,y1),(x2,y2)]
    x_coords, y_coords = zip(*points)
    A = vstack([x_coords,ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords, rcond=1)[0]
    '''
    FutureWarning: `rcond` parameter will change to the default of machine precision times ``max(M, N)`` where M and N are the input matrix dimensions.
    To use the future default and silence this warning we advise to pass `rcond=None`, to keep using the old, explicitly pass `rcond=-1`.
    '''

    for x in arange(x1, x2, 0.1): # with granularity of 0.1
        grid[gety(int(round(m*x + c)))][getx(int(x))] = 1
        # print(int(x), int(round(m*x + c) ))

# MP proper
drawpath(0, 0, 5, 5)
drawpath(4, 0, 5, 5)
drawpath(0, 0, 4, 0)

print(grid)
