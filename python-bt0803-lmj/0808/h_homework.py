# class Car:
#     max_oil = 50

#     def __init__(self, oil):
#         self.oil = oil

#     def add_oil(self, oil):
#         if oil <= 0:
#             return
#         self.oil += oil
#         if self.oil > Car.max_oil:
#             self.oil = Car.max_oil
#     def car_info(self):
#         print('현재 주유상태: {}'.format(self.oil))

# class hybrid(Car):
#     max_charge = 30


#     def __init__(self, oil, charge):
#         super().__init__(oil)
#         self.charge = charge

#     def add_charge(self, charge):
        
#         if charge <= 0:
#             return
#         self.charge += charge
#         if self.charge > hybrid.max_charge:
#             self.charge = hybrid.max_oil
        
    

#     def hybrid_info(self):
#         super().oil_info()
#         print('현재 충전상태: {}'.format(self.charge))

# car = hybrid(0, 0)
# car.add_oil(100)
# car.charge(50)
# car.hybrid_info()


class Car:
    max_oil = 50

    def __init__(self, oil):
        self.oil = oil

    def add_oil(self, oil):
        if oil <= 0:
            return
        self.oil += oil
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil
    def car_info(self):
        print('현재 주유상태: {}'.format(self.oil))

class Hybrid(Car):
    max_battery = 30

    def __init__(self, oil, battery):
        super().__init__(oil) # 슈퍼 클래스의 생성자를 호출하여 oil속성을 초기화
        self.battery = battery

    def charge(self, battery):
        if battery <= 0:
            return # 0 이하로 출전하는 것을 방지
        self.battery = battery
        if self.battery > Hybrid.max_battery:
            self.battery = Hybrid.max_battery # 현재 배터리 충전량을 최대 충전량으로 설정

    def hybrid_info(self):
        self.car_info() # 슈퍼클래스의 car_info를 호출
        print('현재 충전 상태: {}'.format(self.battery))
        
car = Hybrid(0, 0)
car.add_oil(100)
car.charge(22)
car.hybrid_info()