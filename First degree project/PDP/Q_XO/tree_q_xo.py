# Min-max tree for tic-tac-toe game.
# The tree was built recursively.
# The code was taken from here: http://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
# with small changes....

import Q_XO.q_xo_board as b
import Q_XO.judge_q_xo as j
import copy
import xo

def size():
    return 64**2


class tree:
    def find_best_move(self,board,depth,myTurn,sign):
        """

        :param board:
        :return:
        """
        ju=j.Judge_q_xo(board)
        free=ju.free_sqrs()
        if (ju.winner=='d'): return None

        best_move=-(2**(size()))
        m=free[0]
        for move in free:
            b=copy.deepcopy(board)
            b.ins(move,sign)
            if (ju.check_for_win('x')):
                return move
            curr_move=tree.minimax(self,b,depth,not myTurn,xo.opp_sign(sign),ju)
            if (curr_move >= best_move):
                best_move = curr_move
                m=move
            print(curr_move,best_move,m)

        return m

    # *****************************************************************************************************#

    def minimax(self, board,depth,myTurn,sign,jugde):
        """

        :param depth:
        :param myTurn:
        :return:
        """
        #print(depth,end='\n')
        ju = j.Judge_q_xo(board)
        if (jugde.check_for_win(xo.opp_sign(sign))):
            if myTurn:
                return -(size() ** 2 + 1) + depth
            else:
                return (size() ** 2 + 1) - depth
        elif jugde.check_for_draw() or jugde.game_finish(): return 0

        if (myTurn):
            bestVal=-(2**700)
            for move in ju.free_sqrs():
                b = copy.deepcopy(board)
                b.ins(move, sign,True)
                value=tree.minimax(self,b,depth+1,not myTurn, xo.opp_sign(sign),ju)
                print("My val: ", value)
                bestVal = max([bestVal,value])
            return bestVal

        else:
            bestVal = (2**700)
            for move in ju.free_sqrs():
                b = copy.deepcopy(board)
                b.ins(move, sign,True)
                value = tree.minimax(self, b, depth + 1, not myTurn, xo.opp_sign(sign),ju)
                print("opp val: ",value)
                bestVal = min([bestVal, value])
            return bestVal


    # *****************************************************************************************************#