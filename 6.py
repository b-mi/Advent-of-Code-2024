import tools


matrix = tools.get_matrix('6f')
height, width = matrix.shape
result = 1                


def get_guard_pos():
    x, y, dx, dy = -1, -1, -1, -1
    for _y in range(height):
        for _x in range(width):
            if matrix[_y,_x] == '^':
                x, y, dx, dy = _x, _y, 0, -1
                matrix[y,x] = 'X'
                break
        if x > -1:
            break    
    return x, y, dx, dy

hx, hy, hdx, hdy = get_guard_pos()


def step():
    global hx, hdx, hy, hdy, result
    newx, newy = hx + hdx, hy + hdy
    if newx < 0 or newy < 0 or newx == width or newy == height:
        return False
    c = matrix[newy, newx]
    if c == '.':
        result += 1
        hx, hy = newx, newy
        matrix[hy, hx] = 'X'
    elif c == 'X':
        hx, hy = newx, newy
    elif c == '#':
        # prekazka otocit sa 
        if hdx == 0 and hdy == -1: # hore
            hdx, hdy = 1, 0
        elif hdx == 1 and hdy == 0: # vpravo
            hdx, hdy = 0, 1
        elif hdx == 0 and hdy == 1: # dole
            hdx, hdy = -1, 0
        elif hdx == -1 and hdy == 0: # vlavo
            hdx, hdy = 0, -1
    return True
        

while True:
    if not step():
        break

print(result)
