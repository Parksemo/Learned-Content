d=" da ta "
e="Aa"
print(len(d)) #공백또한 문자로서 글자수에 포함된다.
data=d.strip() #끝단의 공백을 없앤다
print(d)
print(len(data))
print(data)
print(d.isupper()) #전부 대문자인지 소문자인지
print(d.islower())
print(e.isupper())
print(e.islower())
#rstrip() lstrip() 오른쪽왼쪽 공백 삭제

print(e.upper()) #대소문자로 변경
print(e.lower())

f="data asdf"
print(f.title()) #공백을 기준으로 단어를 취급하여 앞글자만 대문자로 바꿔줌
print(f.capitalize()) #공백과 상관없이 맨앞글자만 대문자

g="data asdf exe 실행 동작 자료 분석 자료 석분"
print(g.count("data")) #그 문자의 갯수 파악
print(g.count("d"))
print(g.count("분"))

print(g.find("da")) #그 문자가 몇번째에 위치하는지 인덱스처럼 보면됨
print(g.find("분"))
print(g.rfind("분")) #오른쪽에서 그문자의 우ㅣ치를 찾는것 그 번호는 왼쪽에서 인덱스처럼

l="나는 ~~~ 다."
print(l.startswith("나는")) #해당 문자가 시작점에 위치하는지
print(l.startswith("다"))
print(l.endswith("나는")) #해당문자가 끝에 위치하는지
print(l.endswith("다."))

l1="나는 ~~~ 다"
print(l1.endswith("."))

