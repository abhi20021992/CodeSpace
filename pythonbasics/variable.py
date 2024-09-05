#premitive types

x = 10
print(x)
print(type(x).__name__)


x = 'test abhishek'
print(x)
print(type(x).__name__)

x = 1.5
print(x)
print(type(x).__name__)

x = True
print(x)
print(type(x).__name__)

x = None
print(x)
print(type(x).__name__)

print(True + 1) #type casting happens here as well True to 1 and False to 0
print( '1' + '1') #type casting not happens here as both are same data type
print(1.9 + 1) #normal addition
#print('1' + 1)# error will come here


print(20/19) # always return float

print(int(20/19)) #they just extract the int out of the fload but it will not roud it, to do that you have to round it using round()

print(1.2-1.0)#0.19 wrong use decimal module rather than float as they have floating error



