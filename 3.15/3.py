#입력:1.1,2.1,3,4   출력:1.1+2.1+3+4=?
#1.각각 변경

a,b,c,d=input("입력(구분자==공백):").split(",")
print("입력:",end="")
print(float(a),float(b),int(c),int(d))

e=float(float(a)+float(b)+int(c)+int(d))
print("출력:",end="")
print(float(a),"+",float(b),"+",int(c),"+",int(d),"=",e,sep="")

#2.map(eval)

a,b,c,d=map(eval,input("입력:").split(","))
print(f"출력:{a}+{b}+{c}+{d}={a+b+c+d}")