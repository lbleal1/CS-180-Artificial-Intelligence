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
      
def bfs(graph, startNode, goalNode):
    parent = {} 
    fringe = [] 
    fringe.append(startNode) #append starting node

    while fringe: #explore til the fringe is not empty!
        currentNode = fringe.pop(0) #get vertex
        #print(node)
        expandedNode.append(currentNode) #append the considered vertex to the Expanded Nodes
        if currentNode == goalNode: #if reaches goal node
            return backtrace(parent, startNode, goalNode)
        for adjacent in graph.get(currentNode, []): #consider the children of the popped node 
            if currentNode not in fringe:   
                if startNode[0]<=goalNode[0]:
                  if adjacent[0] >= currentNode[0]:
                    parent[adjacent] = currentNode 
                if startNode[0]>=goalNode[0]:
                    if adjacent[0] <= currentNode[0]:
                      parent[adjacent] = currentNode  
                fringe.append(adjacent) 

grid = [[0 for col in range(200)] for row in range(100)]

graph = createGraph(grid)   
startNode = (0,0)
goalNode = (10,10)

print(len(grid))
print(len(grid[0]))
print("starting point:", startNode)
print("goal point:", goalNode)
path=bfs(graph, startNode, goalNode)
print("solution Path:",path)
print("cost of the solution:", len(path))
print("number of expanded nodes:",len(expandedNode))
end = time.time()
print("actual running time of the program:", end - start)

# reference: 
# https://codereview.stackexchange.com/questions/135156/bfs-implementation-in-python-3