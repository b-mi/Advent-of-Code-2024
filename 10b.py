import tools
import itertools
import math

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] # R, L, U, D


def start_score_search(matrix, start):
    stack = [(start, set([start]))]
    height, width = matrix.shape
    count = 0
    
    while stack:
        (y, x), visited = stack.pop()
        
        if matrix[y, x] == 9:
            count += 1
            continue
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if -1 < ny < height and -1 < nx < width \
                and matrix[ny, nx] != -1 \
                and matrix[ny, nx] == matrix[y, x] + 1 \
                and (ny, nx) not in visited:
                new_visited = visited | {(ny, nx)}
                stack.append(((ny, nx), new_visited))
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
