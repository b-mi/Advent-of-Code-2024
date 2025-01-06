from numba import njit
import tools

@njit
def split_number(num):
    # Rozdelenie čísla na polovice pomocou matematických operácií
    digit_count = 0
    temp = num
    while temp > 0:
        temp //= 10
        digit_count += 1

    half_power = 10 ** (digit_count // 2)
    s1 = num // half_power  # Prvá polovica čísla
    s2 = num % half_power  # Druhá polovica čísla
    return s1, s2

@njit
def process_steps(arr, steps):
    for step in range(steps):
        print(step, len(arr))
        new_arr = []
        for idx in range(len(arr) - 1, -1, -1):
            if arr[idx] == 0:  # Ak je na kameni vyryté číslo 0, nahradí sa kameňom s číslom 1.
                new_arr.append(1)
                continue

            # Počet cifier sa počíta matematicky
            digit_count = 0
            temp = arr[idx]
            while temp > 0:
                temp //= 10
                digit_count += 1

            if digit_count % 2 == 0:  # Ak má číslo na kameni párny počet cifier
                s1, s2 = split_number(arr[idx])
                new_arr.append(s2)
                new_arr.append(s1)
                continue

            new_arr.append(arr[idx] * 2024)  # Ak sa neuplatní žiadne iné pravidlo, násobíme 2024.
        new_arr.reverse()
        arr = new_arr
    return len(arr)

if __name__ == "__main__":
    file_name = '11'
    arr = tools.get_rows_as_ints(file_name)[0]
    steps = 75
    result = process_steps(arr, steps)
    print(result)
