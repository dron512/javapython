def doSum():
    sum = 0
    for i in [1,2,3,4,5,6,7,8,9,10]:
        sum += i
    return sum

def doSumRange():
    sum = 0
    for i in range(1,11):
        sum += i
    return sum

result = doSum()
print('result = ',result)

result = doSumRange()
print('result = ',result)