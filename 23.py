import tools
import numpy as np
import itertools
import math

class Node():
    def __init__(self, id):
        self.id = id
        self.children = set()
        self.id_list = ''
        self.ids = set()
        self.ids.add(id)
        
    def add(self, node):
        self.children.add(node)
        self.ids.add(node.id)
        
        node.children.add(self)
        node.ids.add(self.id)
    
    def create_id_list(self):
        self.id_list = self.id + ',' + ",".join(obj.id for obj in self.children )
        self.id_list2 = ','.join(sorted(self.ids))
        
    def __repr__(self):
        return f"{self.id_list}"    
        

if __name__ == "__main__":
    
    result = 0
    # file_name = '20'
    # file_name = '23'
    file_name = '23f'
    lines = tools.get_lines(file_name)
    node_list = {}
    id_list = set()
    for line in lines:
        id1, id2 = line.split('-')
        id_list.add(id1)
        id_list.add(id2)
        
        if id1 in node_list:
            n1 = node_list[id1]
        else:
            n1 = Node(id1)
            node_list[id1] = n1
    
        if id2 in node_list:
            n2 = node_list[id2]
        else:
            n2 = Node(id2)
            node_list[id2] = n2
        n1.add(n2) # prida aj n1 do 
    for node in node_list.values():
        node.create_id_list()
        
    tlist = [i for i in node_list.values() if i.id_list.startswith('t') or ',t' in i.id_list]
    
    # zoznam ids z prvkov, ktore obsahuju aspon jedno t
    ids = list([i.id for i in tlist])
    
    k = 3
    comb3 = itertools.combinations(ids, k)
    comb_cnt = math.comb(len(ids), k)
    
    cnt = 0
    for a, b, c in comb3:
        cnt += 1
        # if cnt % 1000 == 0:
        #     print(f'{cnt}/{comb_cnt}')
        if a[0] == 't' or b[0] == 't' or c[0] == 't':
            na, nb, nc = node_list[a], node_list[b], node_list[c]
            if a in nb.ids and a in nc.ids \
              and b in na.ids and b in nc.ids \
              and c in na.ids and c in nb.ids:
                # print(f'{a}, {b}, {c}')
                result += 1
                pass
            pass
        pass
    
    print(f"result: {result}")
