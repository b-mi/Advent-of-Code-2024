import tools

def get_correct(pgs):
    correct = []
    # 75,97,47,61,53 becomes 97,75,47,61,53
    pgs = pgs.copy()
    while pgs:
        right_page = pgs.pop()
        # zisti, ci existuje kombinacia N | test_page
        found = False
        for left_page in pgs:
            if (left_page, right_page) in rules:
                found = True
                break
        if found:
            # naslo sa to na pravej strane, nie je to prva hodnota
            pgs.insert(0, right_page)
        else:
            correct.append(right_page)
    
    return correct


lines = tools.get_lines('5f')
mode = 1
pages = []
rules = set()

# nacitanie rules a pages
for line in lines:
    if line == '':
        mode = 2 # cisla stranok
        continue
    if mode == 1:
        node_key, child_key = line.split('|')
        rules.add((node_key, child_key))
    else:
        pages.append(line.split(','))


# vyhladanie ok, a bad
result = 0
bad_cnt = 0
for pgs in pages:
    ok = True
    for start_idx in range(1, len(pgs)):
        parent, child = pgs[start_idx-1], pgs[start_idx]
        if not (parent, child) in rules:
            ok = False
            break
    if ok:
        # middle_idx = int( ( len(pgs) - 1 ) / 2)
        # middle_value = pgs[middle_idx]
        # result += int(middle_value)
        pass
    else:
        bad_cnt += 1
        correct_pages = get_correct(pgs)
        middle_idx = int( ( len(correct_pages) - 1 ) / 2)
        middle_value = correct_pages[middle_idx]
        result += int(middle_value)
        # print(f'bad: {pgs} -> {correct_pages}')
       
print(result)

