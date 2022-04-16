a=input().split('(^0^)')
b=a[0]
c=a[1]
b=b.replace('@=','1')
c=c.replace('=@','1')
print(f"{b.count('1')} {c.count('1')}")