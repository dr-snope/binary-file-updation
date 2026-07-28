import pickle
f=open('abcd.dat','rb')
x=[]
while True:
    try:
        l=pickle.load(f)
        x.append(l)
    except EOFError:
        break
print(x) 
f.close()