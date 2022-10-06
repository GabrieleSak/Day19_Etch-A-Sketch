from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_drawing():
    tim.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_counter_clockwise)
screen.onkeypress(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
