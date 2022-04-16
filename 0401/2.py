import requests
r=requests.get("http://www.hanbit.co.kr/store/books/full_book_list.html")
print(r.status_code) #200이면 정상
print(r.raise_for_status()) #문제가 있는지
#print(r.text)
with open ("data.html","w",encoding="UTF-8") as f:
    f.write(r.text)
