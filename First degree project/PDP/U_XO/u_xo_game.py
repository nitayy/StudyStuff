
import U_XO.u_xo_board as u
import U_XO.judge_uxo as jud
import tools
import players
import sqr
import game_stat


# ------------------------------------------ The class ----------------------------------------------
# ---------------------------------------------------------------------------------------------------
class U_xo():
    """The class for the board"""

    def __init__(self,p1,p2):
        self.bo=u.U_xo_board()
        self.p1 = p1
        self.p2 = p2
        self.last_x = None
        self.last_o = None
        self.ju=jud.JudgeUxo(self.bo)

        self.stat=game_stat.GameStat()

    # **********************************************************************#

    def show_one(self, num):
        """
        The function get a number between 1-9 and print the board.
        :param num: between 1-9.
        :return: 
        """
        if num in range(1,10):
            self.board[num].show()



    # *************************************************************************

    def ins(self, move, sign):
        """
        
        :param move: The move number.
        :param sign: The sign.
        :return: True or false.
        """
        if (move in self.ju.free_sqrs()  and (sign in ['x', 'o'])):
            return self.ju.get_move(move,sign)
        else:
            return False

    # ------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------

    def next_move(self,player):
        free = self.ju.free_sqrs()
        print(free)
        player.last_move = player.next(free)
        if player.last_move not in free:
            print("Problem with the square! Please put another one.")
            return False
        self.ju.get_move(player.last_move,player.sign)
        if player.sign=='x': self.last_x=player.last_move
        else: self.last_o=player.last_move
        return True
        # print("Last", self.last_x,self.last_o)
        # self.bo.show()
        # print("V_B:", self.bo.valid_boards)
        # print("Free: ",free)
        # print("next bo", self.ju.bo)
        # print("last", player.last_move)
        # print("winner", self.ju.winner)

        # if self.ju.bo not in self.bo.valid_boards and self.ju.bo != 0:
        #     exit(1)

    # --------------------------------------------------------------------------------------------------------
    def game(self):
        """
        This function is for playing u_xo between two players
        
        :param p1: The first player. 
        :param p2: The second player.
        :return: d - draw, x - x wins, o - o wins.
        """


        while not self.ju.game_finish():
            self.p1.last_move = self.next_move(self.p1)
            if not self.ju.finish:
                self.last_o=self.p2.last_move=self.next_move(self.p2)
                self.bo.show()
        self.stat.inc_wins(self.ju.winner)
        return self.ju.winner


    # --------------------------------------------------------------------------------------------------------

    def get_sqrs(self):
        """
        This function return a list of lists of the squares.
        Each sub-list contains 4 parameters:
        [s,col_b,l,last]
        
        s = The sign of the square: . - empty, x/o or D (when it's draw).
        col_b = The color of the square.
        l = A boolean parameter if the square is lock (available for play).
        last = if it was the lat move. (By the sign you can know if it was the last move of 'x' or 'o'
        
        :return: List of sub-lists.
        """

        sq=[]
        for b in range (1,10):
            free_board = True if b==self.ju.bo or self.ju.bo==0 else False
            col_b = sqr.color['active'] if free_board else sqr.color['block']
            if self.bo.main_b.board[b-1]=='x':
                col_b = sqr.color['win_x']
            elif self.bo.main_b.board[b-1] == 'o':
                col_b = sqr.color['win_o']
            i=0
            for s in self.bo.board[b].board:
                i+=1
                if s!='.':
                    last = tools.to_1n(b,i) == self.last_x or tools.to_1n(b,i) == self.last_o
                    d = 'x' if s=='x' else 'o'
                    l = False
                if s=='.':
                    d=None
                    last = False
                    l = free_board
                q=sqr.Sqr(s, col_b, True, last)
                sq.append(q)
        return sq

    # --------------------------------------------------------------------------------------------------------
    def get_next_bo(self):
        """
        0 - All the boards ar valid.
        A number between 1-9 - The next move should be at this board.
        :return: 
        """
        return self.ju.bo
    # --------------------------------------------------------------------------------------------------------
    def reset(self):
        """The function resets the board"""
        self.__init__(self.p1,self.p2)

    def clear_board(self):
        self.bo.__init__()
        self.ju.__init__(self.bo)




# l=random.sample(range(1,82),81)
# for i in range(80):
#     if (i%2==0):
#         c.ins3(l[i],'x')
#     else:
#         c.ins3(l[i],'o')
# c.main_b.show()
# c.show()
# t=[0,0,0]
# p1=players.rand_player('x')
# p2=players.hum_player('o')
# c = U_xo(p1,p2)
# for i in range(1):
#     c.clear_board()
#     c.game()
#     print(i,c.ju.winner)
#     print(len(c.get_sqrs()))
#     for (i,j) in zip(c.get_sqrs(),range(1,82)):
#         print(j, i.get_sqr_list())
#     c.bo.show()
# print(c.stat.get_wins(),c.stat.get_stat())