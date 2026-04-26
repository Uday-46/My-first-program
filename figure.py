import turtle

# Create screen
screen = turtle.Screen()
screen.title("Simple Figure")

# Create turtle
pen = turtle.Turtle()
pen.pensize(3)
pen.color("blue")

# Draw a square figure
for i in range(4):
    pen.forward(100)
    pen.right(90)

# Hide turtle
pen.hideturtle()

# Keep window open
turtle.done()