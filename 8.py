import tools
import itertools
import math

def get_ant_coords(ant_char: str, matrix, width: int, height: int):
    coords = []
    for y in range(height):
        for x in range(width):
            if matrix[y, x] == ant_char:
                coords.append((x, y))
    return coords

def calculate_antinods(p1, p2, matrix, matrix2):
    x1, y1 = p1
    x2, y2 = p2
    
    if p1 == (6, 5) or p2 == (6, 5) and p1 == (8, 8) or p2 == (8, 8):
        pass
    
    if x1 > x2:
        pass
    else:
        pass
    
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    dx = ( x2 - x1 ) / d
    dy = ( y2 - y1 ) / d
    
    d_dx = abs( dx * d )
    d_dy = abs( dy * d )
    
    sign_x = 1 if x1 > x2 else -1
    sign_y = 1 if y1 > y2 else -1
    
    ext1 = (int(x1 + d_dx * sign_x), int(y1 + d_dy * sign_y))
    ext2 = (int(x2 + d_dx * -sign_x), int(y2 + d_dy * -sign_y))
    
    
    vx, vy = ext1
    valid1 = True if -1 < vx < width and -1 < vy < height and matrix2[vy, vx] != '#' else False
    if valid1:
        matrix2[vy, vx] = '#'
    
    vx, vy = ext2
    valid2 = True if -1 < vx < width and -1 < vy < height  and matrix2[vy, vx] != '#' else False
    if valid2:
        matrix2[vy, vx] = '#'
    
    return valid1, valid2


if __name__ == "__main__":
    result = 0
    file_name = '8f'
    matrix = tools.get_matrix(file_name)
    matrix2 = matrix.copy()
    height, width = matrix.shape
    text = tools.get_string(file_name).replace('.', '').replace('\n', '')
    uniq_chars = list(set(text))
    
    for ant_char in uniq_chars:
        ant_coords = get_ant_coords(ant_char, matrix, width, height)
        coord_pairs = list(itertools.combinations(ant_coords, 2 ))
        for coord_pair in coord_pairs:
            p1, p2 = coord_pair
            valid1, valid2 = calculate_antinods(p1, p2, matrix, matrix2)
            if valid1:
                result += 1
            if valid2:
                result += 1
    
    for row in matrix2:
        print(''.join(row))
    
    print(result)
