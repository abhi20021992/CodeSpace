list = [1,2,3] #exactly as array in js
print(list)

list = ['1', '2', '3']
print(list)

list = [1, '2', True]
print(list)

list = [1, '2', True, [1, '2', True, [1, '2', True]]]
print(list)

print(len(list))
print([1,2]==[2,1])# false order matters
print([1,2]==[1,2])# true as same order


set = { 1, 2, 3, 4}
print(set)

set = { 1, 1, 4, 4}
print(set)

#set = { {1,2,3}, 2, 5}
#print(set) # error as set can not be hashed as a key

print({1,2}=={2,1})# true order not matters
print({1,2}=={1,2})# true as same order

tuples = tuple(list)
print(tuples) #tuples cant be modified also order of element matters in tuples
#like constants memory equal to amount of data is used

print(len(tuples))


dicto = dict() # you can use {} as initialize exaclty as our object in js
dicto.update({'tes': 'new'})
print(dicto)


#range() use to create a range of array 
print(range(10))
# append() add item in list at last 
# insert(x) to insert at a position x
# remove(item) remove if available or through error
# pop() remove top item from the list
# copy() used like array.copy() will create a copy of array
myset = {1,2,3};
print(myset)

myset.pop();
print(myset)

myset.discard(2)
print(myset)


#tuples 
#they are not mutable and memory and operaiton effecient and mostly used by return in function
myTuple = 1,2,3# also a tuple , avoid using this as lead to confusion 
print(myTuple)

def returnMultiple():
    return 1,2,3

print(returnMultiple())

#like array or object destructuring in js we can also de structre in python
a,b,c = returnMultiple()
print(a,b,c)# a will assign to 1 and so on respectively

#dict
di= { a:'afasd', b: 'dsfas'}
print(di.get(a))

#defaultDict belong to collection and use to solve default get() return issue when the key is not there and inner key value is a complex object

# list comprenhension 

myList = [1,2,3,4]
print([2*item for item in myList]) 

#using fileter and function is comprehension 
myList = range(10)
print([item for item in myList if item % 2 != 0])


#we can nest list comprehension inside another
mySample = [('a', 1),('b', 2),('c', 3)]
dic = {key:value for key, value in mySample} #creating object using correct list of tuples
#key and value are unpacked from tuples and assigned same as destructuring in js
print(dic)


