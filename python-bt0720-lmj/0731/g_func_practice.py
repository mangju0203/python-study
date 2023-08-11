# 가변 인자(매개변수)를 받아 평균을 반환하는 함수를 작성
# len(), sum() 내장 함수 사용

def average(*numbers):
    return sum(numbers) / len(numbers)

print(average(1, 2, 3, 4, 5)) # 15 / 5 = 3.0