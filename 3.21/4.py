"""
앨범

사진 이름 년도 날짜
"""

class 앨범:#클래스 선언
    사진=""
    이름=""
    년도=0
    날짜=0
    def __init__(self,사진1="1",이름1="2",년도1=3,날짜1=4):
        self.사진=사진1
        self.이름=이름1
        self.년도=년도1
        self.날짜=날짜1

    def f(self):
        print(f"사진:{self.사진}, 이름:{self.이름}, 년도:{self.년도}, 날짜:{self.날짜}")
a=앨범()
print(a.사진,a.이름,a.년도,a.날짜)
#1 생성자
a=앨범("이미지","이름",10,10)
print(a.사진)

#2 메서드
a.f()
#출력->사진=문자열, 이름:이름, 년도:년도, 날짜:날짜
