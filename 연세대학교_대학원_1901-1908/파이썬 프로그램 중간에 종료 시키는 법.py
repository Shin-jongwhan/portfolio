import sys

#1st step
num = int(input('number: '))

if num >= 50:
    print('my number is >= 50')
elif num >= 30:
    print('my number is >= 30')
elif num < 30:
    print('my number is under 30')
    sys.exit(1)
# sys exit(1)을 쓰면 중간에 프로그램을 종료할 수 있다.

#2nd step
num2 = int(input("number2: "))
print("my number is ", num2)
