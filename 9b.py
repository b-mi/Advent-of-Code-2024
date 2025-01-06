import tools

# nie je spravne

if __name__ == "__main__":
    result = 0
    file_name = '9'
    src = tools.get_string(file_name)
    
    # unpack map
    data = []
    is_file = True
    id: int = 0
    for c in src:
        ic = int(c)
        for _ in range(ic):
            if is_file:
                data.append(id)
            else:
                data.append(-1)
        if is_file:
            id += 1
        is_file = not is_file
                
    
    # print ('unpacked')
    # print(unpacked)
    
    # move from back to free place
    
    start_idx, start_len = 0, 0
    end_idx, end_len = len(data) - 1, 0
    
    while end_idx > start_idx:
        # najst cislo > -1
        while data[start_idx] != -1:
            start_idx += 1
            
        # najst dlzku volneho miesta na zaciatku
        dummy = start_idx
        start_len = 0
        while data[dummy] == -1:
            dummy += 1
            start_len += 1
        
        # najst zaciatok dat na konci
        while data[end_idx] == -1:
            end_idx -= 1
        
        # najst dlzku dat na konci
        dummy = end_idx
        end_len = 0
        c = data[end_idx]
        while data[dummy] == c:
            dummy -= 1
            end_len += 1
        
        # presun dat ak sa to zmesti
        if end_len <= start_len:
            # zmesti sa to tam
            for i in range(end_len):
                data[start_idx] = data[end_idx]
                data[end_idx] = -1
                start_idx += 1
                end_idx -= 1
            while data[start_idx] == -1:
                start_idx += 1
        else:
            # ak sa nezmesti posunut sa na dalsie data smerom k zaciatku
            end_idx -= end_len
    
    
    # checksum
    idx = 0
    id = 0
    while data[idx] > -1:
        result += data[idx] * id
        idx += 1
        id += 1
    # print(unpacked)
    print(result)
