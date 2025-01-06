import tools
import numpy as np
from astar import AStar

class MazeAStar(AStar):
    def __init__(self, maze, start, end):
        super().__init__()
        self.maze = maze
        self.start = start    # (r, c)
        self.end = end        # (r, c)
        self.rows, self.cols = maze.shape
    
    def neighbors(self, node):
        # node: (r, c, dr, dc)
        r, c, dr, dc = node
        directions = [
            (-1,  0),  # hore
            ( 1,  0),  # dole
            ( 0, -1),  # vľavo
            ( 0,  1)   # vpravo
        ]
        for d_r, d_c in directions:
            nr, nc = r + d_r, c + d_c
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.maze[nr, nc] != '#':
                    yield (nr, nc, d_r, d_c)
    
    def distance_between(self, n1, n2):
        # n1: (r1, c1, dr1, dc1)
        # n2: (r2, c2, dr2, dc2)
        r1, c1, dr1, dc1 = n1
        r2, c2, dr2, dc2 = n2
        cost = 1
        # Prirážka za zmenu smeru vždy, ak sa zmení (dr, dc)
        if (dr1, dc1) != (dr2, dc2):
            cost += 1000
        return cost
    
    def heuristic_cost_estimate(self, current, goal):
        # current: (r1, c1, dr1, dc1)
        # goal: (r2, c2, dr2, dc2)
        r1, c1, _, _ = current
        r2, c2, _, _ = goal
        return abs(r1 - r2) + abs(c1 - c2)
    
    def is_goal_reached(self, current, goal):
        r1, c1, dr1, dc1 = current
        r2, c2, dr2, dc2 = goal
        return (r1, c1) == (r2, c2)
    
    def start_node(self):
        # Nastavíme počiatočný smer doprava
        return (self.start[0], self.start[1], 0, 1)
    
    def goal_node(self):
        return (self.end[0], self.end[1], 0, 0)


if __name__ == "__main__":
    result = -1
    file_name = '16'
    matrix = tools.get_matrix(file_name)

    # Získanie štartu a cieľa z matrixu
    sy, sx = np.where(matrix == 'S')
    start = (sy[0], sx[0])
    ey, ex = np.where(matrix == 'E')
    end = (ey[0], ex[0])
    
    height, width = matrix.shape
    use_renderer = False
    cell_size = 20
    
    colors = {
        '#': ('black', 'black', ' '),  # múr
        '.': ('white', 'white', ' '),  # prázdne miesto
        'S': ('green', 'white', ''),   # start
        'E': ('blue', 'white', ''),    # end
        '^': ('white', 'green', ''),   
        'v': ('white', 'green', ''),   
        '<': ('white', 'green', ''),   
        '>': ('white', 'green', '')    
    }

    if use_renderer:
        renderer = tools.get_renderer(matrix, colors, cell_size=cell_size, fps=30)

    finder = MazeAStar(matrix, start, end)
    path = finder.astar(finder.start_node(), finder.goal_node())

    if path is not None:
        # Nakoľko sme všetky náklady zarátali priamo v distance_between(),
        # nemusíme ich počítať znova. Ak chceš, môžeš overiť výsledok.
        # Ale tu nepotrebuješ ďalšiu kalkuláciu, A* ti už našla najlacnejšiu cestu.
        # print("Nájdená cesta:", [(r,c) for (r,c,dr,dc) in path])
        # Ak predsa chceš spätne overiť skóre:
        total_score = 0
        prev = None
        for node in path:
            if prev is None:
                prev = node
                continue
            r1,c1,dr1,dc1 = prev
            r2,c2,dr2,dc2 = node
            step_cost = 1
            if (dr1, dc1) != (dr2, dc2):
                step_cost += 1000
            total_score += step_cost
            prev = node
        
        result = total_score
        print("Celkové skóre:", total_score)
    else:
        print("Cesta neexistuje.")
        
    if use_renderer:
        tools.renderer_close(renderer)

    print(result)
