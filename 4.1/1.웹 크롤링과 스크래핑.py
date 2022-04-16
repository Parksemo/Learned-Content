from urllib.request import urlopen
f=urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
print(f.read())

print(r"data\ndata2") #r""는 문자그대로 다 들고옴
print("data\ndata2")

