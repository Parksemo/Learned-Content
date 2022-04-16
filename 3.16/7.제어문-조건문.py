a,b =map(int,input("입력").split())
if a>b:
    max_v=a
    min_v=b
else:
    max_v = b
    min_v = a
print(f"최대값:{max_v}\n최소값{min_v}")
#여기서 f는 에프스트링이다.

#참값 if 조건 else 거짓값->
max_v=b if a<b else a
min_v=a if a<b else b
print(f"최대값:{max_v}\n최소값{min_v}")