class AA:
    number = 0
    def __init__(self,number):
        self.number = number
    def print(self):
        print('number = ',self.number)
        if(self.number>0):
            print('양수입니다')
        else:
            print('음수입니다.')
    def inputnumber(self):
        self.number = eval(input("숫자를 입력하세요"))
        
