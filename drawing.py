import turtle

screen = turtle.Screen()
screen.title("Drawing Window")

pen = turtle.Turtle()
pen.pensize(3)
pen.color("blue")

for i in range(4):
    pen.forward(100)
    pen.right(90)

turtle.done()