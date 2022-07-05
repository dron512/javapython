def main():
    num = int(input('input number'))
    if num %2 == 0 and num%3 == 0:
        print('2의 배수 이면서 3의 배수 입니다.')
    else:
        print(num ,'은 num 입니다.')
main()