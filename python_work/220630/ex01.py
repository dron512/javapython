'''
exam01 
1,3,5,7,9 sum.... for

alt +shift + f 
'''
sum = 0
for i in range(1, 10, 2):
    print("i = ", i)
    sum = sum+i

print("sum", sum)

sum = 1
for i in range(1, 11):
    sum = sum * i
print(sum)

for i in range(1, 10):
    print(7, '*', i, '=', 7*i)


for i in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
    print(7, '*', i, '=', 7*i)

for i in range(9, 0, -1):
    print(7, '*', i, '=', 7*i)

for i in range(5):
    print("hi")
