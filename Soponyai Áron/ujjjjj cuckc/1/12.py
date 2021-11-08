import turtle
ablak = turtle.Screen() 
Sanyi = turtle.Turtle() 

Sanyi = turtle.penup()
Sanyi = turtle.forward(80)
for i in range(10):
    Sanyi = turtle.pendown()
    Sanyi = turtle.forward(20)
    Sanyi = turtle.penup()
    Sanyi = turtle.forward(30)
    Sanyi = turtle.stamp()
    Sanyi = turtle.back(130)
    Sanyi = turtle.left(30)




ablak.mainloop() 