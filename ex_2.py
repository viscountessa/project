from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def total(self):
        pass


class Coat(Clothes):
    def __init__(self, name, V):
        self.V = V
        self.name = name

    def total(self):
        pass

    @property
    def material_coat(self):
        total_coat = round(self.V/6.5 + 0.5)
        return total_coat

class Suit(Clothes):
    def __init__(self, name, H):
        self.H = H
        self.name = name

    def total(self):
        pass

    @property
    def material_suit(self):
        total_suit = round(2*self.H + 0.3)
        return total_suit

suit_1 = Suit('ZARA_suit', 170)
print(f'На пошив пальто модели {suit_1.name} необходимо {suit_1.material_suit} метров ткани')
coat_1 = Coat('Mango_coat', 44)
print(f'На пошив пальто модели {coat_1.name} необходимо {coat_1.material_coat} метров ткани')
total_material = suit_1.material_suit + coat_1.material_coat
print(f'Всего для пошива изделий необходимо {total_material} метров ткани')