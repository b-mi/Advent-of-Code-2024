import tools
import numpy as np
import math


if __name__ == "__main__":
    
    result = 0
    file_name= '24f'
    lines = tools.get_lines(file_name)
    
# x00: 1
# x01: 0
# x02: 1
# x03: 1
# x04: 0
# y00: 1
# y01: 1
# y02: 1
# y03: 1
# y04: 1

# ntg XOR fgs -> mjb
# y02 OR x01 -> tnw
# kwq OR kpj -> z05
# x00 OR x03 -> fst    
    
    # read input
    mode = 0
    vals = {}
    exps = []
    for line in lines:
        if not line:
            mode += 1
            if mode > 1:
                break
            continue
        
        if mode == 0:
            name, val = line.split(':')
            vals[name] = int(val)
            pass
        else:
            # ntg XOR fgs -> mjb
            parts = line.split(' ')
            #       arg1       oper      arg2     result    done
            arr = [parts[0], parts[1], parts[2], parts[4], False]
            exps.append(arr)
    
    not_solved = True
    cnt = 0
    while not_solved:
        cnt += 1
        print(cnt)
        # evaluate
        not_solved = False
        for data in exps:
            arg1, oper, arg2, res_name, done = data
            if arg1 in vals and arg2 in vals:
                v1, v2 = vals[arg1], vals[arg2]
                if oper == "AND":
                    rslt = v1 & v2
                elif oper == "OR":
                    rslt = v1 | v2
                else: #XOR
                    rslt = v1 ^ v2
                
                if not res_name in vals:
                    vals[res_name] = rslt
                else:
                    pass
            else:
                not_solved = True
                    
    z = [(k, v) for k, v in vals.items() if k[0] == 'z']
    zs = sorted(z, key=lambda item: item[0], reverse=True)
    zstr = ''
    for i in zs:
        zstr += str(i[1])
    result = int(zstr, 2)
    print("end", result)
