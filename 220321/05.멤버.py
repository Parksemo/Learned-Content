class 클래스이름:
    클래스필드="클래스필드"
    def __init__(self):
        self.인스턴스필드="인스턴스필드"  #인스턴스는 self로 만들어진다. 주로 생성자를 통해 만든다.
    def 인스턴스메소드(self):
        self.인스턴스필드2="data"


print(클래스이름.클래스필드)
#print(클래스이름.인스턴트필드) -> 에러  클래스를 통해 인스턴스필드를 만들어야 된다.
인스턴스=클래스이름()
print(인스턴스.인스턴스필드)
#print(인스턴스.인스턴스필드2) -> 에러   이는 인스턴스메소드를 호출해야 된다.
인스턴스.인스턴스메소드()
print(인스턴스.인스턴스필드2)
#print(클래스이름.인스턴스필드)  -> 에러


print()


class A:
    c_f=0
    def __init__(self):
        self.i_f=100
print(A.c_f)
a=A()
print(a.i_f)
print(a.c_f)
a1=A()
print(a1.i_f)
print(a1.c_f)
A.c_f=300
print(A.c_f)
print(a.c_f)
print(a1.c_f)
a.c_f=20
print(A.c_f)
print(a.c_f)
print(a1.c_f)
A.c_f=100
print(A.c_f)
print(a.c_f)
print(a1.c_f)


