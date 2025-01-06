import tools
import numpy as np
import math


if __name__ == "__main__":
    
    result = 0
    # file_name = '22'
    file_name = '22f'
    lines = tools.get_lines(file_name)
    cnt = 0
    for line in lines:
        cnt += 1
        if cnt % 100 == 0:
            print(cnt)
        sec_num = int(line)
        for i in range(2000):
            res = sec_num * 64
            sec_num = sec_num ^ res
            sec_num = sec_num % 16777216
            
            res = sec_num // 32
            sec_num = sec_num ^ res
            sec_num = sec_num % 16777216
            
            res = sec_num * 2048
            sec_num = sec_num ^ res
            sec_num = sec_num % 16777216
        result += sec_num
    
    print(f"result: {result}")
