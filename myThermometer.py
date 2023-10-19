from vpython import *
import numpy as np

glassBulb=sphere(radius=1.25,color=color.white,opacity=.5)
galssCyl=cylinder(radius=.75,length=6,color=color.white,opacity=.5)
mercSphere=sphere(radius=1,color=color.red)
mercColumn=cylinder(radius=.5,length=6,color=color.red)
for tick in np.linspace(1,6,25):
    box(size=vector(1,.5,.5),color=color.black,pos=vector(tick,0,.5))
while True:
    for mytemp in np.linspace(1,6,100):
        rate(100)
        mercColumn.length=mytemp
    for mytemp in np.linspace(6,1,100):
        rate(100)
        mercColumn.length=mytemp    