class Check:

    def __init__(self, list, t3):
        self.list = list
        self.t3 = t3

    def check1(self):
        if self.list[0].xcor() == self.t3.xcor() and self.list[0].ycor() == self.t3.ycor():
            return True
        elif abs((self.list[0]).xcor() - self.t3.xcor()) < 3 and abs(self.list[0].ycor() - self.t3.ycor()) < 3:
            return True
        else:
            return False

