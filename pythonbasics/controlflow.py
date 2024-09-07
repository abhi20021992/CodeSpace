#if else
a = True
if a:
    print('true')
elif a:
    print('false')
else:
    print('else')
    
    
for a in [1,2,3,4]: #works only with iterable this in is not in operator its part of for syntax
    print(a) #a is only in the scope of for loop not be able to access outside
    
    
while a < 5:
    print(a)
    a = a+1


#pass is a key word used as not implemente method and it passees loops or other control flow statement
#break is also there to break out of first loop 
#continue skips every thing else below it


#for / else structure , if we put any break statement in the loop like while or for we can use else with them to do action if brek will not happne
# for num in range(1, 100):
#     if(num %10 ==0):
#         break;
# else: 
#     print('Prime number')

# def allPrimesUpTo(num):
#     foundPrime = [2]
#     for digit in range(2, num):
#         for item in foundPrime:
#             if(digit % item == 0):
#                 break;
#         else:
#             foundPrime.append(digit)
#     return foundPrime
# we can see here that we can write this programe as below if we dont use for ealse loop
# def allPrimesUpTo(num):
#     foundPrime = [2]
#     for digit in range(2, num):
#         isPrime = False
#         for item in foundPrime:
#             if(digit % item == 0):
#                 isPrime = False
#                 break;
#             isPrime = True
#         if isPrime:
#             foundPrime.append(digit)
#     return foundPrime


    
    
