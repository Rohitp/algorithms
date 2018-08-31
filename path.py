import numpy as np
import time

start = time.time()


BOARD_SIZE = 6


def canKnightBePlaced(board, x, y, knight, moves):    
    return not ( x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE or (board[x][y] > 0) )


def tour(board, knight, moves, x, y):
    if(knight >= BOARD_SIZE * BOARD_SIZE):
        return True
    
    for coords in moves:
        if canKnightBePlaced(board, x + coords[0], y + coords[1], knight, moves):
            board[x][y] = knight
            if (tour(board, knight + 1, moves, x + coords[0], y + coords[1])):
                return True
            
            board[x][y] = 0

    return False

def init():
    board = np.zeros(shape=(BOARD_SIZE, BOARD_SIZE))
    moves = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
    board[0][0] = 0
    if(tour(board, 1, moves, 0, 0)):
        print(board)
    else:
        print("No solution found")

init()

end = time.time()

print(end - start)
