import random
import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

t = Turtle('square')
t.color('white')
t.shapesize(0.5)
t.penup()
t.speed(1)

objects = [t]



def make_seg():
    x = objects[len(objects) - 1].xcor()
    y = objects[len(objects) - 1].ycor()
    t = Turtle('square')
    t.color('grey')
    t.shapesize(0.5)
    t.penup()
    t.speed(1)
    if objects[0].heading() != 90 and objects[0].heading() != 270:
        new_x = x - 10
        new_y = y
    else:
        new_x = x
        new_y = y - 10

    t.goto(new_x, new_y)
    objects.append(t)


screen.update()

t3 = Turtle('square')
t3.color('red')
t3.shapesize(0.5)


def food():
    while True:
        x = random.randint(10, 230)
        y = random.randint(10, 230)
        if x % 10 == 0 and y % 10 == 0:
            break
    t3.penup()
    t3.goto(x, y)


food()


def check():
    if objects[0].xcor() == t3.xcor() and objects[0].ycor() == t3.ycor():
        # make_seg()
        # food()
        return True
    elif abs(objects[0].xcor() - t3.xcor()) < 3 and abs(objects[0].ycor() - t3.ycor()) < 3:
        # make_seg()
        # food()
        return True
    else:
        return False


def helo():
    for seg in range(len(objects) - 1, 0, -1):
        new_x = objects[seg - 1].xcor()
        new_y = objects[seg - 1].ycor()
        objects[seg].goto(new_x, new_y)


# Directions function
def up():
    if objects[0].heading() != 270:
        objects[0].setheading(90)


def down():
    if objects[0].heading() != 90:
        objects[0].setheading(270)


def right():
    if objects[0].heading() != 180:
        objects[0].setheading(0)


def left():
    if objects[0].heading() != 0:
        objects[0].setheading(180)


playing = True
score = 0
speed = 0.1
while -300 < objects[0].xcor() < 300 and -300 < objects[0].ycor() < 300:
    screen.update()
    time.sleep(speed)
    helo()
    if check():
        make_seg()
        food()
        score += 1
        speed -= 0.002
    # print(objects[len(objects) - 1].heading())
    objects[0].fd(10)
    screen.listen()
    screen.onkey(up, 'w')
    screen.onkey(down, 's')
    screen.onkey(right, 'd')
    screen.onkey(left, 'a')


t5 = Turtle()
t5.hideturtle()
t5.color('white')
t5.goto(-100,0)
t5.write(f'Oops!\nYour Score: {score}', font=("Calibri", 20, "normal"))

screen.exitonclick()
