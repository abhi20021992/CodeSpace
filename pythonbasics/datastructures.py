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


