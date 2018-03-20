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


def make_zeros_matrix(rows, columns):
    matrix = []
    for i in range(0, rows):
        row = []
        for j in range(0, columns):
            row.append(0)
        matrix.append(tuple(row))
    return tuple(matrix)


def make_ones_matrix(rows, columns):
    matrix = []
    for i in range(0, rows):
        row = []
        for j in range(0, columns):
            row.append(1)
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
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def rank(matrix):
    matrix = [list(row) for row in matrix]
    column_count = len(matrix[0])
    row_count = len(matrix)
    rank = min(column_count, row_count)

    if row_count > column_count:
        new_matrix = []
        for i in range(0, column_count):
            new_row = []
            for j in range(0, row_count):
                new_row.append(matrix[j][i])
            new_matrix.append(new_row)
        matrix = new_matrix
        column_count, row_count = row_count, column_count

    for i in range(0, rank):
        if matrix[i][i] != 0:
            for j in range(i + 1, row_count):
                for k in range(0, len(matrix[j])):
                    matrix[j][k] += matrix[i][k] * (-(matrix[j][i] // matrix[i][i]))
        else:
            zero = True
            for k in range(i + 1, row_count):
                if matrix[k][i] != 0:
                    matrix[k], matrix[i] = matrix[i], matrix[k]
                    zero = False
                    break
            if zero:
                for k in range(row_count):
                    matrix[k][i], matrix[k][rank - 1] = matrix[k][rank - 1], matrix[k][i]
            row_count -= 1
        counted = 0
        for j in matrix:
            if j == [0] * column_count:
                counted += 1

        return rank - counted


def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        print("Matrix is not square, therefore no determinant exists")
        return 0
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    value = 0.0
    for i in range(0, len(matrix)):
        value += ((-1) ** i) * matrix[0][i] * determinant(compute_matrix_minor(matrix, 0, i))
    return value


def inverse_matrix(matrix):
    det = determinant(matrix)
    if det == 0:
        print("Determinant equals 0, therefore no inverse matrix exists")
        return ()
    if len(matrix) == 2:
        return ((matrix[1][1] / det, -1 * matrix[0][1] / det),
                (-1 * matrix[1][0] / det, matrix[0][0] / det))
    cofactor_matrix = []
    for i in range(len(matrix)):
        row_cofactor = []
        for j in range(len(matrix)):
            minor = compute_matrix_minor(matrix, i, j)
            row_cofactor.append(((-1) ** (i + j)) * determinant(minor))
        cofactor_matrix.append(row_cofactor)
    cofactor_matrix = list(transpose(cofactor_matrix))
    cofactor_matrix = [list(row) for row in cofactor_matrix]
    for i in range(len(cofactor_matrix)):
        for j in range(len(cofactor_matrix)):
            cofactor_matrix[i][j] = cofactor_matrix[i][j] / det
    return tuple(cofactor_matrix)


# Use example
mat = make_random_matrix(3, 3, -10, 10)
print_matrix(mat)
print("Matrix determinant is ", determinant(mat), ", rank is", rank(mat), " and inverse matrix is")
print_matrix(inverse_matrix(mat))
