# Source for this file in:
# written at Python by Nitay Yehezkely
# http://stackoverflow.com/questions/3956258/minimax-explained-for-an-idiot
#------------imports---------------------------------
import xo
import tools
import itertools as it
import copy


class tree:
    tr=[] #For the tree moves
    opp=[] # for the opp moves.

    #*****************************************************************************************************#

    def is_same(self,l, sign):
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

    #*****************************************************************************************************#

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

    #*****************************************************************************************************#
    def minimax(self,board,sign='x'):
        """

        :param board:
        :param sign:
        :return: The first step to do
        """

        if (5 in board.empty): return 5
        if (len(board.empty)==8): return 1

        score=(board.s**2)
        key={}
        for i in board.empty:
            key[i]=0
        for i in [len(board.empty)]:
            c = it.permutations(board.empty, i)
            c = list(c)
            wins=-(2**700)
            loses=-wins

            for moves in c:  # moves is a series of steps.
                depth=0
                s = copy.deepcopy(sign)
                s = board.opp_sign(s)
                b = copy.deepcopy(board)
                for m in moves:
                    depth+=1
                    s = board.opp_sign(s)
                    b.ins(m, s)
                    if ((depth % 2 ==1) and self.is_win(b, s)): #The tree wins.
                        if (depth ==1): return m
                        print("I win!", m, moves)
                        key[moves[0]]=max([10-depth,key[moves[0]]])
                        break
                    elif ((depth % 2 ==0) and self.is_win(b, s)): #The opp wins.
                        print("Yow win!", m, moves)
                        if (depth == 2):
                            return m
                        key[moves[0]]=min([-10+depth,key[moves[0]]])
                        break

        print(key)

        li=list(key.items())
        steps=[]
        for i in li:
            t=(i[1],i[0])
            steps.append(t)
        steps.sort()
        steps.reverse()
        return steps[0][1]






    #*****************************************************************************************************#







