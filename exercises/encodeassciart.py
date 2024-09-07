from collections import Counter

sample = 'AAAAABBBCC'
sample2 = [('W', 5), ('L', 3), ('K', 2)]    
def encodeString(stringVal):
    return list({char: cout for char, cout in Counter([char for char in stringVal]).items()}.items())


def decodeString(encodedList):
    return ''.join([ ''.join([char for item in range(count)]) for char, count in encodedList])

print(encodeString(sample))

print(decodeString(sample2))