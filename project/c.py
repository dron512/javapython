class A:
    name = 10
    email = 20
    pwd = 1234

    def __str__(self):
        return f"name = {self.name} email = {self.email} pwd = {self.pwd}"

dit = {}
dit['aa@naver.com'] = A();
dit['bb@naver.com'] = A();

aa = dit['aa@naver.com']
print(aa)
cc = dit['cc@naver.com']
print('cc = ',cc)