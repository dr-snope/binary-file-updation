import pickle
f=open('abcd.dat','wb')
n=int(input('Enter number of records to be entered: '))
for i in range (n):
    r=int(input('Enter roll no: '))
    m=int(input('Enter marks: '))
    x=[r,m]
    pickle.dump(x,f)
    print(f'Number of records entered: {i+1}')
f.close()