import tools
import itertools
import math
import numpy as np

def get_ant_coords(ant_char: str, matrix, width: int, height: int):
    coords = []
    for y in range(height):
        for x in range(width):
            if matrix[y, x] == ant_char:
                coords.append((x, y))
    return coords

# 1151 bad too high

def get_cnt(x1, y1, d_dx, d_dy, sign_x, sign_y):
    cnt = 0
    rslt = 0
    while True:
        vx, vy = (int(round(x1 + d_dx * cnt * sign_x)), int(round(y1 + d_dy * cnt * sign_y)))
        valid = True if -1 < vx < width and -1 < vy < height else False
        if valid:
            if matrix2[vy, vx] == '.':
                matrix2[vy, vx] = '#'
            if not visited[vy, vx]:
                rslt += 1
                visited[vy, vx] = True
            cnt += 1
        else:
            break
    return rslt

def calculate_antinods(p1, p2, matrix, matrix2):
    x1, y1 = p1
    x2, y2 = p2
    
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    dx = ( x2 - x1 ) / d
    dy = ( y2 - y1 ) / d
    
    d_dx = abs( dx * d )
    d_dy = abs( dy * d )
    
    sign_x = 1 if x1 > x2 else -1
    sign_y = 1 if y1 > y2 else -1
    
    cnt1 = get_cnt(x1, y1, d_dx, d_dy, sign_x, sign_y)
    cnt2 = get_cnt(x2, y2, d_dx, d_dy, -sign_x, -sign_y)
    
    return cnt1, cnt2

if __name__ == "__main__":
    result = 0
    file_name = '8f'
    matrix = tools.get_matrix(file_name)
    matrix2 = matrix.copy()
    height, width = matrix.shape
    visited = np.full(matrix.shape, False)
    text = tools.get_string(file_name).replace('.', '').replace('\n', '')
    uniq_chars = list(set(text))
    
    for ant_char in uniq_chars:
        ant_coords = get_ant_coords(ant_char, matrix, width, height)
        coord_pairs = list(itertools.combinations(ant_coords, 2 ))
        for coord_pair in coord_pairs:
            p1, p2 = coord_pair
            cnt1, cnt2 = calculate_antinods(p1, p2, matrix, matrix2)
            result += cnt1
            result += cnt2
    
    for row in matrix2:
        print(''.join(row))
    
    print(result)
