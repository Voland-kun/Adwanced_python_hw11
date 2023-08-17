class Matrix:
    """"Класс матрицы"""
    def __init__(self, list_of_lists):
        """Создаёт объект класса Matrix принимая список списков, содержащих числа."""
        self.matrix = []
        length = len(list_of_lists[0])
        count = 0
        for i in list_of_lists:
            if len(i) == length:
                self.matrix.append(i.copy())
            else:
                raise Exception('Разная длина строк матрицы')
            count += 1
        self.rows = count
        self.columns = length

    def __str__(self):
        """Печать матрицы"""
        format_size = []
        for col in zip(*self.matrix):
            col_len = [len(str(x)) for x in col]
            format_size.append(max(col_len))
        res = ''
        for i in self.matrix:
            for n, e in enumerate(i):
                res += f'{e:>{format_size[n]}}  '
            res += '\n'
        return res

    def __eq__(self, other):
        """Сравнение матриц."""
        # if str(self) == str(other):
        #     return True # на первый взгляд тоже работает
        if self.rows == other.rows and self.columns == other.columns:
            for i in range(self.columns):
                for j in range(self.rows):
                    if self.matrix[j][i] != other.matrix[j][i]:
                        return False
            return True
        else:
            return False

    def __add__(self, other):
        """Сложение матриц. Для матриц одной размерности"""
        if self.rows == other.rows and self.columns == other.columns:
            sum_res = [list(map(sum, zip(*i))) for i in zip(self.matrix, other.matrix)]
        else:
            raise Exception('Разная размерность матриц')
        return Matrix(sum_res)

    def __mul__(self, other):
        """Умножение матриц. Для совместимых матриц."""
        if self.rows == other.columns and self.columns == other.rows:
            mul_res = [[sum(a * b for a, b in zip(ra, cb)) for cb in zip(*other.matrix)] for ra in self.matrix]
            return Matrix(mul_res)
        else:
            raise Exception('Матрицы не совместимы')


a = [1, 2]
b = [4, 5]
e = [6, 7]
f = [85684, 9, 10]
c = [9, 8, 7]
d = [6, 5, 4]
r1 = [a, b, e]
r2 = [c, d]
r3 = [a, b]
r4 = [b, e]
r5 = [c, f, d]

m1 = Matrix(r1)
m2 = Matrix(r2)
m3 = Matrix(r3)
m4 = Matrix(r4)
m5 = Matrix(r5)
m6 = Matrix([[1, 2],[4, 5]])

print(m5)
print(m1 * m2)
print(m3 + m4)
print(m1 == m2)
print(m3 == m6)

# help(Matrix)
