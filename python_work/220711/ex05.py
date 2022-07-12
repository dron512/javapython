'''
page 181
문제 1
구구단의 7단을 거꾸로 출력하는 코드를 for 루프와 range 기반으로 만들어 보자. 단 출력 내용으로는
다음과 같이 결과만 보이기로 하자
63 56 49 42 35 28 21 14 7

문제2
다음 튜플을 만들어보자 이 튜플은 1부터 시작해서 100까지 증가한다. 그리고 다시 1씩 줄어들어서
마지막에 1로 끝난다
(1,2,3,4,5,6,7,...97,98,99,100,99,98,97,96,,,5,4,3,2,1)
'''

# for i in range(9,0,-1):
#     print(i*7,end=" ")

print()

a = []
for i in range(1,101):
    a.append(i)

a = tuple(a)
b = [i for i in range(99,0,-1)]
b = tuple(b)
c = a+b
# print(c)

import numpy as np

a = np.arange(1,10)
print(list[a])

a = [i for i in range(1,10)]
print(a)


'''
    >>> for i in range(3):
        ________________________
    1,2,3
    2,3,4
    3,4,5
    그리고 동일한 실행결과를 보이도록 빈 문장을 채워보자
'''