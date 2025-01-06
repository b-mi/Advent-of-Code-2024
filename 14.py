import tools
import numpy as np


if __name__ == "__main__":
    result = 0
    seconds = 100
    file_name = '14'
    lines = tools.get_lines(file_name)
    width, height = 101, 103
    robots = []
    board = np.zeros((height, width), dtype=int)
    for line in lines:
        p_str, v_str = line.split(' ')
        p_str, v_str = p_str.replace('p=', ''), v_str.replace('v=', '')
        px, py = tuple(map(int, p_str.split(',')))
        vx, vy = tuple(map(int, v_str.split(',')))
        robots.append([px, py, vx, vy])
        board[py, px] += 1
    
    for second in range(seconds):
        for robot in robots:
            px, py, vx, vy = robot
            newx = (px + vx) % width
            newy = (py + vy) % height
            board[py, px] -= 1
            board[newy, newx] += 1
            robot[0], robot[1] = newx, newy
            
            pass
    
    quad = np.zeros((2, 2), dtype=int)
    half_width = width // 2
    half_height  = height // 2
    for y in range(height):
        for x in range(width):
            if x == half_width or y == half_height:
                continue
            qx = 0 if x < half_width else 1
            qy = 0 if y < half_height else 1
            quad[qy, qx] += board[y, x]
            # print(f'(x,y)=({x},{y}) -> (qx,qy) -> ({qx},{qy})')
    
    quad = quad.flatten()
    result = quad[0] * quad[1] * quad[2] * quad[3]
    print(result)
