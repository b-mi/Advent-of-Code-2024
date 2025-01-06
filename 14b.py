import tools
import numpy as np
from PIL import Image


def draw(board, second):

    # coords = [(28, 28), (58, 28), (28, 60), (58, 60), (43, 33)]
    ok = True
    # for x, y in coords:
    #     if board[y, x] == 0:
    #         ok = False
    #         break

    if ok:
        # if (second - 67) % 101 == 0:
        # Prevod na obrazok: 0 -> biela, iné hodnoty -> čierna
        # Hodnoty 0 sú mapované na 255 (biela) a ostatné na 0 (čierna)
        image_data = np.where(board == 0, 255, 0).astype(np.uint8)

        # Vytvorenie obrázka z numpy array
        img = Image.fromarray(image_data, mode='L')  # 'L' pre grayscale

        # Uloženie obrázka
        fn = f'p_{second:06}.png'
        img.save(fn)
    pass


if __name__ == "__main__":
    result = 0
    seconds = 7138
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
            
        draw(board, second)
    
    print(result)
