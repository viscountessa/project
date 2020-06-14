from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый', 'Желтый']

    def running(self):
        i = 0
        while i >= 0:
            if i == 0:
                print(f'\033[31m Сигнал светофора: {TrafficLight_1.__color[i]}'.format())
                sleep(7)
            elif i == 1:
                print(f'\033[33m Сигнал светофора: {TrafficLight_1.__color[i]}'.format())
                sleep(2)
            elif i == 2:
                print(f'\033[36m Сигнал светофора: {TrafficLight_1.__color[i]}'.format())
                sleep(7)
            elif i == 3:
                print(f'\033[33m Сигнал светофора: {TrafficLight_1.__color[i]}'.format())
                sleep(2)
                i = (-1)
            i += 1


TrafficLight_1 = TrafficLight()
TrafficLight_1.running()



