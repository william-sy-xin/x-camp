import turtle as t

#set the color of the pen and the fill color
t.pencolor("yellow green")
t.fillcolor("yellow green")

#start to fill
t.begin_fill()

#Creating the heptagon
for n in range(7):
    t.fd(100)
    t.lt(52)

#fininshing the fill
t.end_fill()