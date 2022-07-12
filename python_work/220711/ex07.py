cnt = 100
i = 100
def doA():
    cnt = 0
    print('지역변수',cnt)

doA()
print('전역벽수',cnt)

def doB():
    for i in range(10):
        print(i)
    print('결과 = ',i)

doB()
print(i)

