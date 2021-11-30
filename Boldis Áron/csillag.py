import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

t = turtle.Turtle()
t.color("hotpink")

def csillag(len):
  for i in range(5):
    t.forward(len)
    t.right(144)
  
for c in range(5):
  csillag(50)
  t.forward(200)
  t.right(144)
  
