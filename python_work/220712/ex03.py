try:
    age = int(input('나이입력'))
    a = age/0
except Exception as e:
    print('모든 예외는 여기로 옵니다.', e)
# except ValueError:
#     print('한글적으면 어뜨케')
# except ZeroDivisionError:
#     print('0으로 나눌수 없는데')
# except IndexError

print('종료됩니다.')
