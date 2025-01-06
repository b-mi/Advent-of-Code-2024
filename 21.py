import tools
import numpy as np
import msvcrt
import os
from DebugFile import DebugFile
import time

xres = ''
db1 = ''
db2 = ''
debug = DebugFile()
wait_key = False


def xprint(txt='', end='\n'):
    debug.print(txt, end)

def repaint():
    debug.clear()
    xprint('----------------', end='')
    
    for idx in range(len(keybs)):
        keyb, loc = keybs[idx], locs[idx]
        cy, cx = loc
        height, width = keyb.shape
        for y in range(height):
            xprint()
            for x in range(width):
                color_start, color_end = '', ''
                if cy >= 0 and y == cy and x == cx:
                    # color_start, color_end = '\033[31m', '\033[0m'
                    color_start = '*'
                else:
                    color_start = ' '
                xprint(f'| {color_start}{keyb[y, x]}{color_end} ', end='')
            xprint('|', end='')
        xprint()
        xprint('----------------', end='')
    xprint()
    if wait_key:
        msvcrt.getch()

def press_key(key, key_idx):
    global xres, db1, db2
    # if key_idx == 0:
    db1 += key
    db2 += str(key_idx)
    print(db1)
    print(db2)
    
    keyb = keybs[key_idx]
    loc = locs[key_idx]
    if key_idx == 0: # human. key znamena vyber znaku a A
        loc[0], loc[1] = map(int, np.where(keyb == key))
        press_key(key, 1)
    else:
        y, x = loc
        oc = keyb[y, x]
        match key:
            case '<':
                x -= 1
                loc[0], loc[1] = y, x
            case '>':
                x += 1
                loc[0], loc[1] = y, x
            case 'v':
                y += 1
                loc[0], loc[1] = y, x
            case '^':
                y -= 1
                loc[0], loc[1] = y, x
            case 'A':
                chn = keyb[y, x]
                if key_idx == len(keybs) - 1:
                    xres += chn
                    print(xres)
                    # print(f'*{chn}*')
                else:
                    press_key( chn, key_idx + 1 )
        on = keyb[loc[0], loc[1]]
            
    
    pass        
                

def replay():
    key_list = [
        "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
        # "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A",
        # "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
        # "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A",
        # "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
    ]
    # keys = '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'
    # keys = '<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A'
    
    for key_line in key_list:
        xres = ''
        for keych in key_line:
            press_key(keych, 0)
            repaint()


def update_loc(dir_char, keyb_id):
    keyb = keybs[keyb_id]
    loc_st = locs[keyb_id]
    if keyb_id == 0:
        new_y, new_x = dir_loc[dir_char]
    else:
        cur_y, cur_x = loc_st
        dy, dx = dyx[dir_char]
        new_y, new_x = cur_y + dy, cur_x + dx
    loc_st[0], loc_st[1] = new_y, new_x 
    repaint()
    
    return keyb[new_y, new_x]

def exec( dir_char, keyb_id ):
    global db1, db2, main_dir
    # db1 += dir_char
    # db2 += str(keyb_id)
    # print(db1)
    # print(db2)
    
    
    if keyb_id == 0:
        # to je human keyb, stlaca priamo ten znak okamzite, automaticky priopagovane do dalsej klavenice
        update_loc(dir_char, keyb_id)
        exec( dir_char, keyb_id + 1)
        repaint()
        pass
    else:
        keyb = keybs[keyb_id]
        loc = locs[keyb_id]
        start_y, start_x = loc
        end_y, end_x = dir_loc[dir_char]
        
        if end_y == start_y and end_x == start_x:
            return # uz sme tam

        match(dir_char):
              case '<':
                  loc[1] -= 1
              case '>':
                  loc[1] += 1
              case '^':
                  loc[0] -= 1
              case 'v':
                  loc[0] += 1
    
    pass

def get_dir_for( curd, kidx ):
    dir = ''
    keyb = keybs[kidx]
    start_y, start_x = locs[kidx]
    end_y, end_x = dir_loc[curd]
    
    if start_x != end_x:
        if start_y == 0 and start_x == 1:
            dir = 'v'
        else:
            dir ='<' if end_x < start_x else '>'
    else:
        dir = '^' if end_y < start_y else 'v'
        
    return dir

def run2(main_dir):
    global db1
    kidx = 0
    
    curd = main_dir
    # <<vvAAv<<AA<AA<>>>>^^AAA<
    # 0101012010120120101010123        
    while True:
        dir1 = get_dir_for( curd, 1 )
        db1 += curd
        print(db1, end='')
        if dir1:
            c = update_loc(dir1, 0)
            db1 += dir1
            print(db1, end='')
            
            c = update_loc(dir1, 1)
            db1 += dir1
            print(db1, end='')
            
            
        else:
            break
    pass
    

if __name__ == "__main__":
    
    result = 0
    # file_name = '20'
    file_name = '21'
    lines = tools.get_lines(file_name)
    
    num_map = \
        [['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        [' ', '0', 'A']]
    keyb_num = np.array(num_map)
    loc_num = [3, 2]
    
    dir_map = \
        [[' ', '^', 'A'],
        ['<', 'v', '>']]

    dir_loc = {
        '<': (1, 0),
        'v': (1, 1),
        '>': (1, 2),
        '^': (0, 1),
        'A': (0, 2),
    }
    
    dyx = {
        '<': (0, -1),
        '>': (0, 1),
        'v': (1, 0),
        '^': (-1, 0),
        
    }

        
    keyb1_dir = np.array(dir_map)
    loc1_dir = [0, 2]
    
    keyb2_dir = np.array(dir_map)
    loc2_dir = [0, 2]
    
    keyb_human = np.array(dir_map)
    loc_human = [0, 2]
    
    keybs = [ keyb_human, keyb1_dir, keyb2_dir, keyb_num ]
    locs = [ loc_human, loc1_dir, loc2_dir, loc_num ]

    
    repaint()
    # replay()
    
    data = {
      "029A" : "<A^A^^>AvvvA" 
      #<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
    }
    # 029A <A^A^^>AvvvA
    # 980A ^^^A<AvvvA>A
    # 179A
    # 456A
    # 379A
    
    # <<vvAAv<<AA<AA<>>>>^^AAA<
    # 0101012010120120101010123    
    # <A^A^^>AvvvA
    
    main_dir = '<'
    run2('<')
    # exec( '<', 0 )
    # exec( 'A', 0 )

        
    
    print(f"result: {result}")
