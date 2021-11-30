import turtle


def teglalap_rajzolas(t, sz, m):
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(h)
        t.left(90)


a = turtle.Screen()
a.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.pensize(3)

meret = 20  # A legkisebb négyzet mérete
for i in range(2):
    tobbszinu_negyzet_rajzolas(Eszti, meret)
    t.forward(sz)  # Növeljük a következo négyzet méretét ˝
    t.left(90)
  # Kicsit arrébb léptetjük a teknocöt ˝
    t.forward(m)
  # és kicsit elfordítjuk

a.mainloop()
