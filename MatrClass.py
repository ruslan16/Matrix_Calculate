import copy
class Matrix:
    def __init__(self):
        self.line, self.column = map(int, input("Enter size of matrix: > ").split(' '))

    def ft_addmatr(self):
        Matr = []
        Matr_res = []
        print('Enter matrix:')
        for i in range(self.line):
            Matr.append(input().split(' '))
        for i in range(self.line):
            Matr_res.append([])
            for j in range(self.column):
                if '.' in Matr[i][j]:
                    Matr_res[i].append(float(Matr[i][j]))
                else:
                    Matr_res[i].append(int(Matr[i][j]))
            if len(Matr[i]) != self.column:
                raise Exception("Неверный размер")
        return Matr_res

    def sum_matr(self, Matr_a, Matr_b):
        result = []
        for i in range(len(Matr_a)):
            result.append([])
            for j in range(len(Matr_a[0])):
                result[i].append(Matr_a[i][j] + Matr_b[i][j])
        return result

    def multipl_const(self, Matr, number):
        result = []
        for i in Matr:
            if type(number) is float:
                result.append(list(map(lambda x: float(x) * number, i)))
            else:
                result.append(list(map(lambda x: int(x) * number, i)))
        return result

    def multipl_matr(slef, Matr_a, Matr_b, line_a, column_a, column_b):
        result = []
        res = 0
        for i in range(line_a):
            result.append([])
            for j in range(column_b):
                for k in range(column_a):
                    res += Matr_a[i][k] * Matr_b[k][j]
                result[i].append(res)
                res = 0
        return result

    def trans_matr(slef, Matr, line, column, command):
        result = []
        if command == '1':
            for i in range(column):
                result.append([])
                for j in range(line):
                    result[i].append(Matr[j][i])
        elif command == '2':
            tmp_line = line
            i = -1
            while column:
                result.append([])
                i += 0
                while tmp_line:
                    result[i].append(Matr[tmp_line - 1][column - 1])
                    tmp_line -= 1
                tmp_line = line
                column -= 1
        elif command == '3':
            tmp_column = column
            for i in range(line):
                result.append([])
                while tmp_column:
                    result[i].append(Matr[i][tmp_column - 1])
                    tmp_column -= 1
                tmp_column = column
        elif command == '4':
            i = -1
            while line:
                result.append([])
                i += 1
                for j in range(column):
                    result[i].append(Matr[line - 1][j])
                line -= 1
        return result
    def opredelitel(self, Matr, line, column):
        if line != column:
            raise Exception("Кол-во строк не соответствует кол-ву столбцов")
        res = 0
        if line == 1:
            return Matr[0][0]
        if line == 2:
            return (Matr[0][0] * Matr[1][1]) - (Matr[0][1] * Matr[1][0])
        string = Matr[0]
        for i in range(column):
            Matr_res = copy.deepcopy(Matr[1:])
            for k in range(line - 1):
                Matr_res[k].pop(i)
            if i % 2 != 0:
                res += -string[i] * self.opredelitel(Matr_res, line - 1, column - 1)
            else:
                res += string[i] * self.opredelitel(Matr_res, line - 1, column - 1)
        return res
    def minor(self, Matr, line, column):
        matr_res = []
        for i in range(line):
            matr_temp = copy.deepcopy(Matr)
            matr_res.append([])
            matr_temp.pop(i)
            for j in range(column):
                matr_temp_two = copy.deepcopy(matr_temp)
                for k in range(line - 1):
                    matr_temp_two[k].pop(j)
                res = self.opredelitel(matr_temp_two, line - 1, column - 1)
                matr_res[i].append(res)
        return matr_res
    def inverse_matr(self, Matr, line, column):
        opr = self.opredelitel(Matr, line, column)
        if opr == 0:
            print('Определитель равен 0')
            return 0
        Matr = self.minor(Matr, line, column)
        for i in range(line):
            for j in range(line):
                if ((i % 2 == 0) & (j % 2 != 0)) or ((i % 2 != 0) & (j % 2 == 0)):
                    Matr[i][j] = Matr[i][j] * -1
        number = 1 / opr
        Matr = self.trans_matr(Matr, line, column, "1")
        result = self.multipl_const(Matr, number)
        res = []
        for i in range(line):
            res.append(list(map(lambda x: round(x, 2), result[i])))
        return res
