import re #정규화
#.문자
#^시작
#$끝

def print_t(str):
    if str:
        print("일치문자",str.group())
        print("입력문자", str.string)
        print("일치문자시작", str.start())
        print("일치문자끝", str.end())
        print("일치문자 시작,끝", str.span())
    else:
        print("일치 없음")


l=["casdfd","cabcdd","c1234d","cddddd"]
ck=re.compile("^c....d$")

for i in l:
    str=ck.match(i)
    print_t(str)
    str=ck.search(i)
    print_t(str)
    print("all_data",ck.findall(i))

#print(ck.match("")) #해당문자가 처음시작부터 일치하는지
#print(ck.search("")) #해당문자가 있는지
#print(ck.findall(""))# 해당문자를 전부다 찾는것
#원하는 형태에 따른 문자열 선택:정규식


