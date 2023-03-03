import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Berserk Turtle Drawing")

# Create the turtle object
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# Draw the Berserk image
t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()

t.color("white")
t.penup()
t.goto(-25, 60)
t.pendown()
t.circle(20)

t.penup()
t.goto(25, 60)
t.pendown()
t.circle(20)

t.color("black")
t.penup()
t.goto(-35, 30)
t.pendown()
t.circle(5)

t.penup()
t.goto(35, 30)
t.pendown()
t.circle(5)

t.penup()
t.goto(0, -50)
t.pendown()
t.circle(80, 180)

# Hide the turtle
t.hideturtle()

# Keep the screen open until manually closed
turtle.done()