class A:#클래스 선언
    def __init__(self): #생성자 괄호안에 self는 꼭 기입해야한다.
        print("생성자 A동작")

a=A()
a=A()


print()


class B:#클래스 선언
    def __init__(self,x): # x라는 입력 받을 객체 선언
        print("생성자 B동작")

b=B(10)
b=B("류성빈")


print()


class C:#클래스 선언
    필드=0 #클래스필드
    def __init__(self,x=10): # x라는 입력 받을 객체 선언
        print("생성자 C동작")
        self.필드=x #인스턴트 필드

c=C()
print(c.필드)
c.필드=30
print(c.필드)
c=C(20)
print(c.필드)


print()


class M:
    def __init__(self):
        print("생성자 동작")
    def 메서드1(self):
        print("메서드1 동작")
    def 메서드2(self,x):
        print(x,"입력을 받는 메서드2 동작")
    def 메서드3(self):
        print("메서드3 동작")
        return 10
    def 메서드4(self,x,y):
        print(x,y,"입력을 받는 메서드4 동작")
    def 메서드5(self,x):
        return f"{x}를 입력받는 메서드5 동작"

m=M()
m.메서드1()
m.메서드2(10)
m.메서드3()
print(m.메서드3())
m.메서드4(10,10)
print(m.메서드5(10))


print()



