import xo as b
import random
import tools
import human_player as hp
import random_c as rc


# ------------------------------- Some helpful functions -------------------------------------------------
def ck(n):
    return (n <= 9 and n >= 1)

# **********************************************************************#
def check_for_win(b, sign):
    """
   The function gets a board, and checks if someone wins or its a draw.
   :param b: The board.
   :param sign: The sign we check for.
   :return: True or False
   """
    for i in range(1, b.get_s()):
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

def check_for_draw(b):
    """
    The function gets a board, and checks if someone wins or its a draw.
    :param b: The board.
    :param sign: The sign we check for.
    :return: True or False
    """
    for i in range(1, b.get_s()):
        if (not tools.two_at_list(b.get_col(i), 'x', 'o')):
            return False
        if (not tools.two_at_list(b.get_row(i), 'x', 'o')):
            return False
    if (not tools.two_at_list(b.get_diag1(), 'x', 'o')):
        return False
    if (not tools.two_at_list(b.get_diag2(), 'x', 'o')):
        return False
    return True
    # **********************************************************************#


# ------------------------------------------ The class ----------------------------------------------
# ---------------------------------------------------------------------------------------------------
class U_xo:
    """The class for the board"""
    def __init__(self):
       self.main_b = b.board()  # The main board
       self.board = {}
       self.valid_boards=[1,2,3,4,5,6,7,8,9] #The boards are valid for play
       for i in range(1, 10):  # Initializing the boards
           self.board[i] = b.board()
       self.bo=0 # The next board, if 0 - any board.
       self.move=0 # The next move.
    # **********************************************************************#

    def show_one(self,num):
        """
        The function get a number between 1-9 and print the board.
        :param num: between 1-9.
        :return: 
        """
        if ck(num):
            self.board[num].show()

    # **********************************************************************#
    def show(self):
        """
        The function shows all the boards and NOT the main booard.
        :return: 
        """
        for i in range(1,10,3): # The boards
            for j in range(1,4): # The rows
                r1=self.board[i].get_row(j)
                r1.append('*')
                r2 = self.board[i+1].get_row(j)
                r2.append('*')
                r3 = self.board[i+2].get_row(j)
                r=[r1,r2,r3]
                for k in r:
                    for p in k:
                        print(p,end=' ')
                print('\n')
            for k0 in range(1,13):
                if(i != 7):
                   print('*',end=' ')
            print('\n')
    # *************************************************************************

    def ins(self,num_b,num_s,sign):
        """
        
        :param num_b: The number of the board.
        :param num_s: The number of the square
        :param sign: The sign.
        :return: True of false.
        """
        if (ck(num_b) and (sign=='x' or sign=='o')):
            return self.board[num_b].ins(num_s,sign)
        else:
            return False

    # --------------------------------------------------------------------------------------------------------
    def in_range(self):
        """
        The function checks if num and move between 1-9.
        :return: True or False
        """
        return (ck(self.num) and ck(self.move))
    # --------------------------------------------------------------------------------------------------------

    def is_win(self,sign):
        """
        The function inserts a symbol to the board and updates the the main board if needed.
        :param sign: the sign
        :return: If there is a winner for the whole game  - the sign, if draw - 'd', else - None
        """
        # Checks if the player wins:
        if (check_for_win(self.board[self.bo], sign)):
            self.valid_boards.remove(self.bo)
            self.main_b.ins(self.bo, sign)
            self.board[self.bo].flip_all('X' if sign == 'x' else 'O')
            if (check_for_win(self.main_b,sign)):
                return sign
        if (check_for_draw(self.main_b)):
            return 'd'
        else:
            return None



    # --------------------------------------------------------------------------------------------------------
    def with_dos_output_num(self):
        """The function outputs the game as numbers"""
        # Start:
        sign='x'
        i=1
        not_finish=True
        while(not_finish):
            print("The turn of: ",sign)
            if (self.bo == 0):  # We can choose a board.
                # d = input("Please enter two numbers: \n")
                print("You can choose any bord for playing....")
                self.bo=rc.get_sqr(self.valid_boards)
                self.move = rc.get_sqr(self.board[self.bo].empty)
                # Insert the sign
                self.board[self.bo].ins(self.move, sign)


                print("Self bo is:", self.bo)
                if(self.is_win(sign)):
                    pass

                # Checks if it's Draw
                self.show()
                sign = b.opp_sign(sign)


            else:
                print("Before - self bo is:", self.bo, "self move is:", self.move)
                #d = input("Please enter the next move: \n")
                #self.move = int(d)
                self.move = rc.get_sqr(self.board[self.bo].empty)

                # Insert the sign
                self.board[self.bo].ins(self.move, sign)
                self.is_win(sign)
                self.show()
                sign = b.opp_sign(sign)

            # #####################################
            # General - things are common for both:

            i+=1
            # For the next move:
            self.bo = self.move

            print("self bo is:", self.bo, "self move is:" ,self.move)
            print("_____________________________________________________________________________")
