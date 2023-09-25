from turtle import *

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)


class MakeSnake:

    def __init__(self):
        self.objects = []
        self.make_seg()
        self.helo()

    def initiate(self):
        t1 = Turtle('square')
        t1.color('white')
        t1.shapesize(0.5)
        t1.penup()
        t1.speed(1)
        self.objects.append(t1)

    def make_seg(self):
        if len(self.objects) >= 1:
            x = self.objects[len(self.objects) - 1].xcor()
            y = self.objects[len(self.objects) - 1].ycor()

            t = Turtle('square')
            t.color('grey')
            t.shapesize(0.5)
            t.penup()
            t.speed(1)

            # if self.objects[0].heading() != 90 and self.objects[0].heading() != 270:
            #     new_x = x - 10
            #     new_y = y
            # else:
            #     new_x = x
            #     new_y = y - 10

            # t.goto(new_x, new_y)
            t.goto(self.objects[-1].pos())
            self.objects.append(t)

    def helo(self):
        for seg in range(len(self.objects) - 1, 0, -1):
            new_x = self.objects[seg - 1].xcor()
            new_y = self.objects[seg - 1].ycor()
            self.objects[seg].goto(new_x, new_y)

    def reset(self):
        for hells in self.objects:
            hells.goto(1000,100)
        self.objects.clear()
        self.make_seg()
        self.initiate()



