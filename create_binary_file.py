import pickle
with open('abcd.dat','wb') as file:
    record_num:int = int(input('Enter number of records to be entered: '))
    for num in range (record_num):
        roll_no:int = int(input('Enter roll no: '))
        marks:int = int(input('Enter marks: '))
        data_pair:list[int] = [roll_no,marks]
        pickle.dump(data_pair,file)
        print(f'Number of records entered: {num+1}')
