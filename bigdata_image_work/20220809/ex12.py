a = [1,2,3,4,5]

print(max(a))
print(min(a))
print(sum(a))
print(sum(a)/len(a))
# print(mean(a))

print()
import numpy as np

npa = np.array(a)
print(np.max(npa))
print(np.min(npa))
print(np.sum(npa))
print(np.mean(npa))

npb = np.arange(16).reshape(-1,4)
sumb = np.sum(npb,axis=0)
meanb = np.mean(npb,axis=0)
print(npb)
print(sumb)
print(meanb)
print()
sumb = np.sum(npb,axis=1)
meanb = np.mean(npb,axis=1)
print(npb)
print(meanb)
print(sumb)





