# 영상처리 텍스트처리


a = "[aa,bb,cc]"

a = a.replace('[','')
a = a.replace(']','')

print(a)

a = a.split(',')
print(a)

for aele in a:
    print(aele)