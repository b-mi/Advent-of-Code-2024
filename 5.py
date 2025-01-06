import tools


class TreeNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent  # Nadriadený uzol
        self.children = []    # Zoznam detí
        self.dct_children = {}

    def add_child(self, child):
        """Pridanie dieťaťa do uzla."""
        child.parent = self
        self.children.append(child)
        self.dct_children[child.value] = child

    def __repr__(self):
        return f"TreeNode(value={self.value})"

    

lines = tools.get_lines('5f')
dctNodes = {}
mode = 1
pages = []

for line in lines:
    if line == '':
        mode = 2 # cisla stranok
        continue
    if mode == 1:
        parent_key, children_key = line.split('|')
        if parent_key not in dctNodes:
            parent_node = TreeNode(parent_key)
            dctNodes[parent_key] = parent_node
            
        parent_node = dctNodes[parent_key]
            
        if children_key not in dctNodes:
            children_node = TreeNode(children_key)
            dctNodes[children_key] = children_node
        
        children_node = dctNodes[children_key]
        parent_node.add_child(children_node)
    else:
        pages.append(line.split(','))

result = 0
    
for pg in pages:
    node = dctNodes[pg[0]]
    ok = True
    for i in range(1, len(pg)):
        key = pg[i]
        if key in node.dct_children:
            node = node.dct_children[key]
        else:
            ok = False
    if ok:
        middle_idx = int( ( len(pg) - 1 ) / 2)
        middle_value = pg[middle_idx]
        result += int(middle_value)


                

    
print(result)



# a uloha

#    x, y
# dirs = [
#     ( 1,  0),
#     ( 1,  1),
#     ( 0,  1),
#     (-1,  1),
#     (-1,  0),
#     (-1, -1),
#     ( 0, -1),
#     ( 1, -1),
# ]

# result = 0

# for y in range(rows):
#     for x in range(cols):
#         if matrix[y,x] == 'X':
#             for dir in dirs:
#                 ok = True
#                 dx, dy = dir
#                 new_x = x
#                 new_y = y
#                 for c in 'MAS':
#                     new_x += dx
#                     new_y += dy
#                     if new_x < 0 or new_y < 0 or new_x >= cols or new_y >= rows:
#                         ok = False
#                         break # out of range
#                     if matrix[new_y, new_x] != c:
#                         ok = False
#                         break  # is not part of XMAS
#                 if ok:
#                     result += 1
                    