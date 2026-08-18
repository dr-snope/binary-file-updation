import pickle

with open('abcd.dat','rb') as file1:
    target:int = int(input('Enter target roll no: '))
    increment:int = int(input('Enter marks to be added: '))
    found:bool = False
    original_data:list[list[int]] = []
    modified_data:list[list[int]] = []
    while True:
        try:
            data_pair:list[int] = pickle.load(file1)
            original_data.append(data_pair)
        except EOFError:
            break
    for data_pair in original_data:
        if int(data_pair[0]) == target:
            modified_data.append([data_pair[0],int(data_pair[1])+increment])
            found = True
        else:
            modified_data.append(data_pair)

with open('abcd.dat','wb') as file2:
    for data_pair in modified_data:
        pickle.dump(data_pair,file2)

if found:
     print("Record updated successfully")
else:
    print("Roll number not found")