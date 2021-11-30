import turtle 

ablak = turtle.Screen() 
Sanyi = turtle.Turtle() 


szinek = ["yellow", "red", "purple", "blue"]
for sz in szinek:
   Sanyi.color(sz)
   Sanyi.forward(50)
   Sanyi.left(90)
Sanyi.penup()
Sanyi.forward(100)
Sanyi.pendown()
Sanyi.forward(50)
Sanyi.left(90)
Sanyi.forward(50)
Sanyi.speed(10)

ablak.mainloop()