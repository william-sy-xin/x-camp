import turtle as t

s = t.Screen()

length1=200
width1= 100
size1=100
x = 0
y = 0

def draw_rectangle(x,y,length,width):
    t.pu()
    t.goto(x-(length/2), y-(width/2))
    t.pd()
    t.setheading(0)
    for i in range(2):
        t.fd(length)
        t.lt(90)
        t.fd(width)
        t.lt(90)
        
draw_rectangle(x, y,length1, width1 )

def print_coords(x_click, y_click):
    if -length1/2 < x_click < length1/2 and -width1/2 < y_click < width1/2:
        print("yes")
    else:
        print("no")
        
s.onclick(print_coords)
