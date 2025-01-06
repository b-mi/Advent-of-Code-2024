import tools
import math

def gen_prog(a, program):
    # a = 117440
    result = []
    if a == 117440:
        pass
    A, B, C = a, 0,  0
    index, opcode, operand_literal, operand_comb = 0, 0, 0, 0
    prog_len = len(program)
    
    while True:
        if index >= prog_len:
            break
        opcode = program[index]
        operand_literal = program[index+1]
        
        operand_comb = operand_literal
        if operand_literal == 4:
            operand_comb = A
        elif operand_literal == 5:
            operand_comb = B
        elif operand_literal == 6:
            operand_comb = C
            
        match opcode:
            case 0:
                x = A // (2**operand_comb)
                A = x
            case 1:
                x = B ^ operand_literal
                B = x
            case 2:
                x = operand_comb % 8
                B = x
            case 3:
                if A != 0:
                    index = operand_literal
            case 4:
                x = B ^ C
                B = x
            case 5:
                x = operand_comb % 8
                result.append(x)

                if len(result) > prog_len:
                    return 0
                
                idx = len(result)
                if program[idx - 1] != x:
                    return 0
            case 6:
                x = A // (2**operand_comb)
                B = x
            case 7:
                # x = math.trunc( A / (2**operand) )
                x = A // (2**operand_comb)
                C = x
                
            case _:
                pass
        if opcode == 3 and A != 0:
            pass
        else:
            index += 2
    if len(result) == prog_len:
        return a
    return 0

    

if __name__ == "__main__":
    
    A = 3100000000
    B = 0
    C = 0
    
    program = [2,4,1,1,7,5,0,3,1,4,4,0,5,5,3,0]
    
    while True:
        A += 1
        if A % 100_000_000 == 0:
            print(A)
        res = gen_prog(A, program)
        if res > 0:
            print(f'*{res}')

    print()
    print()
    print(",".join(map(str,result)))
