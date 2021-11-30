import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
a.title("random")

Sanyi = turtle.Turtle()
hossz = 2

for i in range(100):
    Sanyi.forward(hossz)
    hossz = hossz + 2 
    Sanyi.right(89)
a.mainloop()