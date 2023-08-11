# 1
# 1부터 5사이에 존재하는 모든 정수를 역순으로 출력하는 프로그램 구현

for number in range(5, 0):
    print(number)

# 1번 풀이

# range()함수 - 세 개의 인자(범위 시작점, 범위 끝점, 간격) 범위의 끝점은 포함되지 않음
for i in range(5, 0, -1):
    print(i)
# 2
# 사용자로부터 임의의 양의 정수를 하나 입력받은 뒤
# 그 숫자만큼 '과일 이름'을 입력받아 basket 리스트에 저장하는 프로그램 구현

number = int(input('양의 정수 하나를 입력해주세요: '))



# 2번 풀이

# 사용자로부터 임의의 양의 정수 입력받기
num_of_fruits = int(input('입력할 과일의 개수를 입력하세요: '))

#basket 빈 리스트를 생성
basket = []

# 입력받은 숫자만큼 반복하면서 과일 이름을 입력받고 리스트에 추가
for i in range(num_of_fruits):
    fruit = input('과일 이름을 입력하세요: ')
    basket.append(fruit)

print('과일 바구니 : ', basket)

