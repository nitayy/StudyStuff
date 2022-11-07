class BoardDetails:
    def __init__(self,game):
        self.game=game

    def get_free_sqrs(self):
        return self.game.free_sqrs()

    def get_next_board(self):
        return self.game.get_next_bo()