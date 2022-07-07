'''
    문제1 0부터 시작해서 값을 하나씩 증가시키며 9까지 출력을 보이는 코드를 While 루프를 기반으로 작성해보자

    문제 2
    9에서부터 값을 하나씩 감소시키며 0까지 출력을 보이는 코드를 while 루프를 기반으로 작성해보자
'''


def doA():
    num = 0
    while num < 10:
        print("num = ", num)
        num += 1


def doB():
    num = 9
    while num > -1:
        print("num = ", num)
        num -= 1
doA()
doB()
