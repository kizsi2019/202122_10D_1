import turtle 

ws = turtle.Screen()
Turtle = turtle.Turtle()

def mozog():
    Turtle.penup()
    Turtle.forward(100)
    Turtle.right(144)
    Turtle.pendown()

def csillag (meter):
    for i in range(5):
        Turtle.forward(meter)
        Turtle.right(144)

for i in range(5):
    csillag(20)
    mozog()

