import turtle

# Create screen
screen = turtle.Screen()
screen.title("Home Drawing")

# Create turtle
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(3)

# Draw square house base
pen.color("blue")
for i in range(4):
    pen.forward(150)
    pen.left(90)

# Move to roof start
pen.left(45)

# Draw roof
pen.color("red")
pen.forward(106)
pen.right(90)
pen.forward(106)

# Move for door
pen.penup()
pen.goto(55, 0)
pen.pendown()

# Draw door
pen.color("brown")
pen.setheading(90)
pen.forward(70)
pen.right(90)
pen.forward(40)
pen.right(90)
pen.forward(70)
pen.right(90)
pen.forward(40)

# Move for window
pen.penup()
pen.goto(20, 80)
pen.pendown()

# Draw window
pen.color("green")
for i in range(4):
    pen.forward(30)
    pen.right(90)

# Finish
turtle.done()