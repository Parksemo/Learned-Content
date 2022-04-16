import pickle
pickle.dump([1,2,3,4,5],open("data.p","wb")) #pickle은 바이너리로 읽거나 써야됨 wb rb
i_f=open("data.p","rb")
l=[]
try:
    for i in range(100):  #실제로는 5개만있는데 100번꺼내온다고하면 에러가 뜨지만
                          #try except를 통해 종료 포인트를 만들수 있다.
        l.append(pickle.load(i_f))
except:
    print("예외처리")

print(l)


