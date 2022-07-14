from a import Friend

mylist = [Friend("이선준", "010-333-4444"), Friend("장지우", "010-555-5555"), Friend("윤지율","010-777-888")]
mylist.append(Friend("윤지민", "010-111-222"))

for f in mylist:
    if f.get_name() == '장지우':
        f.set_phone("010-999-999")
    # if f.get_name().startswith('윤') :
    #     print(f)
for f in mylist:
    print(f)


