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

    X_apperances = 0
    O_apperances = 0

    for line in board:
        for board_place in line:
            if board_place == X:
                X_apperances += 1
            elif board_place == O:
                O_apperances += 1
        
    if O_apperances < X_apperances:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    actions_set = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions_set.add((i,j))

    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    board_copy = copy.deepcopy(board)
    turn_player = player(board)
    board_copy[action[0]][action[1]] = turn_player

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != EMPTY:
        return board[0][0] 
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0] 
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != EMPTY:
        return board[0][0] 
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != EMPTY:
        return board[0][1] 
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != EMPTY:
        return board[1][0] 
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2] 
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != EMPTY:
        return board[2][0]
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != EMPTY:
        return board[0][2] 
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    win_state = winner(board)
    if win_state == X:
        return 1
    elif win_state == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None

    curr_player = player(board)

    # if player is X we wanna maximize the min value
    # if player is O we wanna minimize the max value
    
    if curr_player == X:
        move, value = max_val(board)
    elif curr_player == O:
        move, value = min_val(board)

    return move


def max_val(board):
    if terminal(board):
        return None, utility(board)
    v = float('-inf')
    move = None
    for action in actions(board):
        potential_move, aux = min_val(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return move, v

    return move, v


def min_val(board):
    if terminal(board):
        return None, utility(board)
    v = float('inf')
    move = None
    for action in actions(board):
        potential_move, aux = max_val(result(board, action))
        if (aux < v):
            v = aux
            move = action
            if v == -1:
                return move, v

    return move, v


