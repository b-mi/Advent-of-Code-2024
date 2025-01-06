import tools
import math

if __name__ == "__main__":
    
    result = []
    file_name = '17'
    lines = tools.get_lines(file_name)
    A = int(lines[0].replace("Register A: ", ""))
    B = int(lines[1].replace("Register B: ", ""))
    C = int(lines[2].replace("Register C: ", ""))
    
    program = list(map( lambda s: int(s), lines[4].replace("Program: ", "").split(',')))
    
    # debug
    # A, B, C = 0, 0, 9
    # program = [2,6]

    # A, B, C = 10, 0, 0
    # program = [5,0,5,1,5,4]

    # A, B, C = 2024, 0, 0
    # program = [0,1,5,4,3,0]

    # A, B, C = 0, 29, 0
    # program = [1,7]
    
    # A, B, C = 0, 2024, 43690
    # program = [4,0]    
    
    # A, B, C = 0, 2024, 43690
    # program = [4,0]

    A, B, C = 117440, 0, 0
    program = [0,3,5,4,3,0]
    
    
    index = 0
    opcode = 0  # instrukcia
    operand_literal = 0
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
                # print(f'{x},', end='')
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

    print()
    print()
    print(",".join(map(str,result)))
