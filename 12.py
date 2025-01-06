import tools
import numpy as np

def get_area_and_perimeter(matrix, visited, start_y, start_x):
    
    if start_y == 1 and start_x == 0:
        pass
    height, width = matrix.shape
    material = matrix[start_y, start_x]
    stack = []
    stack.append((start_y, start_x))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    area, perimeter = 0, 0
    visited[start_y, start_x] = True
    while stack:
        y, x = stack.pop()
        area += 1
        # print(f'*{material}: y: {y}, x: {x}')

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            if ny == 2 and nx == 0:
                pass
            
            is_valid_loc = -1 < ny < height and -1 < nx < width
            if is_valid_loc: # validna pozicia
                if matrix[ny, nx] == material:
                    if not visited[ny, nx]: # nepridavame to, co uz bolo visited
                        # print(f'+area: {y}, {x} -> {ny}, {nx}')
                        visited[ny, nx] = True
                        stack.append((ny, nx)) # je to pokracovanie oblasti, treba hladat dalej
                else:
                    perimeter += 1
            else:
                perimeter += 1
                
        
    return area, perimeter


if __name__ == "__main__":
    result = 0
    file_name = '12'
    matrix = tools.get_matrix(file_name)
    height, width = matrix.shape
    
    visited = np.full(matrix.shape, False, dtype=bool)
    
    for y in range(height):
        for x in range(width):
            if visited[y, x]:
                continue
            area, perimeter = get_area_and_perimeter(matrix, visited, y, x)
            result += area * perimeter
            # print(f'{matrix[y, x]}, perimeter: {perimeter}, area: {area}')
            
    print(result)
