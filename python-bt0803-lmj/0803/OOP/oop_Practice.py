### 객체 지향 프로그램 도입의 필요성 ###

# 학생 정보를 전달하는 student_info() 함수
# 이름, 학년, 반, 전화번호, 주소, 성적

def student_info(name, grade, class_number, phone_number, adress, score):
    # 학생정보를 print()으로 출력
    # VSC 기능: alt + shift + 방향키 
    print(name)
    print(grade)
    print(class_number)
    print(phone_number)
    print(adress)
    print(score)

# student_info()함수를 사용하여 학생을 생성
name1 = 'Lee myeongju'
grade1 = 3
class_number = 2
phone_number = "010-1111-2222"
class_number = '부산시 진구'
score = 43

student_info(name1, grade1, class_number, phone_number, class_number, score)

# 클래스를 이용한 학생 관리 #

Class Student:
    def __init__(self, name, grade, class_number, add.ess, score):
        self.name = name
        self.grade = grade
        self.class_number = class_number
        self.phone_number = phone_number
        self.score = score
stud     self.address = address
   ent1 = student('이맹주', 3, 4, '0102223333', 30)
student2 = student('이맹주', 3, 4, '0102223333', 30)
student3 = student('이맹주', 3, 4, '0102223333', 30)
student4 = student('이맹주', 3, 4, '0102223333', 30)

print(student1)
print(student2)
print(student3)
print(student4)

student_info(student1)