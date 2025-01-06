import tools
import numpy as np
import math
from astar import AStar

max_subpart_len = 0
total_ok = 0

def check(s):
    global total_ok
    len_s = len(s)
    ret = True
    main_idx = 0
    sub_len = 1
    stack = []
    stack.append([0, 1])
    # r, wr, b, g, bwu, rb, gb, br
    # bwurrg    
    while True:
        last = stack[-1]
        start, sub_len = last
        if start == len_s:
            # ok, najdene
            # print(f'{s}: ok')
            total_ok += 1
            break
        if sub_len > max_subpart_len:
            stack.pop()
            if stack:
                stack[-1][1] += 1
                continue
            else:
                # bad, nenajdene
                # print(f'{s}: bad')
                break
        sub = s[start:start+sub_len]
        if sub in vars_set:
            stack.append([start+sub_len, 1])
        else:
            last[1] += 1

if __name__ == "__main__":
    
    result = 0
    total_ok = 0
    # file_name = '19'
    file_name = '19f'
    lines = tools.get_lines(file_name)
    vars = lines[0].split(', ')
    vars_sorted = sorted(vars, key=lambda s: (len(s), s))
    vars_set = set(vars)
    max_subpart_len = max(len(s) for s in vars)
    for line_idx in range( 2, len(lines)):
        line = lines[line_idx]
        check(line)
    result = total_ok
    print("end", result)
