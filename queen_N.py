import numpy as np
import time

start = time.time()


BOARD_SIZE = 20


def isQueenUnderAttack(board, row, col):

    for x in range(col):
        if(board[row][x]):
            return True

    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if(board[x][y]):
                return True;

    for x, y in zip(range(row, BOARD_SIZE), range(col, -1, -1)):
        if(board[x][y]):
                return True;
        
    return False

def NQueen(board, col):
    if(col >= BOARD_SIZE):
        return True
    
    for row in range(BOARD_SIZE):
        if not isQueenUnderAttack(board, row, col):
            board[row][col] = 1
            if (NQueen(board, col + 1)):
                return True
            
            board[row][col] = 0

    return False

def init():
    board = np.zeros(shape=(BOARD_SIZE, BOARD_SIZE))
    if(NQueen(board, 0)):
        print(board)
    else:
        print("No solution found")

init()

end = time.time()

print(end - start)
