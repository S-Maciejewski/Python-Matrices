from random import randrange as rand


def print_matrix(matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])


def make_empty_matrix(rows, columns):
    matrix = []
    for i in range(0, rows):
        row = []
        for j in range(0, columns):
            row.append(0)
        matrix.append(tuple(row))
    return tuple(matrix)  # Tuple ma szybszy odczyt na przyszłość


def make_identity_matrix(size):
    matrix = []
    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append(1) if i == j else row.append(0)
        matrix.append(tuple(row))
    return tuple(matrix)    # Tuple ma szybszy odczyt na przyszłość


def make_random(rows, columns):
    matrix = []
    for i in range(0, rows):
        row = []
        for j in range(0, columns):
            row.append(rand(-1000, 1000))
        matrix.append(tuple(row))
    return tuple(matrix)    # Tuple ma szybszy odczyt na przyszłość


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


mat = make_random(2, 3)
# mat = make_identity_matrix(5)
# mat = make_empty_matrix(2,3)
print_matrix(mat)
print()
mat = transpose(mat)
print_matrix(mat)


