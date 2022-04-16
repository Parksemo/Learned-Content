class Ec(Exception): #예외가 담겨진 클래스 형성
    def __str__(self):
        return "나만의 예외발생"
def f():
    raise Ec()
def d():
    #f()
    raise Exception("의미")
try:
    f()
    #d()
    #10/0
except Exception as e: #예외가 발생한 원인을 출력한다.
    print("예외")
    print(e)