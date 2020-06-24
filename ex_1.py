class Data:
    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = str(dd_mm_yyyy)

    @classmethod
    def extract(cls, dd_mm_yyyy):
        date = []
        for i in dd_mm_yyyy.split('-'):
            date.append(i)
        print(int(date[0]), int(date[1]), int(date[2]))

    @staticmethod
    def valid(dd, mm, yyyy):
        if 0 < dd <= 31:
            if 0 < mm <= 12:
                if 1990 <= yyyy <= 2020:
                    return f'Введена корректная дата'
                else:
                    return f'Проверьте правильность введенной даты!'
            else:
                return f'Проверьте правильность введенной даты!'
        else:
            return f'Проверьте правильность введенной даты!'

    #def my_method (self, dd, mm, yyyy):
        #return Data.valid()


Data.extract('12-12-1995')
print(Data.valid(12, 12, 1995))
