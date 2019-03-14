# start ri imports
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

# end ri imports

from queue import PriorityQueue
from collections import defaultdict 
import time

start = time.time()

expandedNode = []

def addEdge(graph,u,v): 
    graph[u].append(v)

def createGraph(grid):
    #m x n matrix
    rows = len(grid)
    cols = len(grid[0])

    graph = defaultdict(list) 
    for row in range(rows):
        for col in range(cols):
            if col != 0 and grid[row][col]!=1:
                addEdge(graph,(row,col),(row,col-1)) #left
            if col < cols-1 and grid[row][col]!=1:
                addEdge(graph,(row,col),(row,col+1)) #right
            if row != 0 and grid[row][col]!=1:
                addEdge(graph,(row,col),(row-1,col)) #top
            if row < rows-1 and grid[row][col]!=1:
                addEdge(graph,(row,col),(row+1,col)) #bottom
    return graph

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        add = parent[path[-1]]
        path.append(add)
    path.reverse()
    return path
      
def bfs(graph, start, goal):
    parent = {} 
    fringe = [] 
    fringe.append(start) #append starting node
    
    while fringe: #explore til the fringe is not empty!
        node = fringe.pop(0) #get vertex
        expandedNode.append(node) #append the considered vertex to the Expanded Nodes

        print("expanding node")
        if node == goal: #if reaches goal node
            print("REACHED GOAL NODE")
            return backtrace(parent, start, goal)
        for adjacent in graph.get(node, []): #consider the children of the popped node 
            if node not in fringe:     
                if start[0]<=goal[0]:
                  if adjacent[0] >= node[0]:
                    print("parent[adjacent] = node")
                    parent[adjacent] = node  
                if start[0]>=goal[0]:
                    if adjacent[0] <= node[0]:
                      print("parent[adjacent] = node  ")
                      parent[adjacent] = node  
                print("fringe.append(adjacent) ")
                fringe.append(adjacent) 


# START RI
startNode, goalNode, shapes = read_input('in.txt')

plt.figure()
plt.gca().invert_yaxis()

for shape in shapes:
    plot_polygon(shape)

plot_point(startNode)
plot_point(goalNode)

plot_point((100, 200))
plt.axis('off')

plt.savefig('maze.png')

# plt.show()
plt.clf() 

img = cv2.imread('maze.png', cv2.IMREAD_GRAYSCALE)
light = cv2.resize(img, (200, 100))
# light = cv2.resize(img, (20, 20))

plt.axis('off')
imgplot = plt.imshow(img, cmap='Greys_r')
# print(img)
# plt.show()

grid = np.zeros((100, 200))
# grid = np.zeros((20, 20))

for row, row_points in enumerate(light):
    for col, col_val in enumerate(row_points):
        if col_val < 255:
            # print("found a color")
            grid[row][col] = 1

# END RI
for line in grid:
    print(line)

print(grid)
grid = grid.tolist()

for line in grid:
    line = np.matrix(line)
    print(line)

print("original grid is")
print(grid)

print(len(grid))
print(len(grid[0]))
print("starting point:", startNode)
print("goal point:", goalNode)

print (start)

graph = createGraph(grid)  
path=bfs(graph, startNode, goalNode)
print("solution Path:",path)
print("cost of the solution:", len(path))

print("number of expanded nodes:",len(expandedNode))
end = time.time()
print("actual running time of the program:", end - start)