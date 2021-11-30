import turtle

def ablak_keszites(szin, ablaknev):
    a = turtle.Screen()
    a.bgcolor(szin)
    a.title(ablaknev)
    return a


def teknoc_keszites(szin, tm):
    t = turtle.Turtle()
    t.color(szin)
    t.pensize(tm)
    return t


a = ablak_keszites("lightgreen", "Gyönyörű minta")
Eszti = teknoc_keszites("hotpink", 5)
Sanyi = teknoc_keszites("black", 1)
David = teknoc_keszites("yellow", 2)


def kocika(sz)
    t.forward(100)
    t.left(90)
    

a.mainloop()