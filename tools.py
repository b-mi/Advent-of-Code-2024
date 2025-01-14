import numpy as np
from colorama import Fore, Style, init



# from MatrixRenderer import MatrixRenderer
# from PyQt5Renderer import MatrixRenderer

def get_lines(file_name):
    with open(f'data\{file_name}.txt', "r") as file:
        lines = [line.strip() for line in file]
    return lines


def get_matrix(file_name, break_validator=None, empty_char='.'):
    lines = get_lines(file_name)
    rows = len(lines)
    cols = len(lines[0])
    matrix = np.full((rows, cols), empty_char, dtype=str)
    row = 0
    for line in lines:
        if break_validator:
            if break_validator(line):
                matrix = matrix[:row, :]
                break
        col = 0
        for col_char in line:
            matrix[row, col] = col_char
            col += 1
        row += 1
    return matrix

def get_int_matrix(file_name):
    lines = get_lines(file_name)
    rows = len(lines)
    cols = len(lines[0])
    matrix = np.full((rows, cols), -1, dtype=int)
    row = 0
    for line in lines:
        col = 0
        for col_char in line:
            matrix[row, col] = -1 if col_char == '.' else int(col_char)
            col += 1
        row += 1
    return matrix

def get_string(file_name):
    with open(f'data\{file_name}.txt', "r") as file:
        str = file.read()
    return str
    

def get_columns_as_ints(file_name):
    lines = get_lines(file_name)
    col_cnt = lines[0].split().__len__()
    arrs = [[] for _ in range(col_cnt)]
    for line in lines:
        parts = line.split()
        for col_idx in range(col_cnt):
            arrs[col_idx].append(int(parts[col_idx]))
    return arrs, arrs[0].__len__()


def get_rows_as_ints(file_name):
    lines = get_lines(file_name)
    arrs = []
    for line in lines:
        parts = line.split()
        arow = []
        for part in parts:
            arow.append(int(part))
        arrs.append(arow)
    return arrs

# def print_numpy_2d_array(matrix, colors):
#     for row in matrix:
#         print("".join(row))    

color_map = {
    'r': Fore.LIGHTRED_EX,
    'g': Fore.LIGHTGREEN_EX,
    'b': Fore.LIGHTBLUE_EX,
    'y': Fore.YELLOW,
}

    
def print_numpy_2d_array(matrix, title, colors):
    print()
    print('---')
    print(title)
    print('---')

    # Vytvoriť mapovanie farieb
    color_positions = {(row, col): color_map[color] for row, col, color in colors}

    # Tlač hlavičky s indexami stĺpcov
    num_cols = len(matrix[0])
    col_indices = "  " + "".join(str(i % 10) for i in range(num_cols))
    print(col_indices)

    for row_index, row in enumerate(matrix):
        # Vytvoriť riadok s indexom riadku zľava
        row_str = str(row_index % 10) + " "  # Index riadku modulo 10
        colored_row = []
        for col_index, char in enumerate(row):
            if (row_index, col_index) in color_positions:
                colored_row.append(color_positions[(row_index, col_index)] + char + Style.RESET_ALL)
            else:
                colored_row.append(char)
        print(row_str + "".join(colored_row))