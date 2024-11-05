def issafe(board,row,col):
    for i in range(row):
        if board[i]==col or abs(board[i]-col)==abs(i-row):
            return False
    return True


def solve(board,row):
    if row==8:
        print_board(board)
        return
    
    for i in range(8):
        if(issafe(board,row,i)):
            board[row]=i
            solve(board,row+1)
            board[row]=-1

def print_board(board):
    for i in range(8):
        row=['*']*8
        row[board[i]]='Q'
        print(' '.join(row))
    print()

board=[-1]*8
board[0]=0
solve(board,1)
