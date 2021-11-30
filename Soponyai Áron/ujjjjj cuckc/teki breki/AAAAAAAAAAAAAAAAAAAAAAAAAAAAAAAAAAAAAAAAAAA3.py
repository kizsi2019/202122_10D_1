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

def kocka(meter):
  SANYI.forward(meter)
  SANYI.left(90)

meter = 5

for i in range(100000000000000):
  kocka(meter)
  meter = meter + 5

a.mainloop()