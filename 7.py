import tools
import itertools

# print(list(itertools.product([0, 1], repeat=4)))
# print(itertools.product([0, 1], repeat=4))
# pass

result = 0
lines = tools.get_lines('7f')

for line in lines:
    parts = line.split(':')
    res = int(parts[0])
    str_vals = parts[1].strip().split(' ')
    int_vals = [int(x) for x in str_vals]
    
    oper_count = len( int_vals ) - 1
    opers_perms = list(itertools.product([0, 1], repeat=oper_count))
    for opers in opers_perms:
        r = int_vals[0]
        for idx in range(oper_count):
            oper = opers[idx]
            if oper == 0:
                r += int_vals[idx + 1]
            else:
                r *= int_vals[idx + 1]
        if r == res:
            result += r
            break


print(result)
pass