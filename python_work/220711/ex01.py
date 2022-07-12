from accumulator import Accumulator
a ='''

for i in range(1,10):
    Accumulator.add(i)

Accumulator.showResult()
'''
#print(a)
acc = Accumulator()
for i in range(1,10):
    acc.add(i)
acc.showResult()
