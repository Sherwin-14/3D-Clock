from vpython import *
from time import *
import numpy as np
import simpy
from threading import Thread,Lock


scene=canvas(width=900,length=900)


"""
#Set the size of the grid cells
cell_size = 1

# Set the number of cells in the x and y directions
x_cells = 10
y_cells = 10

# Calculate the size of the canvas
canvas_width = cell_size * x_cells
canvas_height = cell_size * y_cells

# Draw vertical grid lines
for i in range(x_cells + 1):
    x = i * cell_size - canvas_width / 2
    curve(pos=[(x, -canvas_height / 2, 0), (x, canvas_height / 2, 0)], color=color.white)

# Draw horizontal grid lines
for i in range(y_cells + 1):
    y = i * cell_size - canvas_height / 2
    curve(pos=[(-canvas_width / 2, y, 0), (canvas_width / 2, y, 0)], color=color.white)

"""
#                           ------Random Cooridnate generation------
"""
x_min,x_max=-20,20
y_min,y_max=-20,20
z_min,z_max=20,20

x1=np.random.randint(x_min,x_max)
y1=np.random.randint(y_min,y_max)
z1=np.random.randint(z_min,z_max)

x2=np.random.randint(x_min,x_max)
y2=np.random.randint(y_min,y_max)
z2=np.random.randint(z_min,z_max)

x3=np.random.randint(x_min,x_max)
y3=np.random.randint(y_min,y_max)
z3=np.random.randint(z_min,z_max)

"""
#                          ------Full----------------



machine1=box(pos=vector(0,0,0),size=vector(0.9,0.9,0.9))
machine2=box(pos=vector(-12,0,0),size=vector(0.9,0.9,0.9))
machine3=box(pos=vector(12,0,0),size=vector(0.9,0.9,0.9))
machine4=box(pos=vector(19,-15,0),size=vector(0.9,0.9,0.9))


drag=False
selected_machine=None

def hover_mousedown():
    global drag,selected_machine

    if scene.mouse.pick in[machine1,machine2,machine3,Buffer1,Buffer2]:
        drag=True

        selected_machine=scene.mouse.pick

def hover_mousemove():
    global drag,selected_machine

    if drag:

        selected_machine.pos=scene.mouse.pos

def hover_mouseup():
    global drag,selected_machine,targets

    if drag and selected_machine:
        # Update the targets list based on the new position of the selected machine
        if selected_machine == machine1:
            targets[2] = selected_machine.pos
        elif selected_machine == machine2:
            targets[0] = selected_machine.pos
        elif selected_machine == machine3:
            targets[4] = selected_machine.pos

        elif selected_machine==Buffer1:
            targets[1]=selected_machine.pos

        elif selected_machine==Buffer2:
            targets[1]=selected_machine.pos      

    drag=False

    selected_machine=None

scene.bind('mousedown',hover_mousedown)
scene.bind('mousemove',hover_mousemove)
scene.bind('mouseup',hover_mouseup)      

Buffer1=cylinder(pos=vector(-5,0,0),color=color.blue,radius=0.5)
Buffer2=cylinder(pos=vector(5,0,0),color=color.blue,radius=0.5)

targets=[vector(-12,0,0),vector(-5,0,0),vector(0,0,0),vector(5,0,0),vector(12,0,0),vector(19,-15,0)]
targets_again=[vector(12,0,0),vector(5,0,0),vector(19,-15,0)]

my_label1=label(
    pos=machine1.pos,
    height=16,
    border=4,
    text='Machine1',
    yoffset=50,
    font='sans'
)

my_label2=label(
    pos=machine2.pos,
    height=16,
    border=4,
    text='Machine2',
    yoffset=50,
    font='sans'
)

my_label3=label(
    pos=machine3.pos,
    height=16,
    border=4,
    text='Machine3',
    yoffset=50,
    font='sans'
)

label(pos=vector(19,15,0),text='White-Machine',box=False)
label(pos=vector(10,15,0),text='Red-Jobs',box=False,color=color.red)
label(pos=vector(30,15,0),text='Blue-Buffers',box=False,color=color.blue)


marble=sphere(pos=vector(targets[0]), color=vector(1,0,0),radius=0.5,velocity=vector(1,0,0))
marble1=sphere(pos=vector(targets_again[0]),color=vector(1,1,0),radius=0.5,velocity=vector(1,0,0))


deltaX=0.2
xPos=-12
speed=0.1

"""
def marble_process(env,marble,targets,speed,xPos,deltaX):
    current_target_index=0
    while True:
        target_pos = targets[current_target_index]
        distance = mag(target_pos - marble.pos)

        if distance > 0.1:
            direction= norm(target_pos - marble.pos)
            xPos=xPos+deltaX
            marble.pos = marble.pos + direction * speed 
            yield env.timeout(1)

        else:
            if (current_target_index == 1 or current_target_index == 3):
                yield env.timeout(350)
            current_target_index += 1

            if(current_target_index >= len(targets)):
                     break

def marble1_process(env,marble1,targets_again,speed,xPos,deltaX):
    current_index=0
    while True:
       target_position=targets_again[current_index]
       displacement=mag(target_position-marble1.pos)

       if displacement > 0.1:
            direction= norm(target_position - marble1.pos)
            xPos=xPos+deltaX
            marble1.pos = marble1.pos + direction * speed
            yield env.timeout(1)

       else:
            if (current_index == 1 ):
                yield env.timeout(350)
            current_index += 1

            if(current_index >= len(targets_again)):
                     break              

env=simpy.Environment()
marble_process=env.process(marble_process(env,marble,targets,speed,xPos,deltaX))
marble1_process=env.process(marble1_process(env,marble1,targets_again,speed,xPos,deltaX))
env.run()



for _ in range(100):

    marble.pos = vector(targets[0])
    marble1.pos=vector(targets_again[0])
    current_target_index=0
    current_index=0

    while True:

        target_pos = targets[current_target_index]
        target_position=targets_again[current_index]
        distance = mag(target_pos - marble.pos)
        displacement=mag(target_position-marble1.pos)

        if distance > 0.1:
            direction= norm(target_pos - marble.pos)
            xPos= xPos + deltaX
            marble.pos = marble.pos + direction * speed 
            rate(70)    

        else:
            if (current_target_index == 1 or current_target_index == 3):
                for i in range(350):
                    rate(70)
            current_target_index += 1

            if(current_target_index >= len(targets)):
                     break
            
        if displacement > 0.1:
            direction= norm(target_position - marble1.pos)
            xPos= xPos + deltaX
            marble1.pos = marble1.pos + direction * speed 
            rate(70) 

        else:
            if (current_index == 1 ):
                for i in range(350):
                    rate(70)
            current_index += 1

            if(current_index >= len(targets_again)):
                     break             

"""

for i in range(100):

    marble.pos = vector(targets[0])
    marble1.pos=vector(targets_again[0])
    current_target_index=0
    current_index=0

    while True:

        target_pos = targets[current_target_index]
        target_position=targets_again[current_index]
        distance = mag(target_pos - marble.pos)
        displacement=mag(target_position-marble1.pos)

        if distance > 0.1:
            direction= norm(target_pos - marble.pos)
            xPos= xPos + deltaX
            marble.pos = marble.pos + direction * speed 
            rate(70)    

        else:
            if (current_target_index == 1 or current_target_index == 3):
                for i in range(350):
                    rate(70)
            current_target_index += 1

            if(current_target_index >= len(targets)):
                     break
            
        if displacement > 0.1:
            direction= norm(target_position - marble1.pos)
            xPos= xPos + deltaX
            marble1.pos = marble1.pos + direction * speed 
            rate(70) 

        else:
            if (current_index == 1 ):
                for i in range(350):
                    rate(70)
            current_index += 1

            if(current_index >= len(targets_again)):
                     break             


""" 

lock = Lock()

def update_marble(marble, targets):
    current_target_index = 0
    while True:
        with lock:
            # Acquire the lock before accessing shared data
            target_pos = targets[current_target_index]
            print(target_pos)
            distance = mag(target_pos - marble.pos)

        if distance > 0.1:
            direction = norm(target_pos - marble.pos)
            with lock:
                # Acquire the lock before modifying shared data
                marble.pos = marble.pos + direction * speed
            rate(70)
        else:
            if current_target_index == 1 or current_target_index == 3:
                for i in range(350):
                    rate(70)
            current_target_index += 1
            if current_target_index >= len(targets):
                break

def update_marble_again(marble1, targets_again):
    current_index = 0
    while True:
        with lock:
            # Acquire the lock before accessing shared data
            target_pos = targets_again[current_index]
            distance = mag(target_pos - marble1.pos)
            
        if distance > 0.1:
            direction = norm(target_pos - marble1.pos)
            with lock:
                # Acquire the lock before modifying shared data
                marble1.pos = marble1.pos + direction * speed
            rate(70)
        else:
            if current_index == 1:
                for i in range(350):
                    rate(70)
            current_index+=1

            if current_index >= len(targets_again):
                break       


t1 = Thread(target=update_marble, args=(marble, targets))
t2 = Thread(target=update_marble_again, args=(marble1, targets_again))

# Start the threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()  """