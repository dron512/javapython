'''
page 243
문제1
친구의 이름과 전화번호 정보를 담을 수 있는 클래스를 만들어보자. 아래에서 보이는 내용과 동일한 흐름을 보이도록
클래스 Friend를 정의하면 된다. 그리고 Friend 클래스를 만들었으면 지우지 말자
문제 2에서 이 클래스를 대상으로 문제를 제시한다.
'''
class Friend:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone