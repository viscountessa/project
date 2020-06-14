class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position,  wage, bonus):
        super().__init__(name, surname, position,  wage, bonus)

    def get_full_name(self):
        print (f'Сотрудник: {self.name} {self.surname}')

    def get_total_income(self):
        total = self._income.get("wage") + self._income.get("bonus")
        print(f'Суммарный доход сотрудника на должности {self.position} составляет {total}')

worker_1 = Position('Виктория', 'Богданова', 'Data Scientist', 500000, 500000 )
worker_1.get_full_name()
worker_1.get_total_income()