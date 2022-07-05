'''
    문제3
    앞서 본문에서 리스트에 저장된 내용 전부를 삭제하는 clear함수를 소개하였다.
    그리고 그 사용방법은 다음과 같다
    st=[1,2,3,4]
    st.clear()
    st
    []

    그런데 이렇듯 리스트에 저장된 값을 싹 비우는 방법을 앞서 5장에서도 소개한바 있다.
    슬라이싱 연산을 이용하는 방법인데 이 방법을 이용하는 형태로 위의 코드를 소개해보자
'''
st=[1,2,3,4]
st[:] = []
print(st)

'''
    문자열 The Espresso Sprit 
    대문자로 소문자 원본그대로 한
'''
st = 'The Espresso Sprit'
print(st.upper())
print(st.lower())
print(st)

cnt = 0
for i in st:
    if i=='E':
        print(i)
        print(cnt)
    cnt+=1
print(st.find('E'))

myst = "한글입니다.\n잘되네요."
print(myst)
myst = "한글입니다.\t잘되네요."
print(myst)
myst = '한글입니다."잘되네요.'
print(myst)
myst = "한글입니다.'잘되네요."
print(myst)

mylist= [1,2,3,4,5]
del mylist[3:]
print(mylist)

del mylist
print(mylist)