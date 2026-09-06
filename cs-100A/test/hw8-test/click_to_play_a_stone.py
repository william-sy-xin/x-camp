import turtle as t

# ============================================================
#  GOBANG · STEP 4-1   Click to Place a Stone
#  New skill: screen.onclick() event handler
# ============================================================
screen = t.Screen()
SIZE = 15


def InitBoard():
    t.setup(700, 700)
    t.bgcolor("#F0EBCC")
    t.setworldcoordinates(-1, -1, SIZE, SIZE)
    t.speed(0)
    t.hideturtle()
    t.pencolor("black")
    t.penup()
    for i in range(SIZE):
        t.goto(0, i)
        t.pendown()
        t.goto(SIZE - 1, i)
        t.penup()
    for i in range(SIZE):
        t.goto(i, 0)
        t.pendown()
        t.goto(i, SIZE - 1)
        t.penup()


def PlacingChess(x, y, turn):
    radius = 0.4
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    if turn == 1:
        t.color("black", "black")
    else:
        t.color("black", "white")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()

# when you click, draw a stone where you clicked


def HandlePlayerMove(?):
    PlacingChess(?)  # ✏️① draw a stone at the click spot (black = 1)


InitBoard()
screen.title("Click on the board!")
screen.onclick(?)  # ✏️② which function runs when you click?
t.done()
