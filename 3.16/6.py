#산술연산계산기

a,b,c=input("입력:").split()
if b=="+":
    end=int(a)+int(c)
elif b=="-":
    end=int(a)-int(c)
elif b=="*":
    end=int(a)*int(c)
elif b=="//":
    end=int(a)//int(c)
elif b=="/":
    end=int(a)/int(c)
elif b=="%":
    end=int(a)%int(c)
else:
    end="연산불가"

print(f"정답 : {a}{b}{c}={end}")
print("정답 : {}{}{}={}".format(a,b,c,end))
print("정답 : %s%s%s=%d"%(a,b,c,end))







