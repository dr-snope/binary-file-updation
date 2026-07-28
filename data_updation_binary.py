import pickle
f=open('abcd.dat','rb')
a=int(input('Enter target roll no: '))
b=int(input('Enter marks to be added: '))
found = False
x=[]
y=[]
while True:
    try:
        l=pickle.load(f)
        x.append(l)
    except EOFError:
        break
for i in x:
    if int(i[0])==a:
        y.append([i[0],int(i[1])+b])
        found = True
    else:
        y.append(i)
f.close()
f=open('abcd.dat','wb')
for i in y:
    pickle.dump(i,f)
f.close()
if found:
    print("Record updated successfully")
else:
    print("Roll number not found")