class character:
    def __init__(self, name, hp, strength):
        self.name = name
        self. hp = hp
        self.strength = strength
        print(f'캐릭터 {self.name}가 생성되었습니다. 체력은 {self.hp}, 힘은 {self.strength}' )
              
    def attack(self, other_character):
            print(f'{self.name}가 {other_character}을 공격합니다')
            other_character.hp -= self.strength

    def __del__(self):
            print(f'{self.name}가 게임에서 사라졌숩니다')

    def remove_from_game(self):
          

if Naymar.hp <= 0:
      NAymar.remove_from_game()
      del Naymar

Naymar = character('Naymar', 300, 50)
Son = character('son', 400, 150)

Son.attact(Naymar)
print(f'네이마르의 남은 체력은{Naymar.hp}입니다')




#? 파이썬 소멸자 사용 시 주의사항
# : 소멸자(__del__메서드) 는 객체가 메모리에서 제거될 때 사용
# : 소멸자의 삭제 시점을 프로그래머가 명확하게 지정할 수 없음
# : 파이썬의 가비지 컬렉션이 언제 동작할지 불분명