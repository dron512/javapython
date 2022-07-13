import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('data.xlsx')
print(data)
length = data['length'].to_numpy()
weight = data['weight'].to_numpy()
target = data['target'].to_numpy()

print(length[:5])
print(weight[:5])
print(target[:5])


'''
length = data.to_numpy('length',dtype=float)
weight = data.to_numpy('weight',dtype=float)
target = data.to_numpy('target',dtype=float)

print(length[:5])
print(weight[:5])
print(target[:5])
'''