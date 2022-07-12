from person import Person

p1 = Person()
p2 = Person()
p3 = Person()

p1.age = 39
p1.up_age()
print(p1.get_age())

p2.age = 59
p2.up_age()
print(p2.get_age())

n = 100
print( type(n) )
print(n.bit_length())

a = [1,2,3,4]
print(type(a))
a.remove(1)
print(a)