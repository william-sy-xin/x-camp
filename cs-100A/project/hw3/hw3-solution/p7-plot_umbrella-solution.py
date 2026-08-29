import turtle as t
t.fillcolor("orange")
t.begin_fill()
t.rt(90)
t.circle(100,extent = -180)

for x in range(4):
    t.circle(25,extent = 180)
    t.rt(180)
t.end_fill()
t.rt(90)
t.pencolor("white")
t.fd(100)
t.rt(90)
t.pencolor("black")
t.fd(200)    
t.circle(25,extent = 180)