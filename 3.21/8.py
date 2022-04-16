# set_f과 get_f을 통해 __ 사용가능
class A:
    def __init__(self):
        self.__x=0
    def set_f(self,x):
        self.__x=x
    def get_f(self):
        return self.__x

a=A()
#a.__x=20
a.set_f(20)
print(a.get_f())

