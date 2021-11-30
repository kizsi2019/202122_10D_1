import turtle
ablak = turtle.Screen()
sanyi = turtle.Turtle()

fordulat = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for k in fordulat:
    sanyi.forward(100)
    sanyi.left(fordulat)

ablak.mainloop()
