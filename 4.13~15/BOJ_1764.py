person_l={}
heard_seen_count=0
heard_seen_l=[]
number_heard, number_seen=map(int,input().split())
for i in range(number_heard):
    person=input()
    person_l[person]="heard"
for i in range(number_seen):
    person=input()
    if person in person_l.keys():
        person_l[person]="heard&seen"
        heard_seen_count=heard_seen_count+1
    else:
        person_l[person]="seen"
print(heard_seen_count)
for i,j in person_l.items():
    if j=="heard&seen":
        heard_seen_l.append(i)
for i in sorted(heard_seen_l):
    print(i)
"""
number=input().split()
number=int(number[0])+int(number[1])
person_count=[]
person=[input() for i in range(number)]
person_l=list(set(person))
person_count=[person.count(person_l[i]) for i in range(len(person_l))]
person_l_dic=dict(zip(person_l,person_count))
print(person_count.count(2))
for i,j in person_l_dic.items():
    if j==2:
        print(i)
"""