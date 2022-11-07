# Min-max tree for tic-tac-toe game.
# The tree was built recursively.
# The code was taken from here: http://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
# with small changes....

import xo
import copy


class tree:
    def find_best_move(self,board,depth,myTurn,sign):
        """

        :param board:
        :return:
        """
        if (board.empty==[]): return None

        best_move=-(2**(board.s**2))
        m=board.empty[0]
        for move in board.empty:
            b=copy.deepcopy(board)
            b.ins(move,sign)
            if (self.is_win(b,sign)):
                return move
            curr_move=self.minimax(b,depth,not myTurn,xo.opp_sign(sign))
            if (curr_move >= best_move):
                best_move = curr_move
                m=move
            print(curr_move,best_move,m)

        return m

    # *****************************************************************************************************#

    def minimax(self,board,depth,myTurn,sign):
        """

        :param depth:
        :param myTurn:
        :return:
        """
        #print(depth,end='\n')
        if (self.is_win(board, xo.opp_sign(sign))):
            if myTurn:
                return -(board.s ** 2 + 1) + depth
            else:
                return (board.s ** 2 + 1) - depth
        elif board.is_full(): return 0

        if (myTurn):
            bestVal=-(2**700)
            for move in board.empty:
                b = copy.deepcopy(board)
                b.ins(move, sign)
                value=self.minimax(b,depth+1,not myTurn, xo.opp_sign(sign))
                #print("My val: ", value)
                bestVal = max([bestVal,value])
            return bestVal

        else:
            bestVal = (2**700)
            for move in board.empty:
                b = copy.deepcopy(board)
                b.ins(move, sign)
                value = self.minimax(b, depth + 1, not myTurn, xo.opp_sign(sign))
                #print("opp val: ",value)
                bestVal = min([bestVal, value])
            return bestVal


    # *****************************************************************************************************#
    def is_win(self,board, sign):
        """
        The function gets a board and a sign.
        :param board: The board.
        :param sign: The sign (There are only two options: x/o).
        :return: True if sign "wins" the board, i.e. some row or col or diag are all with then sing. Else return False.
        """

        temp=board.s
        wins = []  # The options to win at the game.
        for i in range(1, temp + 1):
            wins.append(board.get_col(i))
            wins.append(board.get_row(i))
        wins.append(board.get_diag1())
        wins.append(board.get_diag2())

        for i in wins:
            if (self.is_same(i, sign)):
                return True
        return False

    # *****************************************************************************************************#

    def control(self,board):
        """
        The function gets a xo board and returns how mush each sign
        :param board:
        :return: a dict of the sign:lines_control
        """
        temp = board.s
        wins = []  # The options to win at the game.
        for i in range(1, temp + 1):
            wins.append(board.get_col(i))
            wins.append(board.get_row(i))
        wins.append(board.get_diag1())
        wins.append(board.get_diag2())

        map = {'x':0, 'o':0}

        for c in wins:
            if (('x' in c) and ('o' not in c)): map['x']+=1 # ('x' in c) and ('o not in c)
            if (('o' in c) and ('x' not in c)): map['o'] += 1

        return map

    # *****************************************************************************************************#
    def is_same(self, l, sign):
        """
        The function get a list l and returns if ALL the list have the same sign.
        :param l: The list.
        :param sign: The sign.
        :return: True or false
        """

        for i in l:
            if (i != sign):
                return False
        return True