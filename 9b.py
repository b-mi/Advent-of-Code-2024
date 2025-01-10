import tools
import itertools
import math

class Frag:
    def __init__(self, id, len, is_file):
        self.len = len
        self.is_file = is_file
        self.id = id if is_file else None
        self.next = None
        
    def __repr__(self):
        return f"{'file' if self.is_file else 'space'}({self.len}), {self.id}"


def xprint(ffrags):
    print()
    for f in ffrags:
        for i in range(f.len):
            c = str(f.id) if f.is_file else '.'
            print(c, end='')

if __name__ == "__main__":
    result = 0
    file_name = '9f'
    src = tools.get_string(file_name)
    
    # unpack map
    ffrags = []
    is_file = True
    id: int = 0
    for c in src:
        lngth = int(c)
        ffrags.append(Frag(id, lngth, is_file ))
        if is_file:
            id += 1
        is_file = not is_file

    space_lengths = set()
    ffrags_pop = ffrags.copy()
    id_reg = set()
    
    while ffrags_pop:
        file_frag = ffrags_pop.pop()
        
        # vyber fragmentu z konca
        if not file_frag.is_file:
            continue
        
        if file_frag.id in id_reg:
            continue
        
        id_reg.add(file_frag.id)
        
        # najdenie dostatocne velkeho space fragmentu
        if file_frag.len in space_lengths:
            # tak taka velkost nie je a toto sa neda presunut
            continue
        
        # taka velkost mozno je treba najst prvy space fragment dostatocnej velkosti
        found_space = False
        for space_frag in ffrags:
            if space_frag.is_file:
                if space_frag.id == file_frag.id:
                    # koniec dalej nehladame
                    break
                else:
                    continue
            else:
                if space_frag.len >= file_frag.len:
                    found_space = True
                    # mame miesto, budeme presuvat
                    if space_frag.len == file_frag.len:
                        # simple
                        # zo space frag urobime file frag a z file frag space frag
                        space_frag.is_file = True
                        space_frag.id = file_frag.id
                        file_frag.is_file = False
                        file_frag.id = None
                    else:
                        # tu treba z file frag urobit space
                        # ale space frag rozdelit na dva: file frag a zostatkovy space frag
                        new_space_len = space_frag.len - file_frag.len

                        space_frag.is_file = True
                        space_frag.id = file_frag.id
                        space_frag.len = file_frag.len
                        file_frag.is_file = False
                        file_frag.id = None
                        
                        new_space_frag = Frag(None, new_space_len, False)
                        idx = ffrags.index(space_frag)
                        ffrags.insert(idx + 1, new_space_frag)
                    # xprint(ffrags)
                    break
                else:
                    # nie je dostatocne miesto
                    continue
        
        if not found_space:
            space_lengths.add(file_frag.len)
        
        
    # xprint(ffrags)
    
    idx = 0
    ssum = 0
    for frag in ffrags:
        for i in range(frag.len):
            if frag.is_file:
                ssum += frag.id * idx
            idx += 1
    
    print()
    print('---')
    print(ssum)
        