MAX_SIZE = 8
queen = [None] * MAX_SIZE

def attack(row,col):
    global queen
    i=0
    atk=0
    offset_row=offset_col=0
    while (atk!=1)and i<col:
        offset_col=abs(i-col)
        offset_row=abs(queen[i]-row)
        
        if queen[i]==row or offset_row==offset_col:
            atk=1
        i=i+1
    return atk

def decide_position(value):
    global queen
    i=0
    while i<MAX_SIZE:
        if attack(i,value)!=1:
            queen[value]=i
            if value==7:
                print(queen)
            else:
                decide_position(value+1)
        i=i+1

decide_position(0)
