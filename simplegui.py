import matplotlib.pyplot as plt
import cv2


my_dpi = 96


plt.figure()


def plot_polygon(coord):
    coord.append(coord[0]) #repeat the first point to create a 'closed loop'
    xs, ys = zip(*coord) #create lists of x and y values
    plt.plot(xs,ys, linewidth=3) 

def plot_point(x, y):
    plt.scatter(x, y, 30)


plot_polygon( [[10,10], [20,10], [20,20], [10,20], [5,15]] )
plot_polygon( [[50,50], [30,50], [30,40]] )
plot_polygon( [[100,50], [20,80], [120,80]] )

plot_point(100, 90)

plt.plot(100, 200)
plt.axis('off')

plt.savefig('maze.png')
plt.clf() 

img = cv2.imread('maze.png', cv2.IMREAD_GRAYSCALE)

imgplot = plt.imshow(img, cmap='Greys_r')
print(img)

for x in img[0]:
    print(x)


plt.axis('off')
plt.show()