import tools



print('hello')
# lines = tools.get_lines('1');
cols, len = tools.get_columns_as_ints('1')
sum = 0
cols[0].sort()
cols[1].sort()

for i in range(len):
    sum += abs(cols[0][i] - cols[1][i])
    
print(sum)