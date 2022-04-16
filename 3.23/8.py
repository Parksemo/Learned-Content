l=[1,2,3,4,5]
try:
    x=l[5]
except:
    print("예외 발생")

#l[5]가 없는데 try except를 통해 예외처리를 하여 실행가능

l=[1,2,3,4,5]
try:
    x=l[5]  #예외발생
    print("동작")
    int("a") #예외발생   #예외처리는 예외가 발생하자마자 예외처리가 된다. x=l[5]에서 except문으로 넘어감
except:
    print("예외 발생")

print()

l=[1,2,3,4,5]
try:
    x=l[1]
    print("동작")
    int("류성빈")
    open()
except ValueError:
    print("값 예외 발생")
except IndexError:
    print("인덱스 예외 발생") #먼저 발생한 예외에 따른 문이 동작함
except Exception:  #Exception은 모든 예외를 포함한다 따라서 Exception은 젤 마지막에 넣어줘야
                    #ValueError IndexError 기능이 사용되어진다.
    print("예외")





