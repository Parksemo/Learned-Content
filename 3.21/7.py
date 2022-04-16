class A:
    __x="data"
    def __init__(self):
        self.__x=0
    @classmethod
    def f(cls):
        print(cls.__x)
a=A()
#a.__x=10
#print(a.__x)
#a.__f()
#print(A.__x)
A.f()

#__을 통해 은닉할 수있다. 나머지는 다 에러가 발생하고 @classmethod를 통해서 __ 사용가능