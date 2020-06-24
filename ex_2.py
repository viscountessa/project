class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_num_1 = input("Введите делимое число: ")
inp_num_2 = input("Введите число-делитель: ")

try:
    inp_num_1 = int(inp_num_1)
    inp_num_2 = int(inp_num_2)
    rez = inp_num_1 / inp_num_2
    if rez < 0:
        raise OwnError("Полученный результат меньше нуля")
except ValueError:
    print("Будьте внимательны! Необходимо вводить число!")
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
except OwnError as err:
    print(err)
else:
    print(f"Результат вычисления: {rez}")
finally:
    print(f"Спасибо что воспользовались калькулятором!")