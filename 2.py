import tools

def is_row_ok(row):
    ok = True
    row_len = len(row)
    if row_len < 2:
        return False
    isUp = row[1] > row[0] 
    for idx in range(row_len - 1):
        diff = row[idx+1] - row[idx]
        if isUp:
            ok = 0 < diff < 4
        else:
            ok = -4 < diff < 0
        if not ok:
            break
    return ok

print('hello')
rows = tools.get_rows_as_ints('2f')
sum = 0
for row in rows:
    ok = is_row_ok(row)
    
    if not ok and len(row) > 2:
        # testovat znova s vyradenim jedneho cisla
        for removed_idx in range(len(row)):
            row_copy = row[:removed_idx] + row[removed_idx+1:]
            ok = is_row_ok(row_copy)
            if ok:
                break
    if ok:
        sum += 1
    
print(sum)