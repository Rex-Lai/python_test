# 8 queens problem
MAX_SIZE = 8
queen = [None] * MAX_SIZE
# queen[row] = col
solutions = 0
def check_atk(row, col):
    global queen
    atk = 0
    idx = 0
    offset_row=offset_col=0
    while atk != 1 and idx < row:
        offset_row = abs(idx - row)
        offset_col = abs(queen[idx] - col)
        if offset_row == offset_col or queen[idx] == col: # or idx == row:
            atk = 1
        idx += 1
    return atk

def check_position(val):
    global queen
    global solutions
    idx = 0
    while idx < MAX_SIZE:
        #raw_input('check ' + str(val) + ',' + str(idx))
        if check_atk(val, idx) != 1:
            queen[val] = idx
            if val == 7:
                solutions += 1
                print(solutions, queen)
                #raw_input('press any key...')
            else:
                check_position(val+1)
        idx += 1

check_position(0)