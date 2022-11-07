import Q_XO.q_xo_board as b
import Q_XO.judge_q_xo as j
import Q_XO.q_pdp as pdp
import players
import game_stat
import sqr


class Game():
    def __init__(self,p1):
        self.p1=p1
        self.bo=b.Q_xo_board()
        self.ju=j.Judge_q_xo(self.bo)
        self.pdp=pdp.QPDP('o')
        self.stat = game_stat.GameStat()

    def reset(self):
        self.__init__(self.p1,self.p2)
    # --------------------------------------------------------------------------------------

    def game_hum_with_pdp(self):
        while not self.ju.game_finish():
            # print(self.ju.free_sqrs())
            t=self.p1.next(self.ju.free_sqrs())
            self.pdp.update_in(t,'x')
            self.pdp.ins_move(t,'x')
            print("x put at: ", t)
            self.bo.ins(t,self.p1.sign,True)
            if not self.ju.game_finish():
                self.pdp.hur1()
                t = self.pdp.get_move()
                print("o (PDP) put at: ", t)
                self.pdp.ins_move(t, 'o')
                self.bo.ins(t, 'o', True)
            self.pdp.show()
            self.bo.show()
        self.stat.inc_wins(self.ju.winner)
        print("\n\nThe winner is ", self.ju.winner if self.ju.winner in ['x','o'] else "\n\nDraw!!")
        return self.ju.winner
    # --------------------------------------------------------------------------------------

    def game_comp_with_pdp(self,pr=False):
        x = []
        o = []
        while not self.ju.game_finish():
            # print(self.ju.free_sqrs())
            t = self.p1.next(self.ju.free_sqrs())
            x.append(t)
            self.pdp.ins_move(t, 'x')
            # print("x put at: ", t)
            self.bo.ins(t, self.p1.sign, True)
            if not self.ju.game_finish():
                self.pdp.hur1()
                t=self.pdp.get_move()
                o.append(t)
                self.pdp.ins_move(t, 'o')
                # print("o put at: ", t)
                self.bo.ins(t, 'o', True)
        self.stat.inc_wins(self.ju.winner)
        if pr:
            print("\n\nThe winner is ", self.ju.winner if self.ju.winner in ['x', 'o'] else "\n\nDraw!!")
        return self.ju.winner
    # -----------------------------------------------------------------------------------------------
    def get_sqrs(self):
        s=[]
        for i in self.bo.board:
            d = None if i=='.' else i
            b = False if d==None else True
            c = None # Relevant for u_xo only.
            l = True if i==self.p1.last_move or i==self.p2.last_move else False
            s.append(sqr.Sqr(d,c,b,l))
        return s
    # -----------------------------------------------------------------------------------------------
    def reset(self):
        self.__init__(self.p1,self.p2)

    def clear_board(self):
        self.bo.__init__()
        self.ju.__init__(self.bo)
        self.pdp.__init__('o')


# #p1=players.Q_xo_tree_player('x')
# p1=players.rand_player('x')
# # p2=players.Q_xo_tree_player('o')
# p2=players.rand_player('o')
# g=Game(p1,p2)
#
# for i in range(10000):
#     g.game_with_pdp()
#     g.clear_board()
#     print(i)
# print(g.stat.get_wins(), g.stat.get_stat())