def allPrimesUpToWithoutForElse(num):
    foundPrime = [2]
    for digit in range(2, num):
        isPrime = False
        for item in foundPrime:
            if(digit % item == 0):
                isPrime = False
                break;
            isPrime = True
        if isPrime:
            foundPrime.append(digit)
    return foundPrime

def allPrimesUpToWithForElse(num):
    foundPrime = [2]
    for digit in range(2, num):
        for item in foundPrime:
            if(digit % item == 0):
                break;
        else:     
           foundPrime.append(digit)
    return foundPrime
 
print(allPrimesUpToWithForElse(100))
print(allPrimesUpToWithoutForElse(100))

# reslut will be same but one with for/else is much nicer and shorter then other