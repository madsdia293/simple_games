import turtle
import random

start_finish = turtle.Turtle()
matt = turtle.Turtle()
catalina = turtle.Turtle()

matt.hideturtle()
catalina.hideturtle()

start_finish.width(3)
start_finish.speed(3)
start_finish.hideturtle()
start_finish.penup()
start_finish.goto(-300, 40)
start_finish.pendown()
start_finish.right(90)
start_finish.forward(80)
start_finish.penup()
start_finish.goto(317, 40)
start_finish.pendown()
start_finish.forward(80)

matt.showturtle()
catalina.showturtle()

matt.shape("turtle")
matt.color("blue")
matt.penup()
matt.goto(-300, 20)
matt.pendown()


catalina.shape("turtle")
catalina.color("red")
catalina.penup()
catalina.goto(-300, -20)
catalina.pendown()

finish_line = 300

while matt.xcor() < finish_line and catalina.xcor() < finish_line:
    matt.forward(random.randint(1, 2))
    catalina.forward(random.randint(1, 2))

if matt.xcor() > catalina.xcor():
    print("Matt wins!")
else:
    print("Catalina wins!")

turtle.exitonclick()