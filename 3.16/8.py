# 입력 3개 최소값을 출력 단 조건 연산자를 이용하여 코드를완성하시오
a,b,c=map(int,input("입력3개:").split())

max_1=c if c<a else a if a<b else c if c<a else a
print(f"최소값:{max_1}")
