import turtle

ablak = turtle.Screen()
sanyi = turtle.turtle()

for sz in ["yellow", "red", "purple", "blue"]:

    sanyi.color(sz)
    sanyi.forward(50)
    sanyi.left(90)

    ablak.mainloop()