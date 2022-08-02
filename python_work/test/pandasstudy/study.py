import pandas as pd


word_dict = pd.Series({"apple":300,"banana":500,"melon":700})
frequency_dict = pd.Series({"apple":5,"banana":5,"melon":3})
importance_dict = pd.Series({"apple":1,"banana":2,"melon":3})

data = pd.DataFrame({"word":word_dict,"fre":frequency_dict,"import":importance_dict})
print(data)
score = data["fre"]*data["import"]
data["score"]=score
print(data)
print()
print(data.loc["apple":"banana","score":])
print(data.iloc[:2,1:])
print(data.loc["apple","import"])

print(data)
data.loc["Ele"]=['aa','bb','cc','44']
print(data)

data.to_csv('data.csv',encoding="utf-8-sig")
mydata = pd.read_csv('data.csv')
print(mydata)