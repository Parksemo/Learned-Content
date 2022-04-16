import pickle

w_f=open("save_data.p","wb")
l=[1,2,3,4,5,6,7,8,9]
dic=dict.fromkeys(l,"data")
pickle.dump(l,w_f)
pickle.dump(dic,w_f)
w_f.close()


i_f=open("save_data.p","rb")
c=pickle.load(i_f)
print(c)
d=pickle.load(i_f)
print(d)


