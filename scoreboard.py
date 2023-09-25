from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        with open('high.txt') as initfile:
            self.high = int(initfile.read())
        self.goto(-100, 250)
        self.write(f'Score: {self.score}, High Score: {self.high}', font=('Arial', 20, 'normal'))

    def print_score(self):
        self.clear()
        self.write(f'Score: {self.score}, High Score: {self.high}', font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1

    def game(self):
        self.goto(-80, 0)
        self.write('GAME OVER', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.high:
            self.high = self.score
        with open('high.txt', mode='w') as file:
            file.write(f'{self.high}')
        self.score = 0
        self.print_score()

    def reset_high(self):
        with open('high.txt', mode='w') as file:
            self.high = 0
            file.write(f'{self.high}')
        print('hi')





