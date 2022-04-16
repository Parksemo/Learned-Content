입력할숫자개수=int(input())
입력한숫자=[]
for i in range(입력할숫자개수):
    입력한숫자.append(int(input()))
정렬된숫자=sorted(입력한숫자)
if 입력할숫자개수==len(입력한숫자):
    for i in range(입력할숫자개수):
        print(정렬된숫자[i])