import tools
import numpy as np

dirs = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0)
}

def execute(matrix, command, ry, rx):
    # <^^>>>vv<v>>v<<
    dy, dx = dirs[command]
   
    newry, newrx = ry + dy, rx + dx
    c = matrix[newry, newrx]
    if c == '#':
        # neda sa
        return ry, rx
    elif c == '.':
        # pohnut robotkom
        matrix[ry, rx] = '.'
        matrix[newry, newrx] = '@'
        return newry, newrx
    
    # je tam O - treba zistit, ci tam je '.' pre #
    zy, zx = newry, newrx
    while matrix[zy, zx] == 'O':
        zy, zx = zy + dy, zx + dx
    if matrix[zy, zx] == '#': # nenaslo sa miesto na posunutie
        return ry, rx

    # assert
    # tu moze byt uz len '.' - miesto na posunutie
    # O z newry, newrx na ry, rx
    # a robotko na poziciu newry, newrx
    # vratit newry, newrx
    matrix[zy, zx] = 'O'
    matrix[newry, newrx] = '@'
    matrix[ry, rx] = '.'
    
    return newry, newrx

if __name__ == "__main__":
    result = 0
    file_name = '15'
    lines = tools.get_lines(file_name)
    matrix = tools.get_matrix(file_name, lambda line: not line.startswith('#'))
    height, width = matrix.shape
    use_renderer = True
        
    # get robot position
    rob_pos = np.where(matrix == '@')
    print("rob_pos:", rob_pos)
    ry = int(rob_pos[0][0])
    rx = int(rob_pos[1][0])

    command_lines = [line for line in lines if line and not line.startswith('#')]

    if use_renderer:
        pass

    # <^^>>>vv<v>>v<<
    for commands in command_lines:
        for command in commands:
            ry, rx = execute(matrix, command, ry, rx)
    
            if use_renderer:        
                pass
            pass
    
    for y in range(height):
        for x in range(width):
            if matrix[y, x] == 'O':
                result += y * 100 + x
    
    if use_renderer:        
        pass
    print(result)
