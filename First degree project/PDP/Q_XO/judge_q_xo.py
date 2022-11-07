import judge
import Q_XO.ranges as r
import tools


class Judge_q_xo(judge.Judge):
    def __init__(self, board):
        judge.Judge.__init__(self,board)

    def check_for_win(self, sign):
        for i in r.all_lines:
            temp = [self.board.board[j-1] for j in i]
            if tools.all(temp,sign):
                self.winner=sign
                self.finish=True
                self.win_sqrs=i
                return True
        return False

    def check_for_draw(self):
        for i in r.all_lines:
            temp=[self.board.board[j-1] for j in i]
            if not tools.two_at_list(temp,'x','o'):
                return False
        self.finish = True
        self.winner = 'd'
        return True

    def free_sqrs(self):
        free=[]
        for i in range(len(self.board.board)):
            if self.board.board[i] == '.':
                free.append(i+1)
        return free

    def game_finish(self):
        """
        The function Return True if the game was finished
        :return: T/F
        """
        if self.finish:
            return True

        t = self.check_for_win('x') or \
        self.check_for_win('o') or \
        self.check_for_draw()
        if self.winner=='x':
            for i in self.win_sqrs:
                self.board.board[i-1]='X'
        else:
            if self.winner == 'o':
                for i in self.win_sqrs:
                    self.board.board[i - 1] = 'O'
        return t