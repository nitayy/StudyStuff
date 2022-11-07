import human_player
import pdp
import random_c as rc
import xo
import tree2


class Game():
    def __init__(self,pdp_sign='o'):
        self.b = xo.board()  # for The players.
        self.pdp_sign=pdp_sign
        self.p = pdp.Pdp(self.pdp_sign)

    def who_win(self,sqr,pr=True):
        """return if someone wins, sqr - is the last square entered. sign - is the sign.
        The function return 0 [false] if no on wins,
        1 - if 'x' wins,
        2 - if 'o' wins,
        3 - if draw."""
        # checks if draw (no one wins):
        sign = self.b.board[sqr-1]
        r=self.b.get_row(self.b.get_r(sqr))
        c=self.b.get_col(self.b.get_c(sqr))
        data = [r, c, self.b.get_diag1(), self.b.get_diag2()]
        for k in data:
            if (k.count(sign) == self.b.s):
                if pr:
                    print("Player -" + sign + "- wins!!")
                if sign=='x':
                    return 1
                if sign=='o':
                    return 2
        if (self.b.is_full()):
            if pr:
                print("Draw!!")
            return 3
        return 0

    # *****************************************************************************************************#
    def game_hum_with_pdp(self,s1='x',s2='o'):
        """
        This is function for the game against the pdp.
        
        """
        p=pdp.Pdp('o')
        p1=human_player.human()
        w=0
        while (w==0):
            print("__________________________________")
            self.b.show()
            p.show_pdp1()
            sq = p1.get_sqr(self.b.empty)
            self.b.ins(sq,s1)
            p.set_input(sq, s1)
            w=self.who_win(sq)
            if (w != 0):
                self.b.show()
                return w
            print("__________________________________")
            self.b.show()
            p.show_pdp1()
            p.hur1()
            sq=p.get_move()
            self.b.ins(sq,s2)
            p.set_input(sq, s2)
            w = self.who_win(sq)
            if (w != 0):
                self.b.show()
                return w

    # *****************************************************************************************************#

    def game_comp_with_pdp(self, s1='x', tree = False):

        self.clear()
        if not tree:
            p1 = rc.randcomp()
        else:
            p1 = tree2.tree()
        w = 0
        while (w == 0):
            print("_____________p1_____________________")
            if not tree:
                sq=p1.get_sqr(self.b.empty)
            else:
                sq = p1.find_best_move(self.b, 0, True, 'x')
            # sq=p1.get_sqr(self.b.empty)
            self.b.ins(sq, s1)
            self.p.set_input(sq, s1)
            # self.b.show()
            print("PDP After P1 plays:")
            # self.p.show_pdp1()
            w = self.who_win(sq)
            # print("w is: ",w)
            if (w != 0):
                self.b.show()
                self.clear()
                return w
            print("_____________________________________")
            print("________________p2__________________")
            # sq=p2.minimax(self.b,'o')
            # sq=p2.find_best_move(self.b,1,True,'o')
            self.p.hur1()
            sq=self.p.get_move()
            self.b.ins(sq, 'o')
            self.p.set_input(sq, 'o')
            print("PDP After P2 plays:")
            # self.b.show()
            # self.p.show_pdp1()
            w = self.who_win(sq)
            # print("w is: ", w)
            if (w != 0):
                self.clear()
                return w
            print("_____________________________________")

    # *****************************************************************************************************#

    def game_perm_with_pdp(self,per, s1='x'):
        """
        The function is for playing against a "permutation".
        :param per: The permutation of 5 elements of char. each char is between 1-9.
        :param s1: The sign of the first player.
        :return: 
        """""
        self.clear()
        self.p.pr=False
        idx=0
        w=0
        while (w == 0):
            sq=int(per[idx])
            self.b.ins(sq, s1)
            self.p.set_input(sq, s1)
            # self.b.show()
            w = self.who_win(sq,False)
            # print("w is: ",w)
            if (w != 0):
                print('-'*10)
                self.b.show()
                self.clear()
                return w
            self.p.hur1()
            sq = self.p.get_move()
            self.b.ins(sq, 'o')
            self.p.set_input(sq, 'o')
            # print("PDP After P2 plays:")
            # self.b.show()
            # self.p.show_pdp1()
            w = self.who_win(sq,False)
            # print("w is: ", w)
            if (w != 0):
                self.clear()
                return w
            idx+=1
            if int(per[idx]) not in self.b.empty:
                return -1  # Irrelevant permutation.

    # *****************************************************************************************************#
    def clear(self):
        """
        Clear the board.
        :return: None
        """
        self.b.clear_board()
        self.p.__init__(self.pdp_sign)

# g=Game()
# w=[0,0,0]
# for i in range(100000):
#     g.clear()
#     t=g.game_comp_with_pdp()
#     w[t-1]+=1
# print(w)

def t1():
    w = [0, 0, 0]
    g = Game()
    for i in range(100000):
        k = g.game_comp_with_pdp()
        w[k - 1] += 1
        g.clear()
    print(w)

# g = Game()
# g.game_hum_with_pdp()
# c=input("Press enter to exit!")