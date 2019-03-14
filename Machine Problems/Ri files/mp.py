import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imresize
import cv2
from read import *

def plot_polygon(coord):
    coord.append(coord[0]) #repeat the first point to create a 'closed loop'
    xs, ys = zip(*coord) #create lists of x and y values
    plt.plot(xs,ys, linewidth=10) 

def plot_point(pt):
    plt.scatter(pt[0], pt[1], 30)

def DFS(grid, x_i = None, y_i=None, visited=None):
    visited.append((x_i, y_i))
    element = grid[y_i, x_i]

    if element == 1: return x_i, y_i

    if x_i < 0: 
        print("negative x")
        return
    if x_i > grid.shape[0]: return

    if y_i < 0: 
        print("negative y")
        return
    if y_i > grid.shape[1]: return


start, goal, shapes = read_input('in.txt')

plt.figure()
plt.gca().invert_yaxis()

for shape in shapes:
    plot_polygon(shape)

plot_point(start)
plot_point(goal)

plt.plot(100, 200) # to ensure dimensions are 100,200
plt.axis('off')

plt.savefig('maze.png')

# plt.show()
plt.clf() 

img = cv2.imread('maze.png', cv2.IMREAD_GRAYSCALE)
light = cv2.resize(img, (200, 100))

plt.axis('off')
imgplot = plt.imshow(img, cmap='Greys_r')
# print(img)

grid = np.zeros((100, 200))

for row, row_points in enumerate(light):

    for col, col_val in enumerate(row_points):
        if col_val < 255:
            # print("found a color")
            grid[row][col] = 1


for row in grid:
    print(row)

visited = []
DFS(grid, start[0], start[1], visited)

plt.axis('off')
plt.show()
