'''
page 162
문제 1
다음은 구구단 중에서 7단을 출력하는 예제이다
for i in range(1,10):
    print(7*i,end=' ')

7 14 21 28 35 42 49 56 63
위의 예제에 continue 관련 코드를 넣어서 결과가 짝수인 경우에만 출력되도록 하자 즉 7은 출력되지 않고 14는 출력되어야한다.
    7곱하기 i가 짝수일때
'''
def doB():
    for i in range(1, 10):
        if (7*i) % 2 == 0:
            print(7*i, end=' ')
'''
    문제2
     2이상 100미만의 정수 중에서 2로도 나누어지지 않고 동시에 3으로도 나누어 지지 않는 수를 찾아서 출력하는 코드를
    while 루프를 기반으로 작성해보자
'''
def doA():
    print()
    num = 1
    while(num <100):
        num +=1
        if num%2==0 or num%3==0:
            continue
        print(num,end=' ')

'''
    문제3
    문제 2의 결과에서 continue를 사용하지 않았다면 이번에는 continue를 사용하는 방식으로 코드를 수정해보자.
    반대로 문제 2에서 continue를 사용했다면 이번에는 continue를 사용하지 않는 방식으로 코드를 수정해보자
'''

'''
page 165
이중 for 루프를 기반으로 구구단을 2단부터 9단까지 전부 출력하는 코드를 만들어보자
출력의 형태는 다음과 같이
'''
def doC():
    for dan in range(2,10):
        for i in range(1,10):
            print(dan*i,end=" ")
        print()
'''
    page 174
    튜플을 인자로 전달하면, 이를 리스트로 바꿔주는 함수를 만들어보자. 예를 들어서 to_list라는 이름으로
    함수를 만들었다면 다음과 같이 동작해야 한다
'''









