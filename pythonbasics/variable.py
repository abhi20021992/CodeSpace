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


#conversion notes
#bool() will convert all value to true except 0, 0.0, '', "",None, {}, []
print(bool(None))

print(5 > 5)


#slicing a string 
name = 'my name is abhishek'
print(name[0:7:2]) # syntax is start : end : gap or skip 

#concatnation 

print(f'my number is {5}')
print(f'my number is {5 * 4}')

print("my num is {}".format(5*3))

#multi line string is done by ''' string ''' or same with double quote


#bytes object is repersented by b at the start 
byt = bytes(3)
print(byt) #b'\x00\x00\x00'

print(byt.decode('utf-8'))







