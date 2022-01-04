import turtle
import time
  
MAX_X, MAX_Y = 400, 250
WIDTH, HEIGHT = MAX_X * 2 + 80, MAX_Y * 2 + 20
screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
  
cel = turtle.Turtle()
cel.penup()
cel.setpos(MAX_X - 20, MAX_Y)
cel.pendown()
cel.pen(pencolor='black', pensize=7)
cel.right(90)
cel.forward(MAX_Y * 2)
    
norris = turtle.Turtle()
norris.shape('turtle')
norris.shapesize(stretch_wid=2, stretch_len=2, outline=4)
norris.pen(pencolor='blue', fillcolor='orange', pensize=9)
norris.penup()
norris.setpos(- MAX_X, 0)
norris.pendown()
norris.forward(MAX_X * 2)


time.sleep(5)