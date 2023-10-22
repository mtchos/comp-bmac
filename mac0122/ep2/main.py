import copy


def main():
    input_text = ''
    while input_text != 'fim':
        input_text = str(input('Digite o nome do arquivo: '))
        filename = 'test-files/sudoku1.txt'
        matrix = open_sudoku(filename)

        if validate_sudoku(matrix):
            solutions = solve_sudoku(matrix, 0, 0)
            for index, solution in enumerate(solutions):
                if validate_sudoku(solution):
                    print('* * * Matriz Completa – Solução ' + str(index + 1))
                    print_matrix(solution)
        else:
            print("Sudoku inválido")
        

def open_sudoku(filename):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        return []

    matrix = [[0] * 9 for i in range(9)]

    for index, line in enumerate(file):
        characters = line.split()
        numbers = []

        for char in characters:
            try:
                number = int(char)
            except ValueError:
                return []

            numbers.append(number)

        matrix[index] = numbers

    print('* * * Matriz inicial * * *')
    print_matrix(matrix)
    return matrix


def validate_sudoku(matrix):
    if len(matrix) == 0:
        return False

    def get_column(column_index):
        return [matrix[line_index][column_index] for line_index in range(9)]

    for x, line in enumerate(matrix):
        block_x = x - x % 3
        for y, number in enumerate(line):
            block_y = y - y % 3

            if number == 0:
                break

            if 0 > number > 9:
                print('a')
                return False

            if line.count(number) > 1:
                print('b')
                return False

            if get_column(y).count(number) > 1:
                print('c')
                return False

            block_values = []
            for i in range(block_x, block_x + 3):
                for j in range(block_y, block_y + 3):
                    block_values.append(matrix[i][j])

            if block_values.count(number) > 1:
                print('d')
                return False

        if len(line) != 9:
            print('e')
            return False

    return True


def solve_sudoku(matrix, x, y):
    solutions = []
    ex, ey = x, y

    while matrix[ex][ey] != 0:
        ey += 1
        if ey == 9:
            ex += 1
            ey = 0
        if ex == 9:
            # Reached the end of the puzzle.
            solutions.append(copy.deepcopy(matrix))
            return solutions

    candidates = get_possible_values(matrix, ex, ey)

    for candidate in candidates:
        matrix[ex][ey] = candidate

        # Recursively solve the puzzle
        solutions += solve_sudoku(matrix, ex, ey)

        matrix[ex][ey] = 0  # Backtrack

    return solutions


def get_possible_values(matrix, x, y):
    possibilities = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    line = matrix[x]
    column = [matrix[i][y] for i in range(len(matrix))]
    start = x - x % 3
    end = y - y % 3

    existing_values = set(line + column)

    if matrix[x][y] != 0:
        return set()

    for position in existing_values:
        if position in possibilities:
            possibilities.remove(position)

    for i in range(start, start + 3):
        for j in range(end, end + 3):
            if matrix[i][j] in possibilities:
                possibilities.remove(matrix[i][j])

    return possibilities


def test_sudoku_solution(matrix):
    return validate_sudoku(matrix)


def print_matrix(matrix):
    for line in matrix:
        str_line = []
        for value in line:
            str_line += str(value)
        print('  '.join(str_line))
    print('\n')


main()
