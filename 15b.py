import tools
import numpy as np
import MatrixRenderer

dirs = {
    '<': (0, -1, True),
    '>': (0, 1, True),
    '^': (-1, 0, False),
    'v': (1, 0, False)
}

use_renderer = True

def update_renderer(renderer, matrix, command):
    if use_renderer:        
        renderer.update_matrix(matrix)
        renderer.set_caption(command)
        renderer.render()
        renderer.tick()
        renderer.do_events()
        renderer.wait_for_keypress()



def execute(matrix, command, ry, rx):
    # <^^>>>vv<v>>v<<
    dy, dx, is_horiz = dirs[command]
   
    newry, newrx = ry + dy, rx + dx
    c = matrix[newry, newrx]
    if c == '#':
        # neda sa
        update_renderer(renderer, matrix, command)
        return ry, rx
    elif c == '.':
        # pohnut robotkom
        matrix[ry, rx] = '.'
        matrix[newry, newrx] = '@'
        update_renderer(renderer, matrix, command)
        return newry, newrx
    
    # je tam [] - treba zistit, ci tam je '.' pre #
    zy, zx = newry, newrx
    if is_horiz:
        while matrix[zy, zx] == '[' or matrix[zy, zx] == ']':
            zy, zx = zy + dy, zx + dx
            
        if matrix[zy, zx] != '.': # nenaslo sa miesto na posunutie
            update_renderer(renderer, matrix, command)
            return ry, rx
        
        if command == '<':
            for ex in range(zx, rx + 1):
                matrix[ry, ex] = matrix[ry, ex + 1]
            matrix[ry, rx] = '.'
        else:
            for ex in range(zx, rx, -1):
                matrix[ry, ex] = matrix[ry, ex - 1]
            matrix[ry, rx] = '.'
        update_renderer(renderer, matrix, command)
            
    else:
        stack = []
        if command == 'v':
            ok = False
            while True:
                if matrix[zy, zx] == '[':
                    box_pos = (zy, zx)
                else:
                    box_pos = (zy, zx - 1)
                stack.append(box_pos)
                    
                # if box_pos
                pass
                
            pass
        pass
    
    return newry, newrx

if __name__ == "__main__":
    result = 0
    file_name = '15'
    lines = tools.get_lines(file_name)
    matrix0 = tools.get_matrix(file_name, lambda line: not line.startswith('#'))
    height, width = matrix0.shape
    
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
    
    # get robot position
    rob_pos = np.where(matrix == '@')
    print("rob_pos:", rob_pos)
    ry = int(rob_pos[0][0])
    rx = int(rob_pos[1][0])

    command_lines = [line for line in lines if line and not line.startswith('#')]

    if use_renderer:
        renderer = MatrixRenderer.MatrixRenderer(matrix, cell_size=30, fps=2)  # 2 snímky za sekundu

    update_renderer(renderer, matrix, '?')
    

    # <^^>>>vv<v>>v<<
    for commands in command_lines:
        for command in commands:
            if use_renderer:
                renderer.do_events()
            ry, rx = execute(matrix, command, ry, rx)
                
            pass
    
    for y in range(height):
        for x in range(width):
            if matrix[y, x] == '[':
                result += y * 100 + x
    
    if use_renderer:        
        renderer.set_caption(str(result))
        renderer.wait_for_keypress()
        renderer.close()
    print(result)
