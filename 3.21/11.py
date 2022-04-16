class A:
    def __init__(self):
        print("A의 생성자동작")

class B(A):
    def __init__(self):
        super().__init__()
        print("B의 생성자동작")

class C(A):
    def __init__(self):
        super().__init__()
        print("C의 생성자동작")

class D(B,C):                #다중상속
    def __init__(self):
        super().__init__()
        print("D의 생성자동작")

D()


#다중 상속에서는 D와 가까울수록 가까운 부모가 된다. 그래서 D ->B->C->A로 호출되고 A->C->B->D 순서가됨.


