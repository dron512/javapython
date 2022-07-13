class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def getAB(self):
        return self.a+self.b

    def __str__(self):
        return f"class A a ={self.a} b ={self.b}"

a = [A(10,20),A(20,30),A(30,40),A(40,50)]
for i in a:
    print(i.getAB())

print(a[0])

