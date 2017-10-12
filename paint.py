from point import Point
from rect import Rect

def main():
    # bound_class_method()
    # test_other_method()
    # test_member()
    # test_constructor()
    # test_to_string()
    # test_to_string2()
    test_oerator_overloading()


def test_oerator_overloading():
    p1 = Point(100, 200)
    p2 = Point(50, 50)
    p3 = p1 + p2
    p4 = p1 - p2

    print(p3)
    print(p4)

    p3 += Point(-10, -10)
    p4 -= Point(-10, -10)
    print(p3)
    print(p4)

    print(Rect(10, 20) == Rect(20, 10))
    print(Rect(10, 10) > Rect(10, 5))
    print(Rect(10, 20) < Rect(20, 10))


def test_to_string():
    p = Point()
    print(p)

def test_to_string2():
    p = Point(10,20)
    print(p)
    print(str(p)+'11')

    p2 = eval(str(p))
    print(p2)

def bound_class_method():
    p = Point()
    p.set_x(10)
    p.set_y(10)
    print(p.get_x(), p.get_y(), sep=',')

def test_other_method():
    print(Point.static_method())
    print(Point.class_method())

def test_member():
    p = Point()
    Point.set_x(p, 100)
    Point.set_y(p, 100)
    print('x={0}, y={1}, count_of_instance={2}'.format(p.x, p.y, p.count_of_instance))

def test_constructor():
    p1 = Point(10, 20)
    print('x={0}, y={1}, count_of_instance={2}'.format(p1.x, p1.y, Point.get_count_of_instance()))
    p2 = Point(100, 200)
    print('x={0}, y={1}, count_of_instance={2}'.format(p2.x, p2.y, Point.get_count_of_instance()))
    del p1
    print('count_of_instance={0}'.format(Point.get_count_of_instance()))
    del p2
    print('count_of_instance={0}'.format(Point.get_count_of_instance()))


if __name__ == '__main__':
    main()

