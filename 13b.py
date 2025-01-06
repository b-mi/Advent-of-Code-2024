import tools
import numpy as np
import math
from scipy.optimize import linprog



def get_data(src: str, prefix: str, postfix: str):
    # Button A: X+94, Y+34
    # Button B: X+22, Y+67
    # Prize: X=8400, Y=5400    
    nums = src.replace(prefix, '').replace('X'+postfix, '').replace('Y'+postfix, '').strip().split(',')
    return int(nums[0]), int(nums[1])


def calc(A: int, B: int, C: int, D: int, N1: int, N2: int):
    # A, B = 94, 22
    # C, D = 34, 67
    # N1, N2 = 8400, 5400

    # Minimalizujeme 3*x + y
    c = [3, 1]
    A_eq = [[A, B],
            [C, D]]
    b_eq = [N1, N2]

    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=(None, None))

    if res.success:
        x, y = res.x
        return x, y
    else:
        return 0, 0
    

if __name__ == "__main__":

    result = 0
    file_name = '13'
    lines = tools.get_lines(file_name)
    txt = tools.get_string(file_name)
    parts = txt.split('\n\n')
    

    
    for part in parts:
        frags = part.split('\n')
        a, c = get_data(frags[0], 'Button A:', '+')
        b, d = get_data(frags[1], 'Button B:', '+')
        n1, n2 = get_data(frags[2], 'Prize:', '=')
        ext = 10000000000000
        n1, n2 = n1 + ext, n2 + ext
        # A, B = 94, 22
        # C, D = 34, 67
        # N1, N2 = 8400, 5400
        
        x, y = calc(a, b, c, d, n1, n2) 
        x, y = round(x), round(y)
        test1 = a * x + b * y
        test2 = c * x + d * y
        if test1 == n1 and test2 == n2:
            result += x * 3 + y
            
    print(result)
