#5개의 정수를 입력하여 절대값을 취하고 합한다.

n=0
for i in range(5):
    n+= abs(int(input(f"{i+1}번째 입력:")))  #abs는 절대값을 만든다.
print(n)

n=0
nl=map(int,input("5개 정수 입력(구분자 공백)").split())
for i in nl:
    n+=abs(i)
print(n)

i1=0
i1+=abs(int(input("입력")))
i1+=abs(int(input("입력")))
i1+=abs(int(input("입력")))
i1+=abs(int(input("입력")))
i1+=abs(int(input("입력")))
print(i1)

