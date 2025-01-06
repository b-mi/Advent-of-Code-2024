import tools
import re

str = 'do()?' + tools.get_string('3f') + "?don't()"
result = 0

do_don_t_parts = str.split('do()')

pattern_mul = r"mul\((-?\d+),(-?\d+)\)"

for do_dont_part in do_don_t_parts:
    if len(do_dont_part) == 0:
        continue
    do_part = do_dont_part.split("don't()")
    matches = re.findall(pattern_mul, do_part[0])
    for match in matches:
        a, b = match
        result += int(a) * int(b)
    

    
print(result)