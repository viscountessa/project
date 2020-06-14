class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def massa(self):
        asf = 25
        s = 5
        mas = self._length * self._width * asf * s / 1000
        print(f'Масса покрытия для дорожного полотна: {mas} т')

mas_1 = Road(20, 5000)
mas_1.massa()
