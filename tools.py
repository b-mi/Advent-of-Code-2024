import numpy as np

# from MatrixRenderer import MatrixRenderer
from PyQt5Renderer import MatrixRenderer

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

def get_renderer(matrix, colors, cell_size=20, caption=None, window_size=None, font_size=20):
    r = MatrixRenderer(matrix, cell_size=cell_size, colors=colors, window_size=window_size, font_size=font_size)
    renderer_update(r, matrix, caption=caption)
    return r

def renderer_update(renderer, matrix, caption=None, wait_for_keypress=None):
    renderer.update_matrix(matrix)
    if caption:
        renderer.set_caption(caption)
    renderer.render()

def renderer_do_events(renderer):
    renderer.do_events()
        
    
def render_matrix(matrix, colors, caption=None, cell_size=20, window_size=None, font_size=10):
    renderer = get_renderer(matrix, colors, cell_size=cell_size, caption=caption, font_size=font_size, window_size=window_size)
