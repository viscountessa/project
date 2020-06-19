class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        rez = self.quantity + other.quantity
        return f'Сумма клеток: {rez}'

    def __sub__(self, other):
        rez = self.quantity - other.quantity
        if rez <= 0:
            return f'Пытаетесь вычесть гиганта из карлика. Не получится'
        else:
            return f'Разность клеток: {rez}'


    def __mul__(self, other):
        rez = self.quantity * other.quantity
        return f'Произведение клеток: {rez}'

    def __truediv__(self, other):
        rez = round(self.quantity / other.quantity)
        return f'Результат деления клеток: {rez}'


    def make_order(self, cells):
        line = str()
        for i in range(int(self.quantity / cells)):
            line += f'{"*" * cells}\\n'
        line += f'{"*" * (self.quantity % cells)}'
        return line

    def make_order_2(self, cells):
        cel = self.quantity // cells
        ost = self.quantity % cells
        i = 0
        while i < cel:
            print("*" * cells)
            i = i + 1
        return "*" * ost

cell_1 = Cell(20)
cell_2 = Cell(15)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(6))
print(cell_2.make_order(4))
print('А сейчас фото клетки 1: ')
print(cell_1.make_order_2(6))
print('И фото клетки 2: ')
print(cell_2.make_order_2(4))
