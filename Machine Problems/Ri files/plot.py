import matplotlib.pyplot as plt

def plot_polygon(coord):
    coord.append(coord[0]) #repeat the first point to create a 'closed loop'
    xs, ys = zip(*coord) #create lists of x and y values
    plt.plot(xs,ys, linewidth=3) 

def plot_point(x, y):
    plt.scatter(x, y, 30)