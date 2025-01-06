import tools
import numpy as np
from MatrixRenderer import MatrixRenderer

if __name__ == "__main__":
    
    result = -1
    file_name = '16'
    matrix = tools.get_matrix(file_name)
    matrix_empty = matrix.copy()
    matrix_disp = matrix.copy()
    
    height, width = matrix.shape
    use_renderer = True
    cell_size = 20
    
    colors = {
        '#': ('black', 'black', ' '), # múr
        '.': ('white', 'white', ' '),  # prázdne miesto
        'S': ('green', 'white', ''),  # start
        'E': ('blue', 'white', ''),   # end
        '^': ('white', 'green', ''),   # up
        'v': ('white', 'green', ''),   # dn
        '<': ('white', 'green', ''),   # left
        '>': ('white', 'green', ''),   # rght
    }

    if use_renderer:
        renderer = tools.get_renderer(matrix, colors, cell_size=cell_size, fps=30)  # 1 snímky za sekundu

    dyn = np.full((height, width),-1, dtype=int)
    visited = np.full((height, width), False, dtype=bool)
    dirs_lr = {
        '>': ('^', 'v'), # left, right
        '<': ('v', '^'),
        '^': ('<', '>'),
        'v': ('>', '<'),
    }
    
    dirs_d_yx = {
        '>': (0, 1), # left, right
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0),        
    }

    start_y, start_x = map(int, np.where(matrix == 'S'))
    stack = []
    steps = []
    stack.append((start_y, start_x, '>', 0))
    # zabocenie smer 0 = rovno, 1-vlavo, 2-vpravo
    
    # pridania dvoch pociatocnych smerov, o ktorych viem, ze su validne
    # pozicia a posledny smer, nasledujuce 
    # stack.append((start_y, start_x, '>', []))
    
    
    while stack:
        y, x, dir_char, dir_slr = stack[-1] # posledny prvok
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
        next_dir_slr = dir_slr
        if next_dir_slr == 0: # pokracovat rovno
            next_dir_char = dir_char
        elif next_dir_slr == 1: # odbocit vlavo
            l, _ = dirs_lr[dir_char]
            next_dir_char = l
        elif next_dir_slr == 2: # odbocit vpravo
            _, r = dirs_lr[dir_char]
            next_dir_char = r
        else:
            pass

        dy, dx = dirs_d_yx[next_dir_char]
        ny, nx = y + dy, x + dx
        nc = matrix[ny, nx]   # znak na dalsej pozicii s hodnotou 1
        if nc == '#': # stena
            next_dir_slr += 1
            continue
        elif nc == '.':
            if visited[ny, nx]:
                next_dir_slr += 1
                continue
            else:
                stack.append((ny, nx, next_dir_char, next_dir_slr))
                break
        elif nc == 'E':
            # spocitat steps
            pass
            # if len(pathx) == 35:
            #     pass
            # prev_c = '>'
            # score = 1
            # for c_idx in range( len(pathx) - 1, -1, -1):
            #     _, _, _c = pathx[c_idx]
            #     score += 1
            #     if _c != prev_c:
            #         score += 1000
            #     prev_c = _c
            # print(score, len(pathx) + 1)
            # if result == -1:
            #     result = score
            # elif score < result:
            #     result = score
            #     print(score)
        elif nc == 'S':
            # start, co s tym?
            pass
        else:
            raise Exception('toto nema nastat')
        if next_dir_slr == 3: # treba popnut
            stack.pop()
            stack.append()
            # visited[y, x] = False
    if use_renderer:
        tools.renderer_close(renderer) 

        
    print(result)
