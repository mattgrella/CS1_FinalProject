def get_input():
    board = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    for i in range(9):
        for j in range(9):
            board[i][j] = input()
    return board

def not_in_row(row,num):
    for i in len(range(board)):
        if board[i][row] == str(num):
            return False
    return True

def create_set(board):
    
    
        
    
def solveSudoku(board):
    box1 = [board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]]
    box2 = [board[0][3], board[0][4], board[0][5], board[1][3], board[1][4], board[1][5], board[2][3], board[2][4], board[2][5]]
    box3 = [board[0][6], board[0][7], board[0][8], board[1][6], board[1][7], board[1][8], board[2][6], board[2][7], board[2][8]]
    box4 = [board[3][0], board[3][1], board[3][2], board[4][0], board[4][1], board[4][2], board[5][0], board[5][1], board[5][2]]
    box5 = [board[3][3], board[3][4], board[3][5], board[4][3], board[4][4], board[4][5], board[5][3], board[5][4], board[5][5]]
    box6 = [board[3][6], board[3][7], board[3][8], board[4][6], board[4][7], board[4][8], board[5][6], board[5][7], board[5][8]]
    box7 = [board[6][0], board[6][1], board[6][2], board[7][0], board[7][1], board[7][2], board[8][0], board[8][1], board[8][2]]
    box8 = [board[6][3], board[6][4], board[6][5], board[7][3], board[7][4], board[7][5], board[8][3], board[8][4], board[8][5]]
    box9 = [board[6][6], board[6][7], board[6][8], board[7][6], board[7][7], board[7][8], board[8][6], board[8][7], board[8][8]]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.':
                for num in range(1,10):
                    if (str(num) not in board[i]):
                        for row in range(len(board)):
                            if board[row][j] != str(num):
                                if board[i][j] in box1:
                                    if str(num) not in box1:
                                        board[i][j] = str(num)
                                    elif board[i][j] in box2:
                                        if str(num) not in box2:
                                            board[i][j] = str(num)
                                    elif board[i][j] in box3:
                                        if str(num) not in box3:
                                            board[i][j] = str(num)
                                    elif board[i][j] in box4:
                                        if str(num) not in box4:
                                            board[i][j] = str(num)
                                    elif board[i][j] in box5:
                                        if str(num) not in box5:
                                            board[i][j] = str(num)
                                    elif board[i][j] in box6:
                                        if str(num) not in box6:
                                            board[i][j] = str(num)
                                    elif board[i][j] in box7:
                                        if str(num) not in box7:
                                            board[i][j] = str(num)
                                    elif board[i][j] in box8:
                                        if str(num) not in box8:
                                            board[i][j] = str(num)
                                    else:
                                        if str(num) not in box9:
                                            board[i][j] = str(num)
                                
    
    
    
    
    
    
board = get_input()
solveSudoku(board)
print(board)