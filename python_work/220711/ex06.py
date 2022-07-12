
a = 0
a += 1
def funcA():
    print(a)

def funcLocalA(n):
    print(n)

funcA()
funcLocalA(10)
print(a)
# print(n)