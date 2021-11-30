import turtle

def ablak_keszites(szin, ablakneve):
    a = turtle.screen()
    a.bgcolor(szin)
    a.title(ablakneve)
    return a

def teknos_keszites(szin, tm ):
    t = turtle.Turtles()
    t.color(szin)
    t.pensize(tm)
    return t

a = ablak_keszites("lightgreen", "Eszti és Sanyi rák evés")
Eszti = teknos_keszites("hotpink", 5)
SANYI = teknos_keszites("black", 1)
DÁVID = teknos_keszites("yellow", 2)

a.mainloop()