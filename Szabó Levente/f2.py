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

def négyzet(sz):
    for i in range(4):
        Eszti.forward(sz)
        Eszti.left(90)
    Eszti.penup()
    Eszti.right(90)
    Eszti.forward(10)
    Eszti.left(90)
    Eszti.backward(10)
    Eszti.pendown()
    
for i in range(1):
    négyzet(20)
for i in range(1):
    négyzet(40)
for i in range(1):
    négyzet(60)
for i in range(1):
    négyzet(80)

a.mainloop()