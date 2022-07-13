import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

x = [100, 200, 300, 400, 500]
y = [100, 200, 300, 400, 500]

bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0,
                33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0,
                700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3,
                11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7,
                10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

print(len(bream_length))
print(len(smelt_length))

plt.scatter(bream_length, bream_weight, c='#ff0000')
plt.scatter(x, y, c='#00ff00')
plt.scatter(smelt_length, smelt_weight, c="#0000ff")

plt.xlabel('length')
plt.ylabel('weight')
# plt.show()

length = bream_length + smelt_length + x
weight = bream_weight + smelt_weight + y

fish_data = [[l, w] for l, w in zip(length, weight)]
fish_target = ['A']*35+['B']*14+['C']*5

print(fish_data[0])
print(fish_target[0])

knclf = KNeighborsClassifier()
knclf.fit(fish_data,fish_target)

distan,index =knclf.kneighbors([[30,600]])
print("distan = ",distan)
print("index = ",index)


plt.scatter(30,600,marker='^')
plt.scatter(x,y,marker='*')
plt.scatter(fish_data[15][0],fish_data[15][1],c="#ffff00")
plt.scatter(fish_data[14][0],fish_data[14][1],c="#ffff00")
plt.scatter(fish_data[18][0],fish_data[18][1],c="#ffff00")
plt.scatter(fish_data[22][0],fish_data[22][1],c="#ffff00")
plt.scatter(fish_data[20][0],fish_data[20][1],c="#ffff00")
plt.scatter(600,600,marker='x')
plt.show()

prevalue = knclf.predict([[600,600]])
print('prevalue = ',prevalue)

prevalue = knclf.predict([[10,20]])
print(prevalue)

score = knclf.score(fish_data,fish_target)
print(score)

score = knclf.score([[300,500],[250,600],[400,600]],[1,1,0])
print(score)