import tools

if __name__ == "__main__":
    result = 0
    file_name = '11'
    arr = tools.get_rows_as_ints(file_name)[0]

    for step in range(15):
        new_arr = []
        for idx in range(len(arr) - 1, -1, -1):

            if arr[idx] == 0: # Ak je na kameni vyryté číslo 0, nahradí sa kameňom s číslom 1.
                new_arr.append(1)
                continue
            
            sNum = str(arr[idx]) # Ak má číslo na kameni párny počet cifier, kameň sa rozdelí na dva kamene.
            str_len = len(sNum)
            if str_len % 2 == 0:
                half = str_len // 2
                s1 = sNum[: half]
                s2 = sNum[half:]
                new_arr.append(int(s2))
                new_arr.append(int(s1))
                
                continue

            new_arr.append(arr[idx] * 2024) # Ak sa neuplatní žiadne iné pravidlo, kameň sa nahradí novým kameňom, na ktorom je vyryté číslo získané vynásobením pôvodného čísla číslom 2024
        new_arr.reverse()
        arr = new_arr
        print(f'{arr}')
        pass
            
    print(len(arr))
