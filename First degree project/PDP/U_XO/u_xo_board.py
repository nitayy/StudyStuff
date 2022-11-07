import xo as b
import tools



class U_xo_board:
    """Class for the u_xo board"""
    def __init__(self):
        self.main_b = b.board()  # The main board
        self.board = {}
        self.valid_boards = list(range(1, 10))  # The boards are valid for play
        for i in range(1, 10):  # Initializing the boards
            self.board[i] = b.board()

    def get_main(self):
        return self.main_b

        # **********************************************************************#
    def show(self):
        """
        The function shows all the boards and NOT the main booard.
        :return: 
        """
        for i in range(1, 10, 3):  # The boards
            for j in range(1, 4):  # The rows
                r1 = self.board[i].get_row(j)
                r1.append('*')
                r2 = self.board[i + 1].get_row(j)
                r2.append('*')
                r3 = self.board[i + 2].get_row(j)
                r = [r1, r2, r3]
                for k in r:
                    for p in k:
                        print(p, end=' ')
                print('\n')
            for k0 in range(1, 13):
                if (i != 7):
                    print('*', end=' ')
            print('\n')