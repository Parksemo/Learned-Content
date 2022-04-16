N = int(input())
value=[]
value_dict={}
for i in range(N):
    value.append(input().split())
    value_dict[value[i][0]]=value[i][1]
input_value=input()
print(value_dict.get(input_value,"Unknown Country"))