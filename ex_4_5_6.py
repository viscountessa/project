from random import randint


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Stock:
    stock_list = []

    def __init__(self, department, *args):
        self.department = {'department': department}

    def incoming(self):
        while True:
            try:
                a = int(input('Выберите позицию для внесения поступлений на склад: \n1 - принтер, 2 - сканер, 3 - копир, 0 для выхода \n'))
                if a > 3 or a < 0:
                    raise OwnError("Внимательнее с вводом! Повторите.")
            except ValueError:
                print('Внимательнее с вводом! Повторите еще раз.')
            except OwnError as err:
                print(err)
            else:
                return a


    def show(self):
        while True:
            try:
                x = int(input('Выберите действие: \n1 - посмотреть склад, 2 - посмотреть офис, 0 для выхода \n'))
                if x > 2 or x < 0:
                    raise OwnError("Внимательнее с вводом! Повторите.")
            except ValueError:
                print('Внимательнее с вводом! Повторите еще раз.')
            except OwnError as err:
                print(err)
            else:
                return x

    """Метод показывает оргтехнику на складе"""
    @staticmethod
    def show_stock():
        return (Stock.stock_list)

    """Метод перемещает оргтехнику со склада"""
    @staticmethod
    def move_stock():
        Stock.stock_list.remove(Technics._technics_list)
        return f'Оргтехника перемещена со склада'


class Technics:
    _technics_list = []
    _move_technics_list = []

    def __init__(self, company, model, price, quantity, inv_num, *args):
        self.company = company
        self.model = model
        self.price = price
        self.quantity = quantity
        self.inv_num = inv_num

    """Метод показывает внесенную оргтехнику"""
    @staticmethod
    def show_technics():
        return (Technics._technics_list)


    """Метод перемещает оргтехнику на склад"""
    @staticmethod
    def move_technics():
        Stock.stock_list.extend(Technics._move_technics_list)
        return f'Оргтехника перемещена на склад'

class Printer(Technics):

    def __init__(self, company, model, price, quantity, inv_num, type_print, color, *args):
        super().__init__(company, model, price, quantity, inv_num)
        self.type_print = type_print
        self.color = color
        self.list_printers = {'Марка': self.company, 'модель': self.model, 'тип принтера': self.type_print, 'цветность печати': self.color, 'цена': self.price, 'количество': self.quantity, 'инвентарный номер': self.inv_num}


    def incoming_printer(self):
        dict_printer = {'Марка': self.company, 'модель': self.model, 'тип принтера': self.type_print, 'цветность печати': self.color, 'цена': self.price, 'количество': self.quantity, 'инвентарный номер': self.inv_num}
        Technics._technics_list.append(dict_printer)
        return f'Введенные параметры: {dict_printer}'

    #тип принтера - струйный, лазерный
    #цветность печати - цветная, монохромная

class Scaner(Technics):
    def __init__(self, company, model, type_scan, resolution, price, quantity, inv_num):
        super().__init__(company, model, price, quantity, inv_num)
        self.type_scan = type_scan
        self.resolution = resolution
        self.list_scaners = {'Марка': self.company, 'модель': self.model, 'тип сканера': self.type_scan,
                              'макс разрешение': self.resolution, 'цена': self.price, 'количество': self.quantity,
                              'инвентарный номер': self.inv_num}

    def incoming_scaner(self):
        dict_scaner = {'Марка': self.company, 'модель': self.model, 'тип сканера': self.type_scan,
                              'макс разрешение': self.resolution, 'цена': self.price, 'количество': self.quantity,
                              'инвентарный номер': self.inv_num}
        Technics._technics_list.append(dict_scaner)
        return f'Введенные параметры: {dict_scaner}'

    #тип сканера - протяжный, планшетный
    #максимальное разрешение сканирования - 480х480dpi, 600х600dpi

class Copier(Technics):
    def __init__(self, company, model, format_original, format_print, price, quantity, inv_num):
        super().__init__(company, model, price, quantity, inv_num)
        self.format_original = format_original
        self.format_print = format_print
        self.list_copiers = {'Марка': self.company, 'модель': self.model, 'макс формат оригинала': self.format_original,
                             'макс формат печати': self.format_print, 'цена': self.price, 'количество': self.quantity,
                             'инвентарный номер': self.inv_num}

    def incoming_copier(self):
        dict_copier = {'Марка': self.company, 'модель': self.model, 'макс формат оригинала': self.format_original,
                             'макс формат печати': self.format_print, 'цена': self.price, 'количество': self.quantity,
                             'инвентарный номер': self.inv_num}
        Technics._technics_list.append(dict_copier)
        return f'Введенные параметры: {dict_copier}'

    #максимальный формат оригинала - А4, А3, А2
    #максимальный формат печати - А4, А3, А2
p_1 = Printer('Canon', 'CX60', 9876.5, 4, 9876543, 'струйный', 'монохромный')
p_2 = Printer('HP', 'C5283', 37890, 2, 7865942, 'лазерный', 'цветной')
s_1 = Scaner('Epson', 'F56', 'протяжный', '480 x 480', 14765.5, 5, 6783452)
s_2 = Scaner('HP', 'C3654', 'планшетный', '600 x 600', 42549, 2, 3452186)
c_1 = Copier('Canon', 'XTR1', 'A3', 'A4', 12400, 1, 1267345)
c_2 = Copier('HP', 'CF54', 'A3', 'A4', 12400, 1, 1267345)
p_1.incoming_printer()
p_2.incoming_printer()
s_1.incoming_scaner()
s_2.incoming_scaner()
c_1.incoming_copier()
c_2.incoming_copier()
Printer.move_technics()
z = 9
st = Stock('бух')
z = st.incoming()
try:
    while z != 0:
        if z == 1:
            print('Введите параметры для принтера: ')
            company = input('Введите марку: ')
            model = input('Введите модель: ')
            type_print = input('Введите тип принтера: ')
            color = input('Введите цветность печати принтера: ')
            price = float(input('Введите цену: '))
            quantity = int(input('Введите количество поступивших единиц: '))
            inv_num = randint(1000000, 10000000)
            printer_1 = Printer(company, model, type_print, color, price, quantity, inv_num)
            print(printer_1.incoming_printer())
            z = int(input('Выберите действие: \n 1 - внести еще принтер, 0 - выход \n'))
            if z == 0:
                z = 9
                z = st.incoming()
            elif z == 1:
                z = 1
        if z == 2:
            print('Введите параметры для сканера: ')
            company = input('Введите марку: ')
            model = input('Введите модель: ')
            type_scan = input('Введите тип сканера: ')
            resolution = input('Введите максимальное разрешение: ')
            price = float(input('Введите цену: '))
            quantity = int(input('Введите количество поступивших единиц: '))
            inv_num = randint(1000000, 10000000)
            scaner_1 = Scaner(company, model, type_scan, resolution, price, quantity, inv_num)
            print(scaner_1.incoming_scaner())
            z = int(input('Выберите действие: \n 1 - внести еще сканер, 0 - выход \n'))
            if z == 0:
                z = 9
                z = st.incoming()
            elif z == 1:
                z = 2
        if z == 3:
            print('Введите параметры для копира: ')
            company = input('Введите марку: ')
            model = input('Введите модель: ')
            format_original = input('Введите максимальный формат оригинала: ')
            format_print = input('Введите максимальный формат печати: ')
            price = float(input('Введите цену: '))
            quantity = int(input('Введите количество поступивших единиц: '))
            inv_num = randint(1000000, 10000000)
            copier_1 = Copier(company, model, format_original, format_print, price, quantity, inv_num)
            print(copier_1.incoming_copier())
            z = int(input('Выберите действие: \n 1 - внести еще копир, 0 - выход \n'))
            if z == 0:
                z = 9
                z = st.incoming()
            elif z == 1:
                z = 3
except ValueError:
    print('Внимательнее с вводом! Повторите.')
    z = 9
    z = st.incoming()
y = st.show()
while y != 0:
    if y == 1:
        print(Technics.show_technics())
        y = int(input('Выберите действие: \n 1 - посмотреть офис, 0 - выход \n'))
        if y == 0:
            z = 9
            z = st.incoming()
        elif y == 1:
            y = 2
    if y == 2:
        print(Stock.show_stock())
        y = int(input('Выберите действие: \n 1 - посмотреть склад, 0 - выход \n'))
        if y == 0:
            z = 9
            z = st.incoming()
        elif y == 1:
            y = 1
