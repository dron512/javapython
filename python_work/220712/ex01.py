class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def getAB(self):
        return self.a+self.b

for i in [A(10,20),A(20,30),A(30,40),A(40,50)]:
    print(i.getAB())