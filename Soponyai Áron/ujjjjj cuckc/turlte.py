import turtle
ablak = turtle.ablak()
Sanyi = turtle.Turtle()
for sz in['yellow', 'red', 'purple', 'blue']:
    Sanyi.speed(10)
    Sanyi.color(sz)
    Sanyi.forward(50)
    Sanyi.left(98)
    Sanyi.penup()
    Sanyi.forward(50)
    Sanyi.pendown()
    Sanyi.left(98)
    Sanyi.forward(50)

ablak.mainloop()