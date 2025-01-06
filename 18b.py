import tools
import numpy as np
import math
from astar import AStar

class BasicAStar(AStar):
    def __init__(self, matrix, start, end):
        self.start = start
        self.end = end
        self.matrix = matrix
        self.height, self.width = matrix.shape
        self.dyx = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

    def neighbors(self, n):
        y, x = n
        for dy, dx in self.dyx:
            ny, nx = y + dy, x + dx
            if -1 < ny < self.height and -1 < nx < self.width and self.matrix[ny, nx] != '#':
                yield (ny, nx)
        # for n1, d in self.nodes[n]:
        #     yield n1

    def distance_between(self, n1, n2):
        return 1
            
    def heuristic_cost_estimate(self, n1, n2):
        (y1, x1) = n1
        (y2, x2) = n2
        rtn = math.hypot(x2 - x1, y2 - y1)
        return rtn
    
    def is_goal_reached(self, current, goal):
        if current == goal:
            pass
        return current == goal


if __name__ == "__main__":
    
    result = []
    # file_name, height, width, fall_count, cell_size = '18', 7, 7, 12, 25
    file_name, height, width, fall_count, cell_size = '18f', 71, 71, 1024, 10
    

    matrix = np.full((height, width), '.', dtype=str)
    coords_yx = []
    lines = tools.get_lines(file_name)
    for line in lines:
        sx, sy = map(int, line.split(','))
        coords_yx.append((sy, sx))

    start = (0, 0)
    end = (height - 1, width - 1)
    
    
    for idx in range(fall_count):
        y, x = coords_yx[idx]
        matrix[y, x] = '#'
    
    for idx in range(fall_count, len(coords_yx)):
        print(f'{idx}/{len(coords_yx)}')
        y, x = coords_yx[idx]
        matrix[y, x] = '#'
        finder = BasicAStar(matrix, start, end)
        result = finder.astar(finder.start, finder.end)
        if not result:
            print(f'Result')
            print(f'{x},{y}')
            break
        
    print("end")
