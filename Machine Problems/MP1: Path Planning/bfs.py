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
    run = 1
    while fringe: #explore til the fringe is not empty!
        node = fringe.pop(0) #get vertex
        expandedNode.append(node) #append the considered vertex to the Expanded Nodes
        if node == goal: #if reaches goal node
            return backtrace(parent, start, goal)
        for adjacent in graph.get(node, []): #consider the children of the popped node 
            if node not in fringe: 
                run+=1  
                print("running=",run)  
                if start[0]<=goal[0]:
                  if adjacent[0] >= node[0]:
                    parent[adjacent] = node  
                if start[0]>=goal[0]:
                    if adjacent[0] <= node[0]:
                      parent[adjacent] = node  
                fringe.append(adjacent) 

grid = [[0 for col in range(199)] for row in range(99)]

print(grid)

graph = createGraph(grid)   
startNode = (0,0)
goalNode = (20,0)

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

