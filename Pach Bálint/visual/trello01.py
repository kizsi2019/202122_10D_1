def otszog():
    print('Ötszög')
otszog()
import turtle
a = turtle.Screen()
Sanyi = turtle.Turtle()
Sanyi.pensize(5)
def csillag_ot():
    for i in range(5):
        Sanyi.forward(200)
        Sanyi.right(144)
    Sanyi.penup()
    Sanyi.right(144)
    Sanyi.forward(500)
    Sanyi.pendown()
for i in range(5):
    csillag_ot()
a.mainloop()

