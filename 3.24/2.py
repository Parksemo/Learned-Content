import pickle
class A:
    def __init__(self,x):
        self.l=list(range(x))
    def __str__(self):
        return f"[{self.l}]"
    
class B:
    pass

c=pickle.load(open("data.p","rb"))
a=A(10)
print(a)
b=B()
pickle.dump(b,open("data.p","wb")) #dump는 데이터를 직렬화해서 저장할때 사용
                                   #pickle은 바이너리 사이즈를 한줄씩 쫘악 늘려서 쓰게한다(직렬화)
                                   #역직렬화를 통해 채우고 직렬화를 통해 읽는다?
