"""Representing  XO board
    Written by: Nitay Yehezkely"""

import os
import copy


def sub(l): return [x-1 for x in l]


# For hur functions.
dic = {'r1': [1, 2, 3], 'r2': [4, 5, 6], 'r3': [7, 8, 9], 'd1':[1, 5, 9], 'd2': [3, 5, 7], 'c1': [1, 4, 7],
       'c2': [2, 5, 8], 'c3': [3, 6, 9]}
wins = list(dic.values())

n_dic = {x:sub(dic[x]) for x in dic}
n_wins = list(n_dic.values())

def cls():
    os.system('cls' if os.name=='nt' else 'clear')




##############################################################################################################
class board:
    "For representing borad"
    BEGIN = 0  # The begin cell.



    # *****************************************************************************************************#
    def __init__(self, size=3):
        """Initilize a board"""
        self.s=size;  # The size of the board.
        self.board = ['.']*(size**2);
        self.empty=[i+1 for i in range(size**2)]; # For a list of the empty squares at the board.
        board.s = size;
        # for i in range(size ** 2):
        #    self.board.append('.')
        #    self.empty.append(i + 1) #After this all the board is "empty".

    # *****************************************************************************************************#
    def show(self):
        """Printing the board"""
        temp = self.s
        for i in range(temp):
            for j in range(temp * i, (temp * i) + temp):
                print(self.board[j], end=' ')
            print('\n')

    # *****************************************************************************************************#
    def show_sign(self,sign):
        """Printing the board with sign 'sign' instead of '.' """
        temp = self.s
        for i in range(temp):
            for j in range(temp * i, (temp * i) + temp):
                print(sign if self.board[j]=='.' else self.board[i], end=' ')
            print('\n')

    # *****************************************************************************************************#
    def clear_board(self):
        """
        Clears the board for a new game....
        :return:
        """
        self.empty.clear()
        self.board.clear()
        for i in range(self.s ** 2):
            self.board.append('.')
            self.empty.append(i + 1)  # After this all the board is "empty".

    #*****************************************************************************************************#
    def ins(self, sqr, symbol):
        """Inserting a symbol to the board"""
        if (self.board[sqr - 1] != '.'):
            print("The square is not empty! ", sqr)
            return False
        self.board[sqr - 1] = symbol
        self.empty.remove(sqr)
        return True

    #*****************************************************************************************************#
    def ins_no_output(self, sqr, symbol): #same as is but with no output
        """Inserting a symbol to the board"""
        if (self.board[sqr - 1] != '.'):
            return False
        self.board[sqr - 1] = symbol
        self.empty.remove(sqr)
        return True

    def is_full(self):
        return (self.empty == [])

    #*****************************************************************************************************#
    def get_row(self, num):
        r = []
        for i in range((num - 1) * self.s, (num - 1) * self.s + self.s):
            r.append(self.board[i])
        return r

    #*****************************************************************************************************#
    def get_col(self, num):
        c = []
        for i in range(self.s):
            c.append(self.board[(num - 1) + i * self.s])
        return c

    #*****************************************************************************************************#
    def get_diag1(self):  # for this "\" diagonal
        d = [];
        cell = self.BEGIN
        for i in range(self.s):
            d.append(self.board[cell])
            cell += self.s + 1
        return d

    #*****************************************************************************************************#
    def get_diag2(self):  # for this "/" diagonal
        d = [];
        cell = self.s - 1
        for i in range(self.s):
            d.append(self.board[cell])
            cell += self.s - 1
        return d

    #*****************************************************************************************************#
    # The functions below are for get a row and column of a specific cell:
    def get_r(self, sqr):
        return ((sqr-1) // self.s) + 1

    #*****************************************************************************************************#
    def get_c(self,sqr):
        --sqr
        return ((sqr-1) % self.s) + 1

    #*****************************************************************************************************#
    def get_rc(self, sqr): #Returns both!
        rc=[]
        sqr-=1
        rc.append((sqr // self.s) + 1)
        rc.append((sqr % self.s) + 1)
        return rc

    # *****************************************************************************************************#
    def get_board(self):
        return self.board

    # *****************************************************************************************************#
    def opp_sign(self,s):
        """
        The function gets sign and return the opposite sign.
        :param s: The sign.
        :return: x=>o , o=>x - Else return '.'
        """
        if (s=='x'): return 'o'
        elif (s=='o'): return 'x'
        else: return '.'

    # *****************************************************************************************************#
    def flip(self, s):
        """
        The function flips all the non x-o to sign s.
        :param s: The sign.
        :return: The flliped board.
        """
        for i in range(len(self.board)):
            self.board[i] = self.board[i] if ((self.board[i] == 'x') or (self.board[i]=='o')) else s

    # *****************************************************************************************************#
    def flip_all(self,sign):
        """
        Flips all the board to sign 'sign'
        :param sign: 
        :return: 
        """
        for i in range(len(self.board)):
            self.board[i]=sign
    #*****************************************************************************************************#
    #*****************************************************************************************************#
    def get_s(self):
        return self.s
##############################################################################################################
def opp_sign(s):
    """
    The function gets sign and return the opposite sign.
    :param s: The sign.
    :return: x=>o , o=>x - Else return '.'
    """
    if (s == 'x'):
        return 'o'
    elif (s == 'o'):
        return 'x'
    else:
        return '.'

#Tests:
def test1():
    b1 = board(9)
    for i in range(1, b1.get_s() ** 2 + 1):
        b1.ins(i, i)
    b1.show()
    print("-----------------")
    print(b1.get_rc(3)[1])
    print(b1.get_rc(7))
    print("-----------------")
    print(b1.get_r(3))
    print(b1.get_c(3))
    print("-----------------")
    print(b1.get_r(7))
    print(b1.get_c(7))
    print("-----------------")
    print(b1.get_r(8))
    print(b1.get_c(8))
    print(b1.get_col(3))

#test1()
