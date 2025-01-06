import tools

matrix = tools.get_matrix('4f')
rows, cols = matrix.shape

result = 0

dirs = [
    ( -1,  -1, 1,  1 ),
    ( -1,   1, 1, -1 ),
]

for y in range(rows):
    for x in range(cols):
        if matrix[y,x] == 'A':
            
            if x == 4 and y == 4:
                pass
            ok = True
            # zlava dole - doprava hore
            for dir in dirs:
                dx1, dy1, dx2, dy2 = dir
           
                x1 = x + dx1
                y1 = y + dy1
                
                x2 = x + dx2
                y2 = y + dy2
                
                if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
                    ok = False
                    break

                if x1 == cols or y1 == rows or x2 == cols or y2 == rows:
                    ok = False
                    break
                
                if not (matrix[y1, x1] == 'M' and matrix[y2, x2] == 'S' or matrix[y1, x1] == 'S' and matrix[y2, x2] == 'M'):
                    ok = False
                    break
            
            if ok:
                # print(f'y: {y}, x: {x}')
                result += 1
                
                

    
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
                    