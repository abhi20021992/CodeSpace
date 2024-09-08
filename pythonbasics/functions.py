def printFn(data): #param is optional
    print(data)
    return data * 3 # return is optional

print(printFn(20))


print(print('test')) #None is returned , same as absence of value and is a None type equals undefined in js

#def __init__(self) -> None #ways to predefine the return type of function

# passing list of argument and positional arguments 

#myfunction(*arguments , **positionalArguments) by default in python we name them as *args and **kwargs

def calculator(*args, **kwargs):
    print(args, kwargs)
    
    
calculator(1,2,3,4,5, operation = 'sum')  #(1, 2, 3, 4, 5) {'operation': 'sum'} kwargs are dictionary and args are tuples by default


#scopes in python is same as in js , every programe search locally first and then 
#there are two funciton to see local and global variables locals() and globals() 
print(locals(), globals())

#passing function as variables in python is same as in cse of js
#we can also use function array [fun1, fun2] and then loop through it and call it
#also we can chain the function like in js
#there is a key word calld lambda and we can creat a one line function and like lembda in java
print((lambda x: x * 3)(10)) #30 basically these functiona are like mini function values passed same as callback in js

