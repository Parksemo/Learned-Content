N,M=map(int,input().split())
girl_group={}
answer=[]
for i in range(N):
    group=input()
    group_number=int(input())
    for j in range(group_number):
        member=input()
        girl_group[member]=group
for i in range(M):
    group_member_q=input()
    number_q=int(input())
    if number_q==0:
        for j,k in girl_group.items():
            if k==group_member_q:
                answer.append(j)
        for j in sorted(answer):
            print(j)
        answer=[]
    elif number_q==1:
        for j,k in girl_group.items():
            if j==group_member_q:
                print(k)