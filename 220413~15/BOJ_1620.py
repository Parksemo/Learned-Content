N, M = map(int,input().split())
monster_number={}
number_monster={}
answer_l=[]
for i in range(1,N+1):
    monster=input()
    monster_number[monster]=i
    number_monster[i]=monster
for i in range(M):
    question=input()
    if question in monster_number:
        answer_l.append(monster_number[question])
    elif int(question) in number_monster:
        answer_l.append(number_monster[int(question)])
for i in answer_l:
    print(i)