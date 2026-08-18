import pickle
with open('abcd.dat','rb') as file:
    data:list[list[int]] = []
    while True:
        try:
            data_pair:list[int] = pickle.load(file)
            data.append(data_pair)
        except EOFError:
            break
    print(data) 