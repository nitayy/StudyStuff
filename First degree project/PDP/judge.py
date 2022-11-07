import tools


"""Class for a judge at the game"""


class Judge:
    def __init__(self,board):
        self.finish=False
        self.winner=None
        self.board=board
        self.win_sqrs=None

    def get_finish(self):
        return self.finish

    def get_winner(self):
        return self.winner

    def check_for_winner(self):
        if self.check_for_win(self.board,'x'):
            self.winner='x'
            self.finish=True
            return 'x'
        elif self.check_for_win(self.board,'o'):
            self.winner='o'
            self.finish=True
            return 'o'
        elif self.check_for_draw(self.board):
            self.winner='d'
            self.finish=True
            return 'd'


    # ----------------------------------------------------------------------
    # **********************************************************************#
    def check_for_win(self,b, sign):
        """
       The function gets a board, and checks if someone wins or its a draw.
       :param b: The board.
       :param sign: The sign we check for.
       :return: True or False
       """
        for i in range(1, b.get_s()+1):
            if (tools.all(b.get_col(i), sign)):
                return True
            if (tools.all(b.get_row(i), sign)):
                return True
        if (tools.all(b.get_diag1(), sign)):
            return True
        if (tools.all(b.get_diag2(), sign)):
            return True
        return False

        # **********************************************************************#

    def check_for_draw(self,b):
        """
        The function gets a board, and checks if  its a draw.
        The 'd' is for the u_xo game.
        :param b: The board.
        :return: True if draw or False else.
        """
        for i in range(1, b.get_s()):
            if (not tools.two_at_list(b.get_col(i), 'x', 'o') and ('d' not in b.get_col(i))):
                return False
            if (not tools.two_at_list(b.get_row(i), 'x', 'o') and ('d' not in b.get_row(i))):
                return False
        if (not tools.two_at_list(b.get_diag1(), 'x', 'o') and ('d' not in b.get_diag1())):
            return False
        if (not tools.two_at_list(b.get_diag2(), 'x', 'o') and ('d' not in b.get_diag2())):
            return False
        return True
        # **********************************************************************#
