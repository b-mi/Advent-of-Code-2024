import tools
import numpy as np

dirs = {
    '<': (0, -1, True),
    '>': (0, 1, True),
    '^': (-1, 0, False),
    'v': (1, 0, False)
}

step_counter = 0

def execute(matrix, command, ry, rx):
    global step_counter
    step_counter += 1

    # <^^>>>vv<v>>v<<
    dy, dx, is_horizontal = dirs[command]
   
    newry, newrx = ry + dy, rx + dx
    c2 = matrix[newry, newrx]
    if c2 == '#':
        # neda sa
        return ry, rx
    elif c2 == '.':
        # pohnut robotkom
        matrix[ry, rx] = '.'
        matrix[newry, newrx] = '@'
        # tools.print_numpy_2d_array(matrix, command, [])
        return newry, newrx
    
    # je tam [] - treba zistit, ci tam je '.' pre #
    if is_horizontal:
        zy, zx = newry, newrx
        c2 = matrix[zy, zx]
        while c2 == '[' or c2 == ']':
            zy, zx = zy + dy, zx + dx
            c2 = matrix[zy, zx]
        if matrix[zy, zx] == '#': # nenaslo sa miesto na posunutie
            return ry, rx

        for x in range(zx, newrx, -dx):
            matrix[zy, x] = matrix[zy, x - dx]
        matrix[newry, newrx] = '@'
        matrix[ry, rx] = '.'
        # tools.print_numpy_2d_array(matrix, command, [])
    else:
        stack = []
        yy, xx = newry, newrx
        found_wall = False
        stack.append((yy, xx))
        assert matrix[yy, xx ] == '[' or matrix[yy, xx ] == ']'
        
        if matrix[yy, xx] == ']':
            stack.append((yy, xx - 1)) # testovat ci tam je [
            assert matrix[yy, xx - 1 ] == '[' or matrix[yy, xx - 1 ] == ']'
                
        else:
            stack.append((yy, xx + 1)) # testovat ci tam je ]
        
        data = []
        data.append((ry, rx, newry, '@'))

        while stack:
            _y, _x = stack.pop()
            c = matrix[_y, _x]         # znak nad/pod
            
            _y2 = _y + dy               # suradnica pre znak nad/pod
            c2 = matrix[_y2, _x]         # znak nad/pod
            if c2 == '#':
                # stena, stop, nemoze sa ist vertikalne
                found_wall = True
                break
            if c2 == '.':
                # ok, toto nebrani v pohybe
                data.append((_y, _x, _y2, c))
                continue
            
            # je tam [ alebo ] - testovat ci to tak je
            stack.append((_y2, _x)) # testovat ci tam je [
            assert matrix[_y2, _x] == '[' or matrix[_y2, _x] == ']'
                
            data.append((_y, _x, _y2, c))
            
            if c2 == ']':
                stack.append((_y2, _x - 1)) # testovat ci tam je [
                assert matrix[_y2, _x - 1] == '[' or matrix[_y2, _x - 1] == ']'
                    
            else:
                stack.append((_y2, _x + 1)) # testovat ci tam je ]
                assert matrix[_y2, _x + 1] == '[' or matrix[_y2, _x + 1] == ']'
           
        if step_counter == 22:
            pass            
        if not found_wall:
            visited = set()
            while data:
                data_itm = data.pop()
                _fromy, _x, _toy, c = data_itm
                if data_itm in visited:
                    continue
                visited.add(data_itm)
                matrix[_toy, _x] = c
                matrix[_fromy, _x] = '.'
                # tools.print_numpy_2d_array(matrix, '', [])
        else:
            newry, newrx = ry, rx
    
    return newry, newrx

if __name__ == "__main__":
    result = 0
    file_name = '15f'
    lines = tools.get_lines(file_name)
    matrix0 = tools.get_matrix(file_name, lambda line: not line.startswith('#'))
    height, width = matrix0.shape
    
    # double width matrix
    matrix = np.full((height, width*2), '?' )
    for y in range(height):
        for x in range(width):
            dblx = x * 2
            c = matrix0[y, x]
            if c == '#' or c == '.':
                matrix[y, dblx] = c
                matrix[y, dblx + 1] = c
            elif c == '@':
                matrix[y, dblx] = c
                matrix[y, dblx + 1] = '.'
            elif c == 'O':
                matrix[y, dblx] = '['
                matrix[y, dblx+1] = ']'
    
    height, width = matrix.shape
    use_renderer = True
        
    # get robot position
    rob_pos = np.where(matrix == '@')
    print("rob_pos:", rob_pos)
    ry = int(rob_pos[0][0])
    rx = int(rob_pos[1][0])
    
    colors = [
        (0, 1, 'r'),
        (1, 2, 'g'),
        (2, 3, 'b'),
        (4, 3, 'y'),
    ]

    command_lines = [line for line in lines if line and not line.startswith('#')]

    if use_renderer:
        tools.print_numpy_2d_array(matrix, 'START', [])

    # <^^>>>vv<v>>v<<
    for commands in command_lines:
        for command in commands:
            ry, rx = execute(matrix, command, ry, rx)
            # tools.print_numpy_2d_array(matrix, 'END', colors)
            pass
            

    if use_renderer:
        tools.print_numpy_2d_array(matrix, 'END', colors)

    
    for y in range(height):
        for x in range(width):
            if matrix[y, x] == '[':
                result += y * 100 + x
    
    print(result)
