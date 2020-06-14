import random
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина поехала!')

    def stop(self):
        print(f'Машина остановилась!')

    def turn(self):
        direction = random.choice(['налево', 'направо', 'прямо'])
        if direction == 'налево':
            print('Дали лево руля!')
        elif direction == 'направо':
            print('Дали право руля!')
        elif direction == 'прямо':
            print('Едем прямо!')

    def show_speed(self):
        speed = random.randint(1, 100)
        print(f'Текущая скорость {speed} км/ч')
        if self.is_police == True and speed > 60:
            print('Копам можно все!')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        speed = random.randint(1, 100)
        print(f'Текущая скорость {speed} км/ч')
        if speed > 60:
            print(f'!!!Полегче!!! Ты превышаешь! Твоя скорость {speed} км/ч')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        speed = random.randint(1, 100)
        print(f'Текущая скорость {speed} км/ч')
        if speed > 40:
            print(f'!!!Полегче!!! Ты превышаешь! Твоя скорость {speed} км/ч')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

car_1 = Car(0, 'зеленый', 'УАЗ', True)
car_1.go()
car_1.turn()
car_1.show_speed()
car_1.turn()
car_1.stop()

car_2 = TownCar(0, 'желтый', 'Ford', False)
car_2.go()
car_2.turn()
car_2.show_speed()
car_2.stop()

car_3 = SportCar(0, 'красный', 'Ferrari', False)
car_3.go()
car_3.turn()
car_3.show_speed()
car_3.stop()

car_4 = WorkCar(0, 'синий', 'Lexus', False)
car_4.go()
car_4.turn()
car_4.show_speed()
car_4.stop()

car_5 = PoliceCar(0, 'серебряный', 'Ford', True)
car_5.go()
car_5.turn()
car_5.show_speed()
car_5.stop()