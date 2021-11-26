###########################################################
#
#  Filename: Liss_animation.py
#
#  Lissajous figures using matplotlib. Animatimation 
#  created by re-drawing the figure at different phase 
#  shifts. The phase shifted plots are stored in arrays as separate frames.
#  The shape of each figure is rendered as a series of small line segments. 
#
#  Author: Dr. Brian MacKay
#
#  Date: 7-4-2021
#
#  Modifications:
#
#  Notes:
#
###########################################################
import numpy as np
from math import sin, cos, radians
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

FRAMES_MAX = 720     # number of frames in the animation sequence
ANGLE_MAX  = 360 #180      # angle range in degrees

X_MAX      = 3.0      # plot scale on x axis
Y_MAX      = 1.0      # plot scale on y axis 
X_LIMIT    = (-X_MAX, X_MAX)  # plot range x axis
Y_LIMIT    = (-Y_MAX, Y_MAX)  # plot range y axis 
PLOT_COLOR = (0.02, 0.02, 0.02)  # just the color of the graph
LINE_COLOR = '#33FF44'    # just the color of the lines 
PLOT_SIZE  = (5,5)       # drawing size on canvas

"""--------------------------------------------------------
 Function: make_plot
 Arguments: 
   fscale : frequency ratio for Liss
   frame  : index number used for animation 
 Description: 
   Compose the graph data for each frame by computing 
   the Lissajous figure values. The x,y values are 
   stored in line segment arrays          
--------------------------------------------------------"""      
def make_plot(fscale, frame):  
    for t in range(ANGLE_MAX):
        angle = radians(3*t) 
        angle2 = radians(3*t)  
        x = np.sin ( 2.0*angle )
        y = np.sin ( (frame/360)*angle  )
        line_segments[frame,t,0]  =  x    
        line_segments[frame,t,1]  =  y 

"""--------------------------------------------------------
 Function : animate
 Arguments: 
   frame is the frame index number used for animation 
 Description: 
    Rrender the x/y sine wave for each frame
    with next shape change (amp or phase modification)  
--------------------------------------------------------"""    
def animate(frame):
    linesx = line_segments[frame,:,0]
    linesy = line_segments[frame,:,1]
    line.set_data(linesx, linesy)
    return line,

freq_scale = 2    # freq ratio for Lissajous figure 
line_segments = np.zeros((FRAMES_MAX, ANGLE_MAX, 2))  # initialize the line segments
for frame in range(FRAMES_MAX):   # this loop will create the data for each frame
    make_plot(freq_scale, frame)

# everything below is pretty much standard matplotlib animation calls, nothing fancy
figure = plt.figure(figsize=PLOT_SIZE) 
axis   = figure.add_subplot( xlim=X_LIMIT, ylim=Y_LIMIT)
figure.patch.set_facecolor(PLOT_COLOR)     
axis.set_facecolor(PLOT_COLOR)    

line, = axis.plot([], [], LINE_COLOR, lw=1.0)   
ani = animation.FuncAnimation(figure, animate, FRAMES_MAX, interval=30, blit=True)
plt.show()

