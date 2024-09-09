#filesystem is directly read via os so os need to know the details of the file required

f1 = open('pythonbasics/data.txt', 'r')


l1 = ''.join(f1.readlines())
print(l1)

f2 = open('pythonbasics/data.txt', 'w+')

f2.write('new data for file')

f2.close()

#as closing the file opened is tidious task, we should use with statment and do all the operaiton inside with block so that
# files will be closed 

with open('pythonbasics/data.txt', 'w') as f:
    f.write('again a with file ')
    
import csv 
    
with open('pythonbasics/data.csv', 'r') as f:
    read = csv.reader(f, delimiter='\t')
    for r in read:
        print(r)
        
#when you want to write value to csv you just have to creat a writer reference also we need to pass file as input with delimeeter


import json

with open('pythonbasics/data.json', 'r') as j:
    dat = json.loads(''.join(j.readlines()))
    json.dumps(dat)