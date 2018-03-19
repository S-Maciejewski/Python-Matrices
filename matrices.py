from random import randrange as rand


def print_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print('{0: <7}'.format(matrix[i][j]), end='')
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
            row_string = input("Row " + str(i+1) + ": ")
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


def make_random(rows, columns):
    matrix = []
    for i in range(0, rows):
        row = []
        for j in range(0, columns):
            row.append(rand(-1000, 1000))
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


mat = read_matrix()
print_matrix(mat)
print()
mat = transpose(mat)
print_matrix(mat)

