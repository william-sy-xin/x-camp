import turtle as t
s = t.Screen()
t.speed(0)
def plot_pen(x,y):
    t.goto(x,y)

s.onclick(plot_pen)