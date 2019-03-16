# from https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
import math

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.cost = 0
        self.heuristic = 0
        self.total_cost = 0

    def __eq__(self, other):
        print("checking node equality", self.position, other.position)
        # return self.position == other.position
        return self.position[0] == other.position[0] and self.position[1] == other.position[1] 

def get_distance(x1, y1, x2, y2, technique):
    if technique == "diagonal":
        return (x1 - x2)**2 + (y1 - y2)**2 # ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
    
    if technique == "chebyshev":
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return (dx + dy) + (1 - 2 * 1) * min(dx, dy)


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    end_node = Node(None, end)

    # initialize lists
    open_list   = []
    closed_list = []

    # put the start node in the open list
    open_list.append(start_node)

    # define looping condition
    # ie. if there are nodes left to open
    # then continue to loop
    has_open_node = len(open_list) > 0

    while has_open_node:
        curr_index = 0
        curr_node = open_list[curr_index]

        # find the node with the least total_cost
        for index, node in enumerate(open_list):
            if node.total_cost < curr_node.total_cost:
                curr_node  = node
                curr_index = index

        # pop most recent current node from open list
        # enqueue to closed_list
        open_list.pop(curr_index)
        closed_list.append(curr_node)

        # Found the goal
        if curr_node == end_node:
            path = []
            curr = curr_node
            while curr is not None:
                path.append(curr.position)
                curr = curr.parent
            path.reverse()
            return path # [::-1] # Return reversed path

        # initialize children list
        children = []

        # set the relative positions of all possible adjacent cells
        # technique is given by Swift, Nicolas
        # from https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

        adj_cells = [(-1, -1), (-1, 0), (-1, 1),
                     ( 0, -1),          (0, 1),  
                     (1, -1),  ( 1, 0), (1, 1)]
        
        for new_position in adj_cells: # adj squares

            # Get node position
            curr_x = curr_node.position[0]
            curr_y = curr_node.position[1]

            new_x = new_position[0]
            new_y = new_position[1]

            node_position = (curr_x + new_x, curr_y + new_y)

            # Make sure walkable terrain
            is_walkable = maze[node_position[0]][node_position[1]] == 0
            if not is_walkable:
                continue

            # Make sure within range
            is_within_range = node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0
            if is_within_range:
                continue

            # Create new node
            new_node = Node(curr_node, node_position)

            # Append
            children.append(new_node)

        # Check children
        for child in children:
            for closed_child in closed_list: # for all nodes that have been checked
                if child == closed_child:    # check if this node has been checked
                    continue                 # if checked, don't process

            # total_cost, cost, and heuristic values
            child.cost = curr_node.cost + 1

            # child.heuristic = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.heuristic = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            # child.heuristic = get_distance(child.position[0], child.position[1], end_node.position[0], end_node.position[1], "diagonal")
            
            # heuristic could either be chebychev or diagonal

            child.total_cost = child.cost + child.heuristic

            for open_node in open_list:     # if child is in set of points pending opening
                child_is_open = child == open_node
                if child_is_open:
                    if child.cost > open_node.cost:
                        continue

            # Add the child to the open list
            open_list.append(child)