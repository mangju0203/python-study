# add 함수: 두 수를 더하는 함수
def add(a, b):
    return a + b
# subtract 함수: 두 수를 빼는 함수
def subtract(a, b):
    return a - b
# multiply 함수: 두 수를 곱하는 함수
def multiply(a, b):
    return a * b
# divide 함수: 두 수를 나누는 함수
# 조건문을 사용하여 b가 0일 경우 ' Error: Cannot division by zero!" 반환
# 0이 아닐 경우에는 a / b
def divide(a, b):
    if b == 0:
        return 'Error: Cannot division by zero!'
    else:
        return a / b
# 4개의 함수 호출
print(add(10,5))
print(subtract(10,5))
print(multiply(10,5))
# print(divide(10,0)) # Error : ZeroDivisionError: division by zero
print(divide(10,2))