import tools
import itertools
import math

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] # R, L, U, D


def start_score_search(matrix, start):
    stack = [start]
    height, width = matrix.shape
    count = 0
    visited = set()

    while stack:
        y, x = stack.pop()
        
        # Ak sme dosiahli cieľ
        if matrix[y, x] == 9:
            count += 1
            continue
        
        # Znač aktuálny bod ako navštívený
        visited.add((y, x))
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < height and 0 <= nx < width \
                and matrix[ny, nx] != -1 \
                and matrix[ny, nx] == matrix[y, x] + 1 \
                and (ny, nx) not in visited:
                stack.append((ny, nx))
        
        # Po spracovaní odznač aktuálny bod
        visited.remove((y, x))

    return count

if __name__ == "__main__":
    result = 0
    file_name = '10'
    matrix = tools.get_int_matrix(file_name)
    height, width = matrix.shape
    
    for y in range(height):
        for x in range(width):
            if matrix[y, x] == 0:
                count = start_score_search(matrix, (y, x))
                result += count
    
    print(result)
