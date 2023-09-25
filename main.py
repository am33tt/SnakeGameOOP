import time
import turtle
from turtle import Turtle, Screen

from check import Check
from direction import Direction
from food import Food
from make_snake import MakeSnake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

t3 = Turtle('square')

make_snake = MakeSnake()
direction = Direction(make_snake.objects)

playing = True


def quit_game():
    global playing
    playing = False
    turtle.done()
    screen.bye()


speed = 0.1
score1 = ScoreBoard()
make_snake.initiate()

# change Direction
screen.listen()
screen.onkey(direction.up, 'w')
screen.onkey(direction.down, 's')
screen.onkey(direction.right, 'd')
screen.onkey(direction.left, 'a')
screen.onkey(quit_game, 'x')
screen.onkey(score1.reset_high, 'q')

food = Food(t3)
check = Check(make_snake.objects, food.t3)

while playing:
    # -300 < make_snake.objects[0].xcor() < 300 and -300 < make_snake.objects[0].ycor() < 250 and
    screen.update()
    time.sleep(speed)
    make_snake.helo()

    if check.check1():
        score1.increase_score()
        food.food()
        score1.print_score()
        make_snake.make_seg()

    # high = High(score1.score)

    if (make_snake.objects[0].xcor() < -250 or make_snake.objects[0].xcor() > 250 or make_snake.objects[0].ycor() < -250
            or make_snake.objects[0].ycor() > 250):
        # high.create_high()
        # high.print_high()
        score1.reset()
        make_snake.reset()
        # playing = False

    make_snake.objects[0].fd(10)

screen.exitonclick()
