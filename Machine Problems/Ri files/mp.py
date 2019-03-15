import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imresize
import cv2
from read import *

def plot_polygon(coord):
    coord.append(coord[0]) #repeat the first point to create a 'closed loop'
    xs, ys = zip(*coord) #create lists of x and y values
    plt.plot(xs,ys, linewidth=5) 

def plot_point(x, y):
    plt.scatter(x, y, s=10)

start, goal, shapes = read_input('in.txt')

plt.figure()
plt.xlim(0, 200)
plt.ylim(0, 100)

plt.gca().invert_yaxis()

for shape in shapes:
    plot_polygon(shape)

plot_point(start[0], start[1])
plot_point(goal[0], goal[1])
plot_point(0, 0)
plot_point(10, 10)
plot_point(20, 20)
# plt.show()

plt.plot(100, 200) # to ensure dimensions are 100,200
plt.axis('off')
plt.tick_params(axis='both', left=False, top=False, right=False, bottom=False, labelleft=False, labeltop=False,
                    labelright=False, labelbottom=False)
plt.savefig('maze.png', bbox_inches='tight', transparent=True, pad_inches=0)

plt.show()
plt.clf() 

img = cv2.imread('maze.png', cv2.IMREAD_GRAYSCALE)
light = cv2.resize(img, (200, 100))

plt.axis('off')
plt.tick_params(axis='both', left=False, top=False, right=False, bottom=False, labelleft=False, labeltop=False,
                        labelright=False, labelbottom=False)

plt.tight_layout(pad=0)
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


grid = grid.tolist()

plt.show()
