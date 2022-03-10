from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("cyan1")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)



screen = Screen()

screen.exitonclick()
