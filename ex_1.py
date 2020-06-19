class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix_list]))


    def __add__(self, other):
        if len(self.matrix_list) != len(other.matrix_list):
            return f'Разная размерность матриц. Невозможно выполнить суммирование!'
        else:
            for i in range(len(self.matrix_list)):

                for j in range(len(other.matrix_list[i])):
                    rez[i][j] = self.matrix_list[i][j] + other.matrix_list[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in rez]))



matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#matrix_2 = Matrix([[11, 12, 13], [14, 15, 16]])
rez = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('***** Матрица А *****')
print(matrix_1)
print('***** Матрица В *****')
#print(matrix_2)
print('***** Сумма А + В *****')
try:
    print(matrix_1 + matrix_2)
except NameError:
    print(matrix_1)