def main():
    while True:
        try:
            print('나이를 입력하세요')
            age = int(input())
            print('입력하신 나이는 ',age)
            break
        except ValueError:
            print('나이를 숫자로 입력하세요')
    print('???')

main()
print("여기까지 오지 않는다.")