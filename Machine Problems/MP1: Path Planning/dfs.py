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


grid = [[0 for col in range(200)] for row in range(100)]
graph = createGraph(grid)   

startNode = (0,0)
goalNode = (2,0)

print("starting point:", startNode)
print("goal point:", goalNode)
path= dfs(graph, startNode, goalNode)
print("solution path:", path)
print("cost of the solution:", len(path))
print("number of expanded nodes:",len(expandedNode))
end = time.time()
print("actual running time of the program:", end - start)

#just edit this to show the path in the grid later
gridResultBFS = grid
for (i,j) in path:
    gridResultBFS[i][j]= '*'
print(grid)