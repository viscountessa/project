class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки канцелярской принадлежностью. Чем порисуем?')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}! Отличный выбор! Чем порисуем теперь?')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}! Отличный выбор! Чем порисуем теперь?')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}! Отличный выбор! Новых принадлежностей больше нет =)')

s = Stationery('канц принадл')
s.draw()
p = Pen('ручка')
p.draw()
p_1 = Pencil('карандаш')
p_1.draw()
h = Handle('маркер')
h.draw()