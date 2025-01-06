import tools
import itertools
import math

if __name__ == "__main__":
    result = 0
    file_name = '9f'
    src = tools.get_string(file_name)
    
    # unpack map
    unpacked = []
    is_file = True
    id: int = 0
    for c in src:
        ic = int(c)
        for _ in range(ic):
            if is_file:
                unpacked.append(id)
            else:
                unpacked.append(-1)
        if is_file:
            id += 1
        is_file = not is_file
                
    
    # print ('unpacked')
    # print(unpacked)
    
    # move from back to free place
    
    end_idx = len(unpacked) - 1
    start_idx = 0
    
    while end_idx > start_idx:
        # najst cislo > -1
        while unpacked[end_idx] == -1:
            end_idx -= 1
        while unpacked[start_idx] != -1:
            start_idx += 1
        # print((start_idx, end_idx))
        
        unpacked[start_idx] = unpacked[end_idx]
        start_idx += 1
        unpacked[end_idx] = -1
        end_idx -= 1
    
    
    # checksum
    idx = 0
    id = 0
    while unpacked[idx] > -1:
        result += unpacked[idx] * id
        idx += 1
        id += 1
    # print(unpacked)
    print(result)
