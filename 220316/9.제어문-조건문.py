#두수를 입력해서 더 큰수는 10을 나눈 몫을, 작은수는 10을 곱한 수를 출력하라
a,b=map(int,input("두수를 입력:").split())

if a<b:
    c=a*10
    d=b//10
elif a>b:
    c=a//10
    d=b*10

print(f"입력 {a} {b}\n출력 {c} {d}")