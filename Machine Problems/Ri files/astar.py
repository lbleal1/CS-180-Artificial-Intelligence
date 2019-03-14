import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imresize
import cv2
from read import *
import math
import heapq



def plot_polygon(coord):
    coord.append(coord[0]) #repeat the first point to create a 'closed loop'
    xs, ys = zip(*coord) #create lists of x and y values
    plt.plot(xs,ys, linewidth=10) 

def plot_point(pt):
    plt.scatter(pt[0], pt[1], 30)

class Cell(object):
    def __init__(self, x, y, reachable):
        """
        Initializes a new cell
        x cell coordinate
        y cell coordinate
        is the cell reachable?
        """
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.cost = 0           # g
        self.heuristic = 0      # h
        self.total_cost = 0     # f

    def __lt__(self, other):
        return self.cost < other.cost 

class AStar(object):
    def __init__(self):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = []
        self.grid_height = 10
        self.grid_width = 10
        # self.grid = grid

    def get_heuristic(self, cell):
        # x1, y1 = pt1[0], pt1[1]
        # x2, y2 = pt2[0], pt2[1]

        # dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 

        
        # return dist
        return 10 * (abs(cell.x - self.end.x) + abs(cell.y - self.end.y))
        #return math.sqrt((self.end.x - cell.x)**2 + (self.end.y - cell.y)**2) 


    def get_cell(self, x, y):
        return self.cells[x*self.grid_height + y]

    def get_adjacent_cells(self,cell):
        cells = []
        if cell.x < self.grid_width - 1:
            cells.append(self.get_cell(cell.x+1, cell.y))
        if cell.y > 0:
            cells.append(self.get_cell(cell.x, cell.y-1))
        if cell.x > 0:
            cells.append(self.get_cell(cell.x-1, cell.y))
        if cell.y < self.grid_height-1:
            cells.append(self.get_cell(cell.x, cell.y+1))

        return cells

    def display_path(self):
        cell = self.end
        while cell.parent is not self.start:
            cell = cell.parent
            print("path: cell", cell.x, cell.y)

    def update_cell(self, adj, cell):
        # updates adjacent cells
        adj.cost = cell.cost + 10
        adj.heuristic = self.get_heuristic(adj)
        adj.parent = cell
        adj.total_cost = adj.heuristic + adj.cost

    def init_grid(self, grid, start, goal):
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                #if (x, y) in walls:
                if grid[x][y] == 1:
                    reachable = False
                else:
                    reachable = True

                self.cells.append(Cell(x, y, reachable))

        self.start = self.get_cell(start[0], start[1])
        self.end = self.get_cell(goal[0], goal[1])



    def process(self):
    

        heapq.heappush(self.opened, (self.start.total_cost, self.start))

        while len(self.opened):
            # pop ecll from heap queue
            total_cost, cell = heapq.heappop(self.opened)

            # add cell to closed list
            self.closed.add(cell)

            # if ending cell, display found path
            if cell is self.end:
                self.display_path()

            # get adjacent cells for cell
            adj_cells = self.get_adjacent_cells(cell)

            for adj_cell in adj_cells:
                if adj_cell.reachable and adj_cell not in self.closed:
                    if (adj_cell.total_cost, adj_cell) in self.opened:
                        # if adjacent cell is in open list, 
                        # check if current path is better than 
                        # the previously found for this adj cell
                        if adj_cell.cost > cell.cost + 10:
                            self.update_cell(adj_cell, cell)
                    else:
                        self.update_cell(adj_cell, cell)

                        # add adj cell to open list
                        heapq.heappush(self.opened, (adj_cell.total_cost, adj_cell))

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
# light = cv2.resize(img, (200, 100))
light = cv2.resize(img, (20, 10))




plt.axis('off')
imgplot = plt.imshow(img, cmap='Greys_r')
# print(img)

# grid = np.zeros((100, 200))
grid = np.zeros((10, 20))

for row, row_points in enumerate(light):

    for col, col_val in enumerate(row_points):
        if col_val < 255:
            # print("found a color")
            grid[row][col] = 1

for row in grid:
    print(row)


plt.axis('off')
plt.show()

trial = AStar()
trial.init_grid(grid, start, goal)
trial.process()
