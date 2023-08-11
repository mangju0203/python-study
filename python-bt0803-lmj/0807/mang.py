'''
class Korean:
    country = '한국'

  

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
man = Korean('홀길동', 35, '서울')
print(man.name)
print(Korean.name)
'''

class Korean:
    country = '한국'
    
    @classmethod
    def trip(cls, country):
        if cls.country == country:
            print('국내여행입니다')
        else:
            print('해외여행입니다')
Korean.trip