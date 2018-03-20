from random import randrange as rand


def print_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print('{0: < 7}'.format(matrix[i][j]), end='')
        print()


def read_matrix():
    matrix = []
    print("Please, enter the following numbers:")
    try:
        rows = int(input("Rows: "))
        columns = int(input("Columns: "))
    except ValueError:
        print("Not a number")
    print("Enter matrix content one row at a time, values separated by comma ',', rows separated by enter")
    for i in range(0, rows):
        try:
            row_string = input("Row " + str(i + 1) + ": ")
            row_string.replace(" ", "")
            row = [float(x) for x in row_string.split(',')]
            matrix.append(row)
        except Exception:
            print("Error reading input")
    return tuple(matrix)


def make_empty_matrix(rows, columns):
    matrix = []
    for i in range(0, rows):
        row = []
        for j in range(0, columns):
            row.append(0)
        matrix.append(tuple(row))
    return tuple(matrix)


def make_identity_matrix(size):
    matrix = []
    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append(1) if i == j else row.append(0)
        matrix.append(tuple(row))
    return tuple(matrix)


def make_random_matrix(rows, columns, lower_bond=-1000, upper_bond=1000, fractions=False):
    matrix = []
    for i in range(0, rows):
        row = []
        for j in range(0, columns):
            if not fractions:
                row.append(rand(lower_bond, upper_bond))
            else:
                row.append(rand(lower_bond, upper_bond) + rand(0, 1000) / 1000)
        matrix.append(tuple(row))
    return tuple(matrix)


def transpose(matrix):
    new_matrix = []
    new_columns = len(matrix)
    new_rows = len(matrix[0])
    for i in range(0, new_rows):
        row = []
        for j in range(0, new_columns):
            row.append(matrix[j][i])
        new_matrix.append(tuple(row))
    return tuple(new_matrix)


def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices have different dimentions, addition is not possible")
        return None
    matrix = []
    for i in range(0, len(matrix1)):
        rows_tuple = (matrix1[i], matrix2[i])
        matrix.append([sum(rows) for rows in zip(*rows_tuple)])
    return tuple(matrix)


def subtract_matrices(minuend, substrahend):
    if len(minuend) != len(substrahend) or len(minuend[0]) != len(substrahend[0]):
        print("Matrices have different dimentions, subtraction is not possible")
        return ()
    matrix = []
    for i in range(0, len(minuend)):
        rows_tuple = (minuend[i], [-x for x in substrahend[i]])
        matrix.append([sum(rows) for rows in zip(*rows_tuple)])
    return tuple(matrix)


def scalar_multiplication(matrix, scalar):
    new_matrix = []
    for i in range(0, len(matrix)):
        row = [x * scalar for x in matrix[i]]
        new_matrix.append(row)
    return tuple(new_matrix)


def matrix_multiplication(left_matrix, right_matrix):
    if len(left_matrix[0]) != len(right_matrix):
        print("It is impossible to multiply those matrices in Couchy's way, as column amonunt "
              "of left matrix is not equal row amount of right matrix")
        return ()
    matrix = []
    for i in range(0, len(left_matrix)):
        row = []
        for j in range(0, len(right_matrix[0])):
            value = 0.0
            for k in range(0, len(left_matrix[0])):
                value += left_matrix[i][k] * right_matrix[k][j]
            row.append(value)
        matrix.append(row)
    return tuple(matrix)


def matrix_power(matrix, power):
    if len(matrix) != len(matrix[0]):
        print("Matrix is not square, therefore it cannot be risen to power")
        return ()
    new_matrix = matrix
    for i in range(1, power):
        new_matrix = matrix_multiplication(new_matrix, matrix)
    return tuple(new_matrix)


def compute_matrix_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]


def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        print("Matrix is not square, therefore no determinant exists")
        return 0
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    value = 0.0
    for i in range(0, len(matrix)):
        value += ((-1)**i) * matrix[0][i] * determinant(compute_matrix_minor(matrix, 0, i))
    return value


mat = make_random_matrix(5, 5, 0, 1, True)
print_matrix(mat)
print("Matrix determinant is ", determinant(mat))
