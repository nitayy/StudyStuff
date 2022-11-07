""" 
File for players for the u_xo and q_xo games.
"""

import tools
#import tree_u_xo
import copy
import U_XO.tree_u_xo as tree
import Q_XO.tree_q_xo as qtree
import conn
import random

class Player:
    """Class for a generic player"""

    def __init__(self,sign):
        self.last_move=None
        self.sign=sign

    def get_last(self):
        return self.last_move

    def next(self,uboard):
        """
        A function for getting the next move from the player.
        :param board: The board.
        :return: A square for the next move.
        """
        print("You need to overwrrtien this function!!")


# -------------------------------------------
#               Random Player
# -------------------------------------------
class rand_player(Player):
    def __init__(self,sign):
        random.seed()
        Player.__init__(self,sign)

    def next(self,l):
        self.last_move = tools.a_from_b(l)
        return self.last_move


# -------------------------------------------
#               Human Player
# -------------------------------------------
class hum_player(Player):
    def __init__(self,sign):
        Player.__init__(self,sign)

    def next(self, free_sqrs):
        n=None
        while n not in free_sqrs:
            if n != None:
                print("There was a problem with the square....")
            print("Trun of: ",self.sign)
            n=input("Please enter a square from the list:")
            n=int(n)
        self.last_move = n
        return n

# -------------------------------------------
#               Con Player
# -------------------------------------------
class ConPlayer(Player):
    def __init__(self, sign,size):
        Player.__init__(self, sign)
        self.size=size
        self.con = conn.Con(size)

    def next(self, free_sqrs):
        while not self.con.active:
            pass
        return self.con.get_n()


# Players of con:
class ConUxo(ConPlayer):
    def __init__(self, sign):
        ConPlayer.__init__(self, sign, 81)

class ConQxo(ConPlayer):
    def __init__(self, sign):
        ConPlayer.__init__(self, sign, 64)

# -------------------------------------------
#               Tree Player
# -------------------------------------------
class tree_player(Player):
    def __init__(self,sign='x'):
        Player.__init__(self,sign)
        self.depth = 0
        self.stop=False # Cause tree never shold lose!


    def inc_dep(self):
        self.depth += 1

    def next(self,board):
        return tree.find_best_move(board,self.depth,True,self.sign)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# -------------------------------------------
#               Q_xo Tree Player
# -------------------------------------------
class Q_xo_tree_player(tree_player):
    def __init__(self,sign='x'):
        tree_player.__init__(self,sign)

    def next(self,board):
        s=self.sign
        return qtree.tree.find_best_move(self,board,self.depth,True,s)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
