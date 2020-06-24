class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
while True:
    try:
        inp_num_1 = input("Введите число или Q для выхода: ")
        if inp_num_1 == 'Q':
            print(my_list)
            print('Выход')
            break
        if inp_num_1.isdigit():
            my_list.append(inp_num_1)
        if not(inp_num_1.isdigit()):
            raise OwnError("Вы вводите не число!")
    except ValueError:
        print("Будьте внимательны! Необходимо вводить число!")
    except OwnError as err:
        print(err)
    else:
        print(f'Текущий список - {my_list}')