import tools
import numpy as np
from MatrixRenderer import MatrixRenderer

dirs_d_yx = {
    '>': (0, 1, '>^v'), # left, right
    '<': (0, -1, '<v^'),
    '^': (-1, 0, '^<>'), 
    'v': (1, 0, 'v><'),        
}

def update_renderer(renderer, matrix_empty, stack, visited, block, step):
    matrix_disp = matrix_empty.copy()
    
    # height, width = visited.shape
    # for y in range(height):
    #     for x in range(width):
    #         if visited[y, x]:
    #             matrix_disp[y, x] = 'x'
    by, bx = block
    if bx >= 0:
        matrix_disp[by, bx] = 'x'
                
    
    for st in stack:
        y, x, dirs, idx = st
        matrix_disp[y, x] = 'O'
    tools.renderer_update(renderer, matrix_disp, wait_for_keypress=wait_key, caption=str(step))
    
    

if __name__ == "__main__":
    
    result = -1
    file_name = '16'
    matrix = tools.get_matrix(file_name)
    matrix_empty = matrix.copy()
    matrix_disp = matrix.copy()
    
    height, width = matrix.shape
    use_renderer, wait_key, cell_size, fps, font_size = True, False, 6, 100, 6
    # use_renderer = False
    
    colors = {
        '#': ('black', 'black', ' '), # múr
        '.': ('white', 'white', ' '),  # prázdne miesto
        'S': ('green', 'white', ''),  # start
        'E': ('blue', 'white', ''),   # end
        '^': ('white', 'green', ''),   # up
        'v': ('white', 'green', ''),   # dn
        '<': ('white', 'green', ''),   # left
        '>': ('white', 'green', ''),   # rght
        'O': ('red', 'green', ''),   # point
        'x': ('yellow', 'yellow', ' '),  # prázdne miesto
        
    }

    if use_renderer:
        renderer = tools.get_renderer(matrix, colors, cell_size=cell_size, fps=fps, font_size=font_size)  # 1 snímky za sekundu

    visited = np.full((height, width), False, dtype=bool)

    start_y, start_x = map(int, np.where(matrix == 'S'))
    stack = []
    
    _, _, d = dirs_d_yx['>']
    stack.append([start_y, start_x, d, 0]) # sy, sx, '>^v', 0
    step = 0
    block = (-1, -1)
    
    while stack:
        step += 1
        if use_renderer:
            if step % 1000 == 0:
                update_renderer(renderer, matrix_empty, stack, visited, block, step)
        last = stack[-1]
        y, x, dirs, idx = last # posledny prvok
        c = matrix[y, x]
        visited[y, x] = True
        # block = (y, x)
        if c == 'E':
            pass
        
        if step == 119:
            # wait_key = True
            pass

        by, bx = block
        # next move
        for i in range(idx, 3):
            dirs_char = dirs[i]
            dy, dx, next_dirs = dirs_d_yx[dirs_char]
            ny, nx = y + dy, x + dx
            nc = matrix[ny, nx]
            if nc == '#'  \
                or nc == '.' and ny == by and nx == bx \
                or nc == '.' and visited[ny, nx] \
                or nc == '.' and last[3] >= 2: # mur
                if i >= 2:
                    stack.pop()
                    visited[y, x] = False
                    block = (y, x)
                continue
            elif nc == '.':
                last[3] += 1
                # _, _, d = dirs_d_yx[dirs]
                stack.append([ny, nx, next_dirs, 0])

                break
            elif nc == 'E':
                pass
            elif nc == 'S':
                pass
                next
                pass
        
        continue
        valid, ny, nx, ndir = get_next(y, x, dirs, next_dir)
        if valid:
            stack.append((ny, nx, ndir, ndir))
        else:
            pass
        
        # toto je validny krok
        # visited[y, x] = True
        # steps.append((y, x, dir_char))
        # if use_renderer:
        #     matrix_disp = matrix_empty.copy()
        #     for step in steps:
        #         _y, _x, _c = step
        #         matrix_disp[_y, _x] = _c
        #     tools.renderer_update(renderer, matrix_disp, wait_for_keypress=True)
        
        # to zobrazit zmenu
        
                    
            # if use_renderer:
            #     tools.renderer_update(renderer, wait_for_keypress=False)
    if use_renderer:
        tools.renderer_close(renderer) 

        
    print(result)
