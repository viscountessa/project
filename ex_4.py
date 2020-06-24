from random import randint
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
class Stock:

    def __init__(self, department, *args):
        self.department = {'department': department}
        self.stock_list = []

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

    def transfer(self):
        pass



#class Worker(Stock):
    #def __init__(self, name, surname, position):
        #self.name = name
        #self.surname = surname
        #self.position = position

class Technics:
    def __init__(self, company, model, price, quantity, inv_num, *args):
        self.company = company
        self.model = model
        self.price = price
        self.quantity = quantity
        self.inv_num = inv_num
        self.technics_list_pr = []
        self.technics_list_sc = []
        self.technics_list_co = []



class Printer(Technics):

    def __init__(self, company, model, price, quantity, inv_num, type_print, color, *args):
        super().__init__(company, model, price, quantity, inv_num)
        self.type_print = type_print
        self.color = color
        self.list_printers = {'Марка': self.company, 'модель': self.model, 'тип принтера': self.type_print, 'цветность печати': self.color, 'цена': self.price, 'количество': self.quantity, 'инвентарный номер': self.inv_num}
        self.printers_list = []

    def incoming_printer(self):
        dict_printer = {'Марка': company, 'модель': model, 'тип принтера': type_print, 'цветность печати': color, 'цена': price, 'количество': quantity, 'инвентарный номер': inv_num}
        self.list_printers.update(dict_printer)
        self.technics_list_pr.append(self.list_printers)
        return f'Введенные параметры: {dict_printer}, {self.technics_list_pr}'

    #тип принтера - струйный, лазерный
    #цветность печати - цветная, монохромная

class Scaner(Technics):
    def __init__(self, company, model, price, quantity, inv_num, type_scan, resolution):
        super().__init__(company, model, price, quantity, inv_num)
        self.type_scan = type_scan
        self.resolution = resolution
        self.list_scaners = {'Марка': self.company, 'модель': self.model, 'тип сканера': self.type_scan,
                              'макс разрешение': self.resolution, 'цена': self.price, 'количество': self.quantity,
                              'инвентарный номер': self.inv_num}
        self.scaners_list = []

    def incoming_scaner(self):
        dict_scaner = {'Марка': self.company, 'модель': self.model, 'тип сканера': self.type_scan,
                              'макс разрешение': self.resolution, 'цена': self.price, 'количество': self.quantity,
                              'инвентарный номер': self.inv_num}
        self.list_scaners.update(dict_scaner)
        self.technics_list_sc.append(self.list_scaners)
        return f'Введенные параметры: {dict_scaner}, {self.technics_list_sc}'
    #тип сканера - протяжный, планшетный
    #максимальное разрешение сканирования - 480х480dpi, 600х600dpi

class Copier(Technics):
    def __init__(self, company, model, price, quantity, inv_num, format_original, format_print):
        super().__init__(company, model, price, quantity, inv_num)
        self.format_original = format_original
        self.format_print = format_print
        self.list_copiers = {'Марка': self.company, 'модель': self.model, 'макс формат оригинала': self.format_original,
                             'макс формат печати': self.format_print, 'цена': self.price, 'количество': self.quantity,
                             'инвентарный номер': self.inv_num}
        self.copiers_list = []

    def incoming_copier(self):
        dict_copier = {'Марка': self.company, 'модель': self.model, 'макс формат оригинала': self.format_original,
                             'макс формат печати': self.format_print, 'цена': self.price, 'количество': self.quantity,
                             'инвентарный номер': self.inv_num}
        self.list_copiers.update(dict_copier)
        self.technics_list_co.append(self.list_copiers)
        return f'Введенные параметры: {dict_copier}, {self.technics_list_co}'
    #максимальный формат оригинала - А4, А3, А2
    #максимальный формат печати - А4, А3, А2

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
        if z == 0:
            z = st.incoming()
except ValueError:
    print('Внимательнее с вводом! Повторите.')
    z = 9
    z = st.incoming()
