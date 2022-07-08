from point import Point

class Circle:
    def __init__(self,x,y,r):
        print("일로 온다.",x,y,r)
        self.p = Point(x,y)
        self.r = r

    def showInfo(self):
        self.p.showInfo()
        print(f"반지름 = {self.r}")

c = Circle(2,2,4)
c.showInfo()