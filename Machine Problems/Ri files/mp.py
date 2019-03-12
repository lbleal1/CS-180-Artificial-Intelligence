import matplotlib.pyplot as plt
from scipy.misc import imresize
# import cv2
from read import *
from plot import *

start, goal, shapes = read_input('in.txt')


plt.figure()

for shape in shapes:
    plot_polygon(shape)

plot_point(100, 90)

plt.plot(100, 200) # to ensure dimensions are 100,200
plt.axis('off')
plt.show()


plt.savefig('maze.png')
plt.clf() 

img = cv2.imread('maze.png', cv2.IMREAD_GRAYSCALE)
light = cv2.resize(img, (200, 100))

imgplot = plt.imshow(img, cmap='Greys_r')
print(img)
print("GI")
for x in light:
    print("ONE:")
    

    print("END\n\n")


plt.axis('off')
plt.show()
