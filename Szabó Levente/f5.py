import turtle
ablak = turtle.Screen()

Sanyi = turtle.Turtle()
hossz = 3
for i in range(92):
    Sanyi.forward(20)
    hossz = hossz + 3
    Sanyi.right(90)
ablak.mainloop()