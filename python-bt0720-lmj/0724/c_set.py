### Set 자료형 ###

# 순서 X, 요소 변경 O, 중복된 값 X
# 순서가 없기 때문에 인덱싱(Indexing), 슬라이싱(Slicing) 등의 연산을 지원하지 않습니다

# set 자료형 생성
# 1-1. 중괄호{} 를 사용하여 생성하고 각 요소는 쉼표(,)로 구분
# 1-2. set()함수를 사용하여 생성

set1 = {1, 2, 3} # 중괄호를 사용한 세트 생성
set2 = set() # 빈 세트 생성
set3 = set([1, 2, 3]) #리스트를 이용한 세트 생성 가능
set4 = set('Hello') # 문자열을 이용한 세트 생성, 출력: {'e', 'H', 'l', 'o'}

# 2. set 메서드
# 2-1. 세트에 항목을 추가: add()
s = {1, 2, 3}
s.add(4)
s.add(2)
print(s) # 출력: {1, 2, 3, 4}

# 2-2. 주어진 값이 있는 항목을 제거: remove()
s.remove(2)
print(s) # {1, 3, 4}
# s.remove(5) # 주어진 값이 없는 경우 오류 발생

# 2-3. 주어진 값이 있는 항목을 제거: discard()
s.discard(5) # 제거하려는 항목이 없어도 에러 발생 X

 