import tools
import numpy as np
import math


if __name__ == "__main__":
    
    result = 0
    file_name= '25f'
    matrix = tools.get_matrix(file_name, empty_char=' ')
    locks = []
    keys = []
    
    # reda keys and locks
    height, _ = matrix.shape
    y = 0
    while True:
        if matrix[y, 0] == '#' or matrix[y, 0] == '.':
            y_start = y + 1
            y_end = y_start + 5
            sums = []
            isLock = True if matrix[y, 0] == '#' else False
            for x in range(5):
                cnt_hash = 0
                for _y in range(y_start, y_end):
                    if matrix[_y, x] == '#':
                        cnt_hash += 1
                sums.append(cnt_hash)
            if isLock:
                locks.append(sums)
            else:
                keys.append(sums)
        else:
            raise Exception('error')
            
        y += 8
        if y > height:
            break


    # find ok keys
    for lock in locks:
        for key in keys:
            bad = False
            for x in range(5):
                if lock[x] + key[x] > 5:
                    bad = True
                    break
            if not bad:
                result += 1
    
    print("end", result)
