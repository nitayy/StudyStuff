import xo
import copy
import tools
import U_XO.u_xo_board as ub

# -------------- Functions for the tree --------------------------------------------------------------
def b_size():
    """
    Size for the functions.
    :return: 81
    """
    return 81




def next_mo(sqrs,depth=1,turn=True,sign='x'):
    """
    For getting the next move.
    :param depth: 
    :return: 
    """
    return find_best_move(sqrs,depth,turn,sign)

# **************************************************************************************************** #
def find_best_move(board,depth,myTurn,sign):
    """
    board=u_xo board.
    :param board: The u_xo board.
    :return:
    """

    if (finish(board) or board.free_sqrs()==[]): return None
    best_move=-(2**(b_size()**2))
    m=board.free_sqrs()[0]
    for move in board.free_sqrs():
        b=copy.deepcopy(board)
        b.ins2(move,sign)
        if (is_win(board.main_b,sign)):
            return move
        curr_move=minimax(b,depth,not myTurn,xo.opp_sign(sign))
        print("$$$$$$$$")
        if (curr_move >= best_move):
            best_move = curr_move
            m=move
        print("AAA",curr_move,best_move,m)
    print("The move was: ",m)
    return m

# ***************************************************************************************************** #

def minimax(board,depth,myTurn,sign):
    """

    :param depth:
    :param myTurn:
    :return:
    """
    #print(depth,end='\n')
    if (is_win(board.main_b, xo.opp_sign(sign)) ):
        if myTurn:
            return -(b_size() ** 2 + 1) + depth
        else:
            return (b_size() ** 2 + 1) - depth
    elif ub.check_for_draw(board.main_b) or board.free_sqrs()==[]: return 0

    if (myTurn):
        bestVal=-(2**10)
        print(board.free_sqrs())
        for move in board.free_sqrs():
            print("Move is:", move)
            b = copy.deepcopy(board)
            b.ins2(move, sign)
            value=minimax(b,depth+1,not myTurn, xo.opp_sign(sign))
            #print("My val: ", value)
            bestVal = max([bestVal,value])
        return bestVal

    else:
        bestVal = (2**10)
        print(board.free_sqrs())
        for move in board.free_sqrs():
            print("Move is:", move)
            b = copy.deepcopy(board)
            b.ins2(move, sign)
            value = minimax(b, depth + 1, not myTurn, xo.opp_sign(sign))
            #print("opp val: ",value)
            bestVal = min([bestVal, value])

        print("Best val is: ", bestVal)
        print("Free sqrs",board.free_sqrs())
        print("D is,",depth)
        #board.show()
        print("========================================================")
        board.main_b.show()
        return bestVal


# *****************************************************************************************************#

def is_win(board,sign):
    return ub.check_for_win(board,sign)

def finish(board):
    """
    Teh function gets a full u_xo board and checks if the game was finished.
    :param board: The board.
    :return: Trhe if the game was finish, False - Otherwise.
    """
    return ub.check_for_draw(board.main_b) or ub.check_for_win(board.main_b,'x') or ub.check_for_win(board.main_b,'o')