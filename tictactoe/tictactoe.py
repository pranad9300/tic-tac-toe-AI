"""
Tic Tac Toe Player
"""

import math


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    else:
        O_count = board[0].count(O) + board[1].count(O) + board[2].count(O)
        X_count = board[0].count(X) + board[1].count(X) + board[2].count(X)
        if ( (O_count + X_count) % 2 == 0):
            return X
        else:
            return O



    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves_available = []
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == EMPTY:
                moves_available.append((i,j))
    return moves_available



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    t = player(board)
    if t == X:
        u = O
    else:
        u = X
    if ( (board[0][0] == u and board[0][1]==u and board[0][2]==u) or (board[1][0] == u and board[1][1]==u and board[1][2]==u) or (board[2][0] == u and board[2][1]==u and board[2][2]==u) or (board[0][0] == u and board[1][1]==u and board[2][2]==u) or (board[0][2] == u and board[1][1]==u and board[2][0]==u) or (board[0][0] == u and board[1][0]==u and board[2][0]==u) or (board[0][1] == u and board[1][1]==u and board[2][1]==u) or(board[0][2] == u and board[1][2]==u and board[2][2]==u)):
         return u
   
    else:
         return None      


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    t = winner(board)
    if  t == X or t == O:
       return True
    elif (EMPTY not in (board[0] or board[1] or board[2])): 
       return True
    else:
       return False 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
   
