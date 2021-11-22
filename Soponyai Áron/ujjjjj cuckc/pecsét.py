import turtle
ablak = turtle.ablak()
ablak.bgcolor("lightgreen")
Sanyi = turtle.Turtle()
Sanyi.shape("turtle")
Sanyi.color("blue")

Sanyi.penup
meret = 20
for i in range(30):
    Sanyi.stamp()
    meret = meret + 3
    Sanyi.forward(meret)
    Sanyi.right(24)

ablak.mainloop()