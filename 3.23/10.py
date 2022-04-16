import pickle
pickle.dump([1,2,3,4,5],open("data1.p","wb"))
try:
    tk=open("data1.p","rb")
except:
    print("예외")
    x=[]
else:
    x=pickle.load(tk)
    print("예외 미발생시 동작")
    tk.close()

finally:       #except에서도 문제가 발생할 수있기에 finally를 통해 반드시 실행되게 할수있다.
    print("반드시 실행되는 블록")

