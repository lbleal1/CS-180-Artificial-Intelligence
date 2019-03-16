import matplotlib.pyplot as plt
from scipy.misc import imresize
import numpy as np
import cv2
import time

from read import *
from astar import Node, astar

TEST_CASE = 5

def plot_polygon(coord):
    coord.append(coord[0]) #repeat the first point to create a 'closed loop'
    xs, ys = zip(*coord) #create lists of x and y values
    plt.plot(ys, xs, linewidth=5) 

def plot_point(x, y):
    plt.scatter(x, y, s=10)

startNode, goalNode, shapes = read_input('in'+ str(TEST_CASE) + '.txt')
print(shapes)

plt.figure()
plt.xlim(0, 200)
plt.ylim(0, 100)

plt.gca().invert_yaxis()

for shape in shapes:
    plot_polygon(shape)

# plt.show()

plt.plot(100, 200) # to ensure dimensions are 100,200
plt.axis('off')
plt.tick_params(axis='both', left=False, top=False, right=False, bottom=False, labelleft=False, labeltop=False,
                    labelright=False, labelbottom=False)
plt.savefig('maze'+ str(TEST_CASE) + '.png', bbox_inches='tight', transparent=True, pad_inches=0)

# plt.show()
plt.clf() 


img = cv2.imread('maze'+ str(TEST_CASE) + '.png', cv2.IMREAD_GRAYSCALE)
light = cv2.resize(img, (200, 100))

# plt.axis('off')
plt.tick_params(axis='both', left=False, top=False, right=False, bottom=False, labelleft=False, labeltop=False, labelright=False, labelbottom=False)
plt.tight_layout(pad=0)
imgplot = plt.imshow(img, cmap='Greys_r')

grid = np.zeros((100, 200))
grid = grid.tolist()

for row, row_points in enumerate(light):
    for col, col_val in enumerate(row_points):
        if col_val < 255:
            # print("found a color")
            grid[row][col] = int(1)
        else:
            grid[row][col] = int(0)

start = time.time()
path, expandedNodes = astar(grid, startNode, goalNode)
end = time.time()

plt.clf()

img = cv2.imread('maze'+ str(TEST_CASE) + '.png', cv2.IMREAD_GRAYSCALE)
light = cv2.resize(img, (200, 100))

plt.xlim(0, 200)
plt.ylim(0, 100)


plt.gca().invert_yaxis()

for shape in shapes:
    plot_polygon(shape)


for point in path:
    plot_point(point[1], point[0])

plot_point(12, 140)

# plt.axis('off')
# cplt.tick_params(axis='both', left=False, top=False, right=False, bottom=False, labelleft=False, labeltop=False, labelright=False, labelbottom=False)
plt.tight_layout(pad=0)
plt.savefig('maze'+ str(TEST_CASE) + '_sol.png')
plt.show()


print("starting point:", startNode)
print("goal point:", goalNode)
print("solution Path:",path)
print("cost of the solution:", len(path))
print("number of expanded nodes:",expandedNodes)
end = time.time()
print("actual running time of the program:", end - start)
