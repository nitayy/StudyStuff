import tools

def s():
    return 4
def s2():
    return s()**3

class Q_xo_board:
    """Class for Qubic xo"""
    def __init__(self):
        self.board=['.']*s2()
        self.empty=[x for x in range(1,65)]
    # --------------------------------
    def ins(self,num,sign,pr=False):
        """
        Insert a symbol into the board.
        :param num: The square number.
        :param sign: The symbol
        :return: True if the square was enter - False otherwise.  
        """
        if ((num < 1 or num > 64)):
            if pr:
                print("Sqaure ot of range!")
            return False
        elif (sign != 'x' and sign != 'o' ):
            if pr:
                print("Sign is not x/o...")
            return False
        elif (self.board[num-1] != '.'):
            if pr:
                print("Squre is not empty!")
            return False

        self.board[num-1]=sign
        self.empty.remove(num)
        return True
    # --------------------------------------------------------------------------------------------


    def print_line(self):
        """
        An help function for printing line of *s for q_xo with SPACE between them.
        :param sp: If to print new line after the *s line.
        :return: -
        """
        for i in range(9):
            print('*',end=' ')
        print('\n')
    # -------------------------------------------------------------------------------------------

    def show(self):

        def q(n):
            """
            For numbers or the board members.
            :param n: The square number.
            :return: n or board[n]
            """
            return self.board[n]

        l1=0; l2=16
        for i in range(2):
            l1=32*i; l2=l1+16
            for k in range(4): # Each loop is a row.
                for j1 in range(4):
                    print(q(l1 + j1), end=' ')
                print('*', end=' ')
                for j1 in range(4):
                    print(q(l2 + j1), end=' ')
                print('\n')
                l1=l1+4; l2=l2+4
            if (i==0):
                for i in range(9):
                    print('*',end =' ')
                print('\n')
