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
#  Date: 11-25-2021
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

FRAMES_MAX = 720    # number of frames in the animation sequence
ANGLE_MAX  = 360 #180      # angle range in degrees

X_MAX      = 3.0 # x axis range, larger number = larger x range visible
Y_MAX      = 1.0 # y axis range , larger number = larger y range visible
X_LIMIT    = (-X_MAX, X_MAX)  # full plot range x axis - to +
Y_LIMIT    = (-Y_MAX, Y_MAX)  # full plot range y axis  - to +
PLOT_COLOR = (0.0, 0.0, 0.0)  # just the color of the graph (black)  Red,Green,Blue 
LINE_COLOR = '#33FF44'    # just the color of the lines.  Red,Green,Blue 
PLOT_SIZE  = (5,5)       # drawing size (stay under 5 to see window controls) 

"""--------------------------------------------------------
 Function: make_plot
 Arguments: 
   fscale : frequency ratio for Liss
   frame  : index number used for animation 
 Description: 
   Compose one plot of graph data for one animation frame by computing 
   the Lissajous figure values over the entire angle range. The x,y values are 
   stored in line segment arrays. Variables that include frame in the 
   calculation will appear to change over time as the plots are 
   animated.      
--------------------------------------------------------"""      
def make_plot(fscale, frame):  
    FRAME_DIV = 45.0;    # only affects y axis, smaller number allows shape to progress further over animation range 
    X_FREQ_SCALE = 32.0;  # only affects X axis, thus changes shapes
    ANGLE_SCALER  = 0.25;   # affects mapping of plot range angle to actual angle, large numbers here will make graph look choppy but doesnt change shape

    for t in range(ANGLE_MAX):
        # to increase progress of the shape within one frame increase ANGLE_SCALER
        angle = radians(ANGLE_SCALER*t) 
        # to change shape of x relative to y, change the X_FREQ_SCALE here: 
        x = np.sin ( X_FREQ_SCALE * angle )  # 
        # to slow down progression of shape change over frames, slowing down movement affect , increase FRAME_DIV here: 
        y = np.sin ( (frame/FRAME_DIV)*angle  )  
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

FREQ_SCALER = 2.0    # freq ratio for Lissajous figure ? should be a double ? 
line_segments = np.zeros((FRAMES_MAX, ANGLE_MAX, 2))  # initialize the line segments
for frame in range(FRAMES_MAX):   # this loop will create the data for each frame
    make_plot(FREQ_SCALER, frame)

# everything below is pretty much standard matplotlib animation calls, nothing fancy
figure = plt.figure(figsize=PLOT_SIZE) 
axis   = figure.add_subplot( xlim=X_LIMIT, ylim=Y_LIMIT)
figure.patch.set_facecolor(PLOT_COLOR)     
axis.set_facecolor(PLOT_COLOR)    

# LINE_COLOR and lw (line width) are located here: 
line, = axis.plot([], [], LINE_COLOR, lw=1.0) 
# setting interval higher will slow down animation a little   
ani = animation.FuncAnimation(figure, animate, FRAMES_MAX, interval=30, blit=True)
plt.show()

