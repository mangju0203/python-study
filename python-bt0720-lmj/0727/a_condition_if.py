#1
num1 = print(int(input('정수를 입력해 주세요:')))
num2 = print(int(input('정수를 입력해 주세요:')))
num3 = print(int(input('정수를 입력해 주세요:')))
if num1 > num2 and num1 > num3:
    print('세 정수 중 가장 큰 수는 %d 입니다' %num1)
if num2 > num3 and num2 > num1:
    print('세 정수 중 가장 큰 수는 %d 입니다' %num2)
else:
    print('세 정수 중 가장 큰 수는 %d 입니다.' %num3)

# 1번 풀이
# 사용자로부터 3개의 정수를 입력받기
num1 = int(input('첫 번째 숫자를 입력하세요: '))
num2 = int(input('두 번째 숫자를 입력하세요: '))
num3 = int(input('세 번째 숫자를 입력하세요: '))
# 관계 연산자 & 논리 연산자를 이용하여 가장 큰 수를 확인하고 출력
if (num1 >= num2) and (num1 >= num3): 
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print('가장 큰 수는', largest, '입니다')

# 2
num = print(int(input('차량번호를 입력해주세요:')))
if (num % 2 == 0):
    print('운행가능')
else:
    print('운행불가')

# 2번 풀이
# 사용자로부터 차량번호를 입력받기

car_number = input('차량 번호를 입력하세요(예: 237가 1234): ')

# 숫자와 문자열이 섞여있기 때문에 숫자와 문자열 구분해야함
# 입력받은 차량번호에서 마지막 숫자를 추출

last_digit = int(car_number[-1]) #'4' -> 4

# 마지막 숫자가 짝수인지 홀수인지 판별


if last_digit % 2 == 0:
    print('운행 가능')
else:
    print('운행 불가')





