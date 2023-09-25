from turtle import Turtle

with open("", mode='w') as file:
    file.write('Ola')


class High(Turtle):
    def __init__(self, score):
        super().__init__()

        self.penup()
        self.score = score
        self.high = 0
        self.color('white')
        self.hideturtle()
        self.goto(100, 250)

    def create_high(self):
        if self.score > self.high:
            self.high = self.score
        self.score = 0
        # self.write(f'High Score: {self.high}', font=('Arial', 10, 'normal'))

    def print_high(self):
        self.clear()
        self.write(f'High Score: {self.high}', font=('Arial', 10, 'normal'))

