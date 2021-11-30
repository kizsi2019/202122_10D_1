import turtle

def ablak_keszites(szin, ablakneve):
    a = turtle.Screen()
    a.bgcolor(szin)
    a.title(ablakneve)
    return a

def teknos_keszites(szin, tm ):
    t = turtle.Turtle()
    t.color(szin)
    t.pensize(tm)
    return t

a = ablak_keszites("lightgreen", "Eszti és Sanyi rák evés")
Eszti = teknos_keszites("hotpink", 5)
SANYI = teknos_keszites("black", 1)
DÁVID = teknos_keszites("yellow", 2)

def mozg():
  SANYI.penup()
  SANYI.forward(100)
  SANYI.right(144)
  SANYI.pendown()

def csilag (meter):
  for i in range(5):
    SANYI.forward(meter)
    SANYI.right(144)

for i in range(5):
  csilag(20)
  mozg()
