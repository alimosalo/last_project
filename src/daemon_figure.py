import os 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
from matplotlib import animation
######defining one figure for our project#######
fig = plt.figure()
###########################(making our picture into gray)
def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[1,0.5870,0.1140])

img = plt.imread("image.jpeg")
##image scaling
img2 =rgb2gray(img/255)
img2 = img2*20
##showing images##
ax1 = plt.axes([0.1,0.1,0.8,0.8])
plt.imshow(img,cmap='gray',vmin=0,vmax=255)
ax2 = plt.axes([0.57, 0.6,0.196,0.277])
plt.imshow(img2,cmap='gray',vmin=0,vmax=67)
#eliminating ticklabels
ax1.axes.xaxis.set_ticklabels([])
ax1.axes.yaxis.set_ticklabels([])
ax2.axes.xaxis.set_ticklabels([])
ax2.axes.yaxis.set_ticklabels([])
#eliminationg ticks
ax2.tick_params(left=False,bottom=False)
ax1.tick_params(left=False,bottom=False)

for axis in ['top','bottom','left','right']:
    ax1.spines[axis].set_linewidth(16)
    ax1.spines[axis].set_color("red")
#ANIMATION###########################################

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
#defineing axis for animation##
ax = plt.axes([0.2,0.3,0.6,0.1])
ax.set_frame_on(False)
ax.axis('off')
####
line, = ax.plot([], [], lw=2)

def init():
   line.set_data([], [])
   return line,

def animate(i):
   x = np.linspace(-0.4, 2, 1000)
   y = 0.05*np.sin(20*np.pi * (x - 0.01 * i))
   line.set_data(x, y)
   return line,
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=200, blit=True)
####(setting name for it)
daemon = "DAEMON"
ax1.text(0,0,daemon,transform=ax1.transAxes,fontsize=14)
plt.show()
