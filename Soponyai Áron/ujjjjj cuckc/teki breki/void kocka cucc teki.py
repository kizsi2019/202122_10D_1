
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

def kocka(előre, balra):
    for i in range(4):
        SANYI.forward(előre)
        SANYI.left(balra)
    SANYI.penup
    SANYI.forward(2*előre)
    SANYI.pendown

for i in range(5):
    kocka(20, 90)

a.mainloop()
