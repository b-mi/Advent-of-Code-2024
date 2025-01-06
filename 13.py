import tools
import numpy as np

def get_data(src: str, prefix: str, postfix: str):
    # Button A: X+94, Y+34
    # Button B: X+22, Y+67
    # Prize: X=8400, Y=5400    
    nums = src.replace(prefix, '').replace('X'+postfix, '').replace('Y'+postfix, '').strip().split(',')
    return int(nums[0]), int(nums[1])

def calculate(a, b, prize):
    a_token_price = 3
    b_token_price = 1
    
    a_dx, a_dy = a # hodnty pre suradnicu X
    b_dx, b_dy = b # hodnty pre suradnicu Y
    p_x, p_y = prize
    
    max_a = p_x // a_dx
    best_tokens_count = -1
    for a_count in range(max_a + 1):
        rest_for_b = p_x - a_count * a_dx
        if rest_for_b % b_dx != 0:
            continue # zbytok po deleni pre b nevytovri celociselny pocet b
        # na suradnic X mame zhodu
        b_count = rest_for_b // b_dx
        
        if a_count == 80:
            pass
        
        # je zhoda aj na suradnic y?
        y_test = a_count * a_dy + b_count * b_dy
        if y_test != p_y:
            continue
        
        tokens_count = a_count * a_token_price + b_count * b_token_price
        if best_tokens_count == -1:
            best_tokens_count = tokens_count
        else:
            best_tokens_count = min(tokens_count, best_tokens_count)
            
        pass
    return None if best_tokens_count == -1 else best_tokens_count

if __name__ == "__main__":
    result = 0
    file_name = '13'
    lines = tools.get_lines(file_name)
    txt = tools.get_string(file_name)
    parts = txt.split('\n\n')
    

    
    for part in parts:
        frags = part.split('\n')
        a = get_data(frags[0], 'Button A:', '+')
        b = get_data(frags[1], 'Button B:', '+')
        p = get_data(frags[2], 'Prize:', '=')
        
        tokens = calculate(a, b, p) 
        if not tokens:
            continue
        result += tokens
            
    print(result)
