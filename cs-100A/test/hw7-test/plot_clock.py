import turtle as t
import time
style = ('Courier', 30, 'italic')

# initializing a canvas
s = t.Screen()
s.setup(600, 600)  # canvas size
s.tracer(0)  # remove cartoon effect of plotting

# create a painter object for plotting clock disk.
p = t.Turtle()
p.hideturtle()
p.speed(0)


def create_clock_hand(name, length, color):
    hand = t.Turtle()
    hand.hideturtle()
    hand.speed(0)
    hand.shape("blank")
    return hand, length, color


sec_hand_info = create_clock_hand("second", 180, "red")
min_hand_info = create_clock_hand("minute", 150, "black")
hour_hand_info = create_clock_hand("hour", 100, "black")


def plot_clock_plate():
    # go to the center of the clock plate
    p.pu()
    p.goto(0, 200)
    p.pd()

    # set "12" to the right place
    p.pu()
    p.circle(-200, extent=30)
    p.pd()

    for c in range(1, 13):
        p.write(c, font=style)
        p.pu()
        p.circle(-200, extent=30)
        p.pd()


def update_clock_hands(hand_info, angle):
    hand, length, color = hand_info
    hand.clear()
    hand.penup()
    hand.goto(0, 0)
    hand.color(color)

    turtle_angle = 90 - angle
    hand.setheading(turtle_angle)

    hand.pendown()
    hand.forward(length)


def run_clock():
    local_time = time.localtime()
    h = local_time.tm_hour % 12
    m = local_time.tm_min
    sec = local_time.tm_sec

    s_angle = sec * (360/60)
    m_angle = m * (360/60) + sec * (360/60/60)
    h_angle = h * (360/12) + m * (360/12/60) + sec * (360/12/60/60)

    update_clock_hands(sec_hand_info, s_angle)
    update_clock_hands(min_hand_info, m_angle)
    update_clock_hands(hour_hand_info, h_angle)

    s.update()
    s.ontimer(run_clock, 100)


# Initialize and kick off the loop
plot_clock_plate()
run_clock()

s.mainloop()
