from queue import PriorityQueue
from collections import defaultdict 
import time

from read import *
from mp import plot_polygon, plot_point

expandedNode = []


import matplotlib.pyplot as plt
import numpy as np
import cv2

def createStateSpaceGrid(fileName, imgName):
    # read .txt file
    startNode, goalNode, shapes = read_input(fileName) 

    # plot the figure
    plt.figure() 
    plt.xlim(0, 200)
    plt.ylim(0, 100)
    plt.gca().invert_yaxis()

    for shape in shapes:
        plot_polygon(shape) 

    # plot starting and goal points
    #plot_point(startNode) 
    #plot_point(goalNode)

    # save the figure as .png image file
    plt.axis('off')
    plt.tick_params(axis='both', left=False, top=False, right=False, bottom=False, labelleft=False, labeltop=False,
                        labelright=False, labelbottom=False)
    # plt.savefig('maze.png', bbox_inches='tight', transparent=True, pad_inches=0)
    plt.savefig(imgName, bbox_inches='tight', transparent=True, pad_inches=0)
    plt.clf() 
    
    # read the image file and resize to original scale
    img = cv2.imread(imgName, cv2.IMREAD_GRAYSCALE)
    light = cv2.resize(img, (200, 100))
    
    # ensure borderless processing
    plt.axis('off')
    plt.tick_params(axis='both', left=False, top=False, right=False, bottom=False, labelleft=False, labeltop=False,
                            labelright=False, labelbottom=False)
    plt.tight_layout(pad=0)
    
    # convert to grayscale for later for
    # 0s to mean not a point in the polygon obstacle
    # 1s to mean a point in the polygon obstacle
    imgplot = plt.imshow(img, cmap='Greys_r')

    plt.show()

    # initialize the grid
    grid = np.zeros((100, 200))

    # express the sides of the polygon obstacle(s) as 1s 
    # in the grid
    for row, row_points in enumerate(light):
        for col, col_val in enumerate(row_points):
            if col_val < 255:
                grid[row][col] = 1

    grid = grid.tolist()
    
    return startNode, goalNode, grid, shapes

def addEdge(graph,u,v): 
    graph[u].append(v)


def createGraph(grid):
    #m x n matrix
    rows = len(grid)
    cols = len(grid[0])

    graph = defaultdict(list) 
    for row in range(rows):
        for col in range(cols):
            if col != 0 and grid[row][col]!=1 and grid[row][col-1]!=1:
                addEdge(graph,(row,col),(row,col-1)) #left
            if col < cols-1 and grid[row][col]!=1 and grid[row][col+1]!=1:
                addEdge(graph,(row,col),(row,col+1)) #right
            if row != 0 and grid[row][col]!=1 and grid[row-1][col]!=1:
                addEdge(graph,(row,col),(row-1,col)) #top
            if row < rows-1 and grid[row][col]!=1 and grid[row+1][col]!=1:
                addEdge(graph,(row,col),(row+1,col)) #bottom
   
    return graph

def dfs(graph, startNode, goalNode):
    path = [startNode]
    visited = []
    fringe = PriorityQueue()
    fringe.put((0, startNode, path, visited))

    while fringe:
        depth, currentNode, path, visited = fringe.get()
        
        expandedNode.append(currentNode)

        if currentNode == goalNode: 
            return path + [currentNode]
          
        if currentNode not in visited:
          visited = visited + [currentNode]

        for node in graph[currentNode]: #look at the children
            if node not in visited:
                if node == goalNode:
                    expandedNode.append(node)
                    return path + [node]               
                fringe.put((-len(path), node, path + [node], visited + [node]))
    return path 


startNode, goalNode, grid, shapes = createStateSpaceGrid('in5.txt','maze5.png')
graph = createGraph(grid)  #create the graph dictionary
# dfsSolPath = dfsAlgo(graph, startNode, goalNode)

print("starting point:", startNode)
print("goal point:", goalNode)
start = time.time()
path= dfs(graph, startNode, goalNode)
finalPlot(dfsSolPath, startNode, goalNode, shapes, 'dfsTestFive.png')

end = time.time()
print("solution path:", path)
print("cost of the solution:", len(path))
print("number of expanded nodes:",len(expandedNode))

print("actual running time of the program:", end - start)

print(grid)