import turtle
wn = turtle.Screen()
tur = turtle.Turtle()
tur.shape("turtle")
tur.showturtle()
tur.fillcolor("blue")
print("The color options are red, blue, green, and black. All colors must be lowercase. Separate colors with a space.")
print("Enter 3 colors. They can all be the same or different")
pen_color = input("Enter the color you want each letter in the initials to be:").split(" ")


def draw_l(turtle, bold, color):
    for i in range(1):
        if bold == True:
            tur.pensize(3)
        if bold == False:
            tur.pensize(1)
        if color == pen_color:
            tur.color(pen_color[0])
        tur.goto(0, 100)
        tur.goto(0, 0)
        tur.forward(75)


tur.fillcolor("black")
jim = turtle.Turtle()
jim.hideturtle()
draw_l(jim, True, pen_color)
tur.fillcolor("red")
tur.penup()
tur.fillcolor("blue")
tur.forward(15)
tur.fillcolor("green")
tur.left(70)
tur.fillcolor("red")
tur.down()

tur.fillcolor("black")


def draw_a(turtle, bold, color):
    for i in range(1):
        if bold == True:
            tur.pensize(3)
        if bold == False:
            tur.pensize(1)
        if color == pen_color:
            tur.color(pen_color[1])
        tur.forward(100)
        tur.right(140)
        tur.forward(100)
        tur.right(180)
        tur.forward(50)
        tur.left(70)
        tur.forward(35)


john = turtle.Turtle()
john.hideturtle()
draw_a(john, True, pen_color)
tur.fillcolor("green")
tur.left(70)
tur.fillcolor("blue")
tur.up()
tur.fillcolor("red")
tur.forward(50)
tur.fillcolor("black")
tur.left(110)
tur.fillcolor("blue")
tur.forward(95)
tur.fillcolor("red")
tur.down()

tur.fillcolor("blue")


def draw_p(turtle, bold, color):
    for i in range(1):
        if bold == True:
            tur.pensize(3)
        if bold == False:
            tur.pensize(1)
        if color == pen_color:
            tur.color(pen_color[2])
        tur.goto(184, 100)
    for i in range(4):
        tur.forward(20)
        tur.right(60)


tur.fillcolor("red")
joe = turtle.Turtle()
joe.hideturtle()
draw_p(joe, True, pen_color)
tur.up()
for i in range(18):
    tur.right(15)
    tur.forward(5 * 10)
tur.fillcolor("blue")
tur.forward(1000)
