import random


# from turtle import Turtle

class Food:
    def __init__(self, t3):
        self.t3 = t3
        self.food()

    def food(self):
        self.t3.color('yellow')
        self.t3.shapesize(0.5)
        self.t3.penup()
        while True:
            x = random.randint(10, 230)
            y = random.randint(10, 230)
            if x % 10 == 0 and y % 10 == 0:
                break
        self.t3.goto(x, y)
