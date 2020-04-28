import MatrClass as f

while True:
    print('1. Add matrices\n2. Multiply matrix by a constant'
          '\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinate\n6. Inverse matrix\n0. Exit')
    command = input('Your choice: > ')
    if command == '1':
        obj_1 = f.Matrix()
        Matr_a = obj_1.ft_addmatr()
        obj_2 = f.Matrix()
        Matr_b = obj_2.ft_addmatr()
        if (obj_1.line != obj_2.line) or (obj_1.column != obj_2.column):
            print('The operation cannot be performed.')
        else:
            print('The result is:')
            result = obj_1.sum_matr(Matr_a, Matr_b)
        for row in result:
            print(*row)
        print()
    elif command == '2':
        obj = f.Matrix()
        Matr = obj.ft_addmatr()
        num = input('Enter constant: > ')
        if '.' in num:
            num = float(num)
        else:
            num = int(num)
        print('The result is:')
        result = obj.multipl_const(Matr, num)
        for row in result:
            print(*row)
        print()
    elif command == '3':
        obj_1 = f.Matrix()
        Matr_a = obj_1.ft_addmatr()
        obj_2 = f.Matrix()
        Matr_b = obj_2.ft_addmatr()
        if obj_1.column != obj_2.line:
            raise Exception("Кол-во столбцов первой матрицы не совпадает с кол-во строк второй")
        else:
            print('The result is:')
            result = obj_1.multipl_matr(Matr_a, Matr_b, obj_1.line, obj_1.column, obj_2.column)
        for row in result:
            print(*row)
        print()
    elif command == '4':
        print("1. Main diagonal\n2. Side diagonal\n3.Vertical line\n4.Horizontal line")
        command = input()
        obj = f.Matrix()
        Matr = obj.ft_addmatr()
        print('The result is:')
        result = f.Matrix.trans_matr(Matr, obj.line, obj.column, command)
        for row in result:
            print(*row)
        print()
    elif command == '5':
        obj = f.Matrix()
        Matr = obj.ft_addmatr()
        print('The result is:')
        result = obj.opredelitel(Matr, obj.line, obj.column)
        print(result, '\n')
    elif command == '6':
        obj = f.Matrix()
        Matr = obj.ft_addmatr()
        print('The result is:')
        result = obj.inverse_matr(Matr, obj.line, obj.column)
        if result:
            for row in result:
                print(*row)
    elif command == '0':
        exit()