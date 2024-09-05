def fact(number):
    if number == 0 or number ==1:
        return 1
    return number * fact(number - 1)

print(fact(2))

print('2'+ '22')