"""
Tic Tac Toe Player
"""

import math
import copy

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
    if count_player(board, X) > count_player(board, O):
        return O
    elif count_player(board, O) > count_player(board, X):
        return X
    return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    move = set()
    for i,value in enumerate(board):
        for j, v in enumerate(value):
            if v == EMPTY:
                move.add((i,j))
    return move


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError
    
    copy_board = copy.deepcopy(board)
    copy_board[action[0]][action[1]] = player(board)

    return copy_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontal win
    for v in board:
        if v == [X, X, X]:
            return X
        elif v == [O, O, O]:
            return O
    
    # vertical win
    for j in range(3):
        if (board[0][j] == board[1][j] == board[2][j]):
            return board[0][j]
    
    # diagonal win
    if (board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]

    # other diagonal win
    if (board[2][0] == board[1][1] == board[0][2]):
        return board[1][1]
    
    # board is full?
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or (count_player(board, X) + count_player(board, O)==9):
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    Max = float("-inf")
    Min = float("inf")

    if player(board) == X:
        return Max_Value(board, Max, Min)[1]
    else:
        return Min_Value(board, Max, Min)[1]

def Max_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None]
    v = float('-inf')
    for action in actions(board):
        test = Min_Value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]

def Min_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None]
    v = float('inf')
    for action in actions(board):
        test = Max_Value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]


# count
def count_player(board, player):
    """
    Return el number of move by player
    """
    count = 0
    count = [count + f.count(player) for f in board]
    return sum(count)