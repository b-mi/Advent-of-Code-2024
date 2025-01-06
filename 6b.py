import tools
import numpy as np


matrix_orig = tools.get_matrix('6f')
height, width = matrix_orig.shape
result = 0


def get_guard_pos():
    x, y, dx, dy = -1, -1, -1, -1
    for _y in range(height):
        for _x in range(width):
            if matrix_orig[_y,_x] == '^':
                x, y, dx, dy = _x, _y, 0, -1
                # matrix_orig[y,x] = 'X'
                break
        if x > -1:
            break    
    return x, y, dx, dy

hx, hy, hdx, hdy = get_guard_pos()


def step():
    global hx, hdx, hy, hdy, result
    newx, newy = hx + hdx, hy + hdy
    cycled = False
    if newx < 0 or newy < 0 or newx == width or newy == height:
        return False, False
    c = matrix[newy, newx]
    ch = '?'
    if c != '#' and c != 'O':
        hx, hy = newx, newy
        if hdy == 0: # zmena x suradnice
            ch = '<' if hdx < 0 else '>'
        else:
            ch = '^' if hdy < 0 else 'v'
        cycled = matrix[hy, hx] == ch
        matrix[hy, hx] = ch
    # elif c == 'X':
    #     hx, hy = newx, newy
    #     cycled = True
    else: # # znak
        # prekazka otocit sa 
        if hdx == 0 and hdy == -1: # hore
            hdx, hdy = 1, 0
        elif hdx == 1 and hdy == 0: # vpravo
            hdx, hdy = 0, 1
        elif hdx == 0 and hdy == 1: # dole
            hdx, hdy = -1, 0
        elif hdx == -1 and hdy == 0: # vlavo
            hdx, hdy = 0, -1
    return True, cycled
        
_hx, _hy, _hdx, _hdy = hx, hy, hdx, hdy
for y in range(height):
    print(y)
    for x in range(width):
        # y, x = 6, 3
        matrix = matrix_orig.copy()
        if matrix[y, x] != '.':
            continue
        
        matrix[y, x] = 'O' # pridanie prekazky navyse na prazdne miesto
        # visited = np.full(matrix.shape, ' ', dtype=str)
        
        # reset start location
        hx, hy, hdx, hdy = _hx, _hy, _hdx, _hdy
        
        while True:
            cont, cycle = step()
            if not cont:
                break
            elif cycle:
                result += 1
                break
        matrix[y, x] = '.' # vratenie povodnej .
        

print(result)
