class A:                              #부모
    def __init__(self,x):
        print("A생성자 동작")
        self.x=x
    def f(self):
        print("A의 함수")

class B(A):                            #자식
    def __init__(self):
        super().__init__(10)       #super를 통해 부모클래스를 사용  super(B,self).__init__(10)
        print("B생성자 동작")
    pass
a=B()
print()
b=A(10)
print()
b.f()
print(b.x)
print(a.x)     #super를 통해 에러해결

