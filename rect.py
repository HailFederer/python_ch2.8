# Rect

class Rect:

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def area(self):
        return self.x * self.y
