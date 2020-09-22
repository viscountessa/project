class ComplexNum:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a}i'


num_1 = ComplexNum(2, 1)
num_2 = ComplexNum(3, 5)
print('*** Результат сложения ***')
print(num_1 + num_2)
print('*** Результат умножения ***')
print(num_1 * num_2)


