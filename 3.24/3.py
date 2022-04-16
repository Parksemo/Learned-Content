class EX(Exception):
    def __str__(self):
        return "예외동작"
def f(x):
    if x==10:
        raise EX() #raise는 예외발생자로 메소드를 탈출하여 상위단으로 가게한다
    return

def d():
    f(11)
    pass
try:
    d()
    raise Exception("입력된 예외 메시지")
except EX as e:
    print(e)
except Exception as e:
    print(e)
    print("모든예외")

