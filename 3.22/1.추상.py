#추상클래스       추상클래스에선 객체 생성 불가
from abc import *
class A(metaclass=ABCMeta):
    @abstractmethod
    def 추상메소드(self): #추상메소드가 있는 부분이 추상클래스이다
        pass
class B(A): #B가 A를 상속받아 추상메소드를 가지고 있으므로 객체 생성 불가
    def 추상메소드(self):
        print("오버라이딩")

        
