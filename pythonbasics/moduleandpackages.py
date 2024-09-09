#within same folder we just need to import the funciton or complete file in module where you want to use it
# we can import any files which are present in pythonbasics folder directly 

#now to create a package we need to create a folder and put all the files related to the module and add a special 
#python file with name __init__.py , after this the complete package will work as module
#for example we created exercise as package by adding the special file 

from exercises import factorial

print(factorial.fact(10))