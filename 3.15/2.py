"""
a=input("정수입력(구분자==공백):").split()
#input으로 값은 문자열로 받아진다.
#split은 값을 나눌때 사용

a,b,c,d=map(int,input("정수 4개입력(구분자==공백):").split())
#map은 반복되어 각각 부여하려고 할때 사용
#입력받은 문자를 숫자로 변경
print(type(a))

a,b,c,d=map(eval,input("정수 4개입력(구분자==공백):").split())
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#eval은 다양한 자료형을 한번에 받아줄 수 있는 기능을 한다.

"""









