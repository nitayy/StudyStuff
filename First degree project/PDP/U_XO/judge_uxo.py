import U_XO.u_xo_board
import judge
import tools

"""This is for judging the game and say if someone wins """


class JudgeUxo(judge.Judge):
    def __init__(self,b):
        judge.Judge.__init__(self,b)
        self.bo = 0

    def there_is_winner(self):
        for s in ['x','o']:
           if judge.Judge.check_for_win(self.b.main_b,s):
               return 's'
        return None

    def is_draw(self):
        return judge.Judge.check_for_draw(self.b.main_b)

    def free_sqrs(self):
        """
        Free = where can be the next move. i.e. - if self.bo != 0 - the the free squares are only at self.bo!!
        :return: The function returns a list with all the free squares at the board. 
        """
        f=[]
        if (self.bo == 0):
            for b in self.board.valid_boards:
                temp=self.board.board[b]
                for s in temp.empty:
                    f.append(tools.to_1n(b,s))
        else:
            for s in self.board.board[self.bo].empty:
                f.append(tools.to_1n(self.bo, s))

        return f

    def game_finish(self):
        t = self.board.main_b
        self.finish = self.check_for_draw(t) or self.check_for_win(t,'x') or self.check_for_win(t,'o')
        if self.finish:
            if self.check_for_win(t,'x'): self.winner='x'
            elif self.check_for_win(t,'o'): self.winner='o'
            else: self.winner='d'
        return self.finish

    def get_move(self,move,sign):
        """
        The function get a move at range 1-81 and insert it to the right board.
        :param move: The move.
        :return: T/F if the insertion seceded 
        """
        if move in self.free_sqrs():
            b,s=tools.to_2n(move)
            if self.board.board[b].ins(s,sign):
                if self.check_for_win(self.board.board[b],sign):
                    self.board.main_b.ins(b,sign)
                    self.board.board[b].flip_all('X' if sign=='x' else 'O')
                    self.board.valid_boards.remove(b)
                    self.game_finish()
                    return True
                elif self.check_for_draw(self.board.board[b]):
                    self.board.main_b.ins(b,'d')
                    self.board.board[b].flip_all('D')
                    self.board.valid_boards.remove(b)
                    self.game_finish()
                    return True
            else:
                return True
            self.bo = s if s in self.board.valid_boards else 0
        else:
            return False
