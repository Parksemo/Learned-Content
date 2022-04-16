class A:
    def f(self):
        print("A의 함수")
class B(A):
    def f(self):
        print("B의 함수")   #오버라이딩됨

a=B()
a.f()

#강아지 고양이 닭 이 세마리의 메소드를 정의하고 실행해서 강아지는 멍멍 고양이는 냐옹 닭은 꼬꼬댁할수있도록
# for i in l:
#     i.소리()

class 동물:
    def 소리(self):
        pass

class 강아지(동물):
    def 소리(self):
        return "멍멍"

class 고양이(동물):
    def 소리(self):
        return "냐옹"

class 닭(동물):
    def 소리(self):
        return "꼬끼오"

l=[강아지(),고양이(),닭()]
for i in l:
    print(i.소리())
