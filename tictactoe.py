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
    Assumes that in the initial game state, X gets the first move, as per the spec.
    """
    numX, numO = 0, 0
    for i in board:
        for n in range(len(i)):
            if i[n] == X:
                numX += 1
            elif i[n] == O:
                numO += 1
    if numX == numO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError('Not a valid action')
    else:
        tempBoard = copy.deepcopy(board)
        turn = player(tempBoard)
        tempBoard[action[0]][action[1]] = turn
    return tempBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    Assumes there is at most one winner as per the spec.
    """
    for i in range(len(board)): # Checks if any player won with 3 in a row
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]

    for i in range(len(board)): # Checks if any player won with 3 in a column
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]: # Checks one diagonal
        return board[1][1]

    if board[0][2] == board [1][1] and board[1][1] == board[2][0]: # Checks the remaining diagonal
        return board[1][1]

    return None # Returns None if there is no winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


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
