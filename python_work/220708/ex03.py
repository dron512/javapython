import won as w1

import pandas as pd
import numpy as np

# 0< x <1
result = np.random.rand(10)
print(f"랜덤 값 나옵니다. {result}")

num = float(input("반지름 입력"))
result = w1.areawon(num)
print(f"넓이는 = {result}")
result = w1.cwon(num)
print(f"둘레는 = {result}")