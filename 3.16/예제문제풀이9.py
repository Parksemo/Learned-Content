#1
n=int(input("정수입력:"))
for i in range(1,n+1):
    print("*"*i)

print()

#2
for i in range(n,0,-1):
    print("*"*i)

print()

#3
for i in range(1,n+1):
    print(" "*(n-i),"*"*i)


print()

#4
for i in range(n,0,-1):
    print(" "*(n-i),"*"*i)

print()

#5
for i in range(1,n+1):
    print("*"*i+" "*(n-i)+"*"*i)

