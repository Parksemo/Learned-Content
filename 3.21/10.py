class A:
    def __init__(self):
        print("A의 생성자 동작")
    def __f(self):
        print("나만 쓰는 함수")
    def g(self):
        self.__f()
    def c(self):
        pass

class B(A):
    def __init__(self):
        super().__init__()
        print("B의 생성자 동작")
    def a(self):
        super(B, self).g()

class C(B):
    def __init__(self):
        super().__init__()
        print("C의 생성자 동작")

a=C()

