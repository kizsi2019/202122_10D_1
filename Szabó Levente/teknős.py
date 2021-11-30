import turtle
ablak = turtle.Screen()
Sanyi = turtle.Turtle()
Sanyi.speed(10)

színek = ["red", "yellow", "purple", "blue"]
for sz in színek:
    Sanyi.color(sz)
    Sanyi.forward(50)
    Sanyi.left(90)

Sanyi.penup()
Sanyi.forward(100)
Sanyi.pendown()

színek = ["red", "yellow", "purple", "blue"]
for sz in színek:
    Sanyi.color(sz)
    Sanyi.forward(50)
    Sanyi.left(90)
ablak.mainloop()