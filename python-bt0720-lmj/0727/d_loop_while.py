# while문: 사용자로부터 숫자를 계속 입력받다가
# 사용자가 0을 입력하면 프로그램이 종료되는 파이썬 프로그램을 작성
while True:
   num = int(input('숫자를 입력해주세요: '))
    if num == 0:
        break


# 무한 로프 생성
while True:
    number = int(input('숫자를 입력하세요(0을 입력하면 종료됩니다)'))
    if number == 0:
        break