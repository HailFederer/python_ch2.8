class Point:

    count_of_instance = 0

    # def __iadd__(self, other):
    #     return Point(self.x + other.x, self.y + other.y)
    #
    # def __isub__(self, other):
    #     return Point(self.x - other.x, self.y - other.y)

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        Point.count_of_instance += 1

    def __del__(self):
        Point.count_of_instance -= 1

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    def show(self):
        print('점({0},{1})을 그렸습니다.'.format(self.x, self.y))

    @staticmethod
    def static_method():
        return "static_method() 호출"

    @classmethod
    def get_count_of_instance(cls):
        return cls.count_of_instance

    def __str__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)




