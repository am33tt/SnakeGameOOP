class Direction:

    def __init__(self, lists):
        self.lists = lists

    def up(self):
        if self.lists[0].heading() != 270:
            self.lists[0].setheading(90)

    def down(self):
        if self.lists[0].heading() != 90:
            self.lists[0].setheading(270)

    def right(self):
        if self.lists[0].heading() != 180:
            self.lists[0].setheading(0)

    def left(self):
        if self.lists[0].heading() != 0:
            self.lists[0].setheading(180)
