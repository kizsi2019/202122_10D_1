import time
import turtle
import random

colors = ['orange', 'red', 'blue', 'yellow', 'green']
turtle.pen(fillcolor='orange', pencolor='red', pensize=7)
turtle.pen(fillcolor=random.choice(colors), pencolor=random.choice(colors), pensize=7)

turtle.begin_fill()
for _ in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.end_fill()

time.sleep(5)



''' Ablakbeállítás'''
import turtle
import time

# screen = turtle.Screen()
# screen.setup(width=200, height=200, startx=0, starty=0)
    
turtle.setup(width=0.75, height=0.5, startx=10, starty=-10)
    
turtle.bgcolor('blue')
turtle.title('Teknőc')
turtle.bgpic('teknoc.gif')
    
turtle.forward(300)
    
time.sleep(2)
turtle.clear()
time.sleep(2)