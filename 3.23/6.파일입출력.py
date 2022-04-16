
w_f=open("data.txt","w",encoding="UTF-8") #encoding="UTF-8"을통해 한글문자도 저장할수있다
w_f.write("1234 data\n data2")
w_f.write("1234")  #이렇게 쓰기를 한번더하면 텍스트파일에서
                   # 지금위치한커서에 입력되면서 파이썬코드처럼 다음줄에입력되는것이 아니다.
w_f.write("안녕하세요")
print(w_f.writable())
print(w_f)


"""
i_f=open("data.txt","r",encoding="UTF-8") #읽을때또한 encoding="UTF-8"를 입력해야 한글을 읽어올수있다.
#print(i_f.readline())   #readline 한줄만 읽어옴
#print(i_f.readline())   #readlines 줄마다 가져오며 리스트형식으로 저장
for i in i_f:
    print(i)
"""
