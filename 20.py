import tools
import numpy as np
import math
from astar import AStar

root = None

class Node():
    def __init__(self, y, x, idx, prev):
        self.y = y
        self.x = x
        self.next = None
        self.prev = prev
        self.idx = idx
        self.neighbors = []
        pass
    
    def __repr__(self):
        # Vráti čitateľný text s relevantnými informáciami
        return f"idx: {self.idx}, (y,x)=({self.y},{self.x}), neigh#={len(self.neighbors)})"    

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


def set_bridges():
    sum = 0
    cnt = 0
    dyx = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    ]
    
    node = root
    while True:
        y, x = node.y, node.x
        for dy, dx in dyx:
            if dy != 0:
                ny = y + dy
                ny2 = ny + dy
                if -1 < ny2 < height and matrix[ny, x] == '#' and matrix[ny2, x] == 'o':
                    matrix[ny, x] = 'x'
                    nd2 = node_list[(ny2, x)]
                    if nd2.idx > node.idx: # berieme len dopredne cesty
                        node.neighbors.append((y, x, nd2))
                        usp = nd2.idx - node.idx - 2
                        if usp >= 100:
                            sum += usp
                            cnt += 1
                        # print(f'{usp}')
            else:
                nx = x + dx
                nx2 = nx + dx
                if -1 < nx2 < width and matrix[y, nx] == '#' and matrix[y, nx2] == 'o':
                    matrix[y, nx] = 'x'
                    nd2 = node_list[(y, nx2)]
                    if nd2.idx > node.idx: # berieme len dopredne cesty
                        node.neighbors.append((y, x, nd2))
                        usp = nd2.idx - node.idx - 2
                        if usp >= 100:
                            sum += usp
                            cnt += 1
                        # print(f'{usp}')
        node = node.next
        if not node:
            break
    return sum, cnt
    
                        
def render(result, cell_size, matrix, window_size=(800,600)):
    colors = {
        '#': ('gray', 'black'), # múr
        'x': ('gray', 'yellow'), # prechadzatelny múr
        '.': ('white', 'white'),  # prázdne miesto
        'o': ('green', 'black'),  # start
        'S': ('blue', 'black'),  # start
        'E': ('red', 'black')  # start
    }
    tools.render_matrix(matrix, colors, caption=str(result), cell_size=cell_size, window_size=window_size, font_size=13)

if __name__ == "__main__":
    
    result = []
    # file_name = '20'
    file_name = '20f'
    matrix = tools.get_matrix(file_name)
    height, width = matrix.shape

    # Získanie štartu a cieľa z matrixu
    sy, sx = np.where(matrix == 'S')
    start = (int(sy[0]), int(sx[0]))
    ey, ex = np.where(matrix == 'E')
    end = (int(ey[0]), int(ex[0]))
    
    finder = BasicAStar(matrix, start, end)
    path = list(finder.astar(finder.start, finder.end))
    
    idx = 0
    pfy, pfx = path[0]
    root = Node(pfy, pfx, idx, 0)
    prev = root
    node_list = {}
    node_list[(pfy, pfx)] = root
    for p in path[1:]:
        y, x = p
        idx += 1
        nn = Node(y, x, idx, prev)
        node_list[(y, x)] = nn
        
        prev.next = nn
        prev = nn
        if (y, x ) == end:
            continue
        matrix[y, x] = 'o'

    result = len(path) - 1

    y, x = start
    matrix[y, x] = 'o' # je to sucast cesty
    y, x = end
    matrix[y, x] = 'o'
    sum, cnt = set_bridges()
    
    render(result, 20, matrix)
    
    print(f"result: {result}, sum: {sum}, cnt: {cnt}")
