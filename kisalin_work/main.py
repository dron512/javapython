import pandas as pd
import matplotlib.pyplot as plt
import re

# kisa = pd.read_csv('kisa.csv',encoding="euc-kr")
# print(kisa.head())

pa ="'";

linnames = "['전기공사', '가스', '전자계산기', '신재생에너지발전설비(태양광)', '빅데이터분석']"

a = re.split(r"[']",linnames)
print(a)