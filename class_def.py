# 파이썬 클래스 정의 테스트


class MyString:
    pass


s = MyString()
s.a = 10
print(s.a)
print(type(s))
print(MyString.__bases__)

s2 = ''
print(type(s2))
print(str.__bases__)
