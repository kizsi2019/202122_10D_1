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


a = ablak_keszites("lightgreen", "Eszti és Sanyi táncol")
Eszti = teknoc_keszites("hotpink", 5)
Sanyi = teknoc_keszites("black", 1)
David = teknoc_keszites("yellow", 2)


def negyzet(sz):
    for i in range(4):
        Eszti.forward(sz)
        Eszti.left(90)
    Eszti.penup()
    Eszti.backward(20)
    Eszti.right(90)
    Eszti.forward(20)
    Eszti.left(90)
    Eszti.pendown()
meret = 20
for i in range(5):
    negyzet(meret)
    meret = meret + 40


a.mainloop()