import numpy as np

mya = np.arange(16).reshape(-1,4)
print(mya)

np.save('mya.npy',mya)