from vpython import *
from time import *
mradius=0.75
wallthickness=0.1
roomWidth=15
roomDepth=5
roomHeight=2
floor=box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallthickness,roomDepth),color=color.white)
ceiling=box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallthickness,roomDepth),color=color.white)
backwall=box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallthickness),color=color.white)
leftwall=box(pos=vector(-roomWidth/2,0,0),size=vector(wallthickness,roomHeight,roomDepth),color=color.white)
rightwall=box(pos=vector(roomWidth/2,0,0),size=vector(wallthickness,roomHeight,roomDepth),color=color.white)
marble=sphere(radius=.75,color=color.red)
deltaX=.1
xPos=0
while True:
    rate(100)
    xPos=xPos+deltaX
    Xrme=xPos+mradius
    Xlme=xPos-mradius
    rwe=roomWidth/2-wallthickness/2
    lwe=-roomWidth/2+wallthickness/2
    if Xrme>=rwe or xPos<=lwe:
        deltaX=deltaX*-1
   
    marble.pos=vector(xPos,0,0)