class 클래스이름:
    클래스필드="클래스필드"
    def __init__(self):
        self.인스턴스필드="인스턴스필드"  #인스턴스는 self로 만들어진다. 주로 생성자를 통해 만든다.
    def 인스턴스메소드(self):
        print("인스턴스메소드 동작")
        print(self.클래스필드, "에 접근")
        print(self.인스턴스필드, "에 접근")
    @classmethod
    def 클래스메소드(cls):
        print("클래스메소드동작")
        print(cls.클래스필드, "에 접근")
        #print(cls.인스턴스필드, "에 접근")

클래스이름.클래스메소드()        #클래스 -> 클래스멤버접근 가능
#클래스이름.인스턴스메소드() 에러  클래스 -> 인스턴스멤버접근 불가능
print()
인스턴스=클래스이름()
인스턴스.인스턴스메소드()


