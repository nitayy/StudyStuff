import random
import conn
black = (0,0,0)
light_gray = (200,200,200)
gray = (100,100,100)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

class RandomGame(object):
    def __init__(self,lim, cn, threadname, queue):
        self.lim = lim
        self.threadname = threadname
        self.queue = queue
        self.cn = cn
        self.signs = [None]*81
        self.boards = []
        for i in range(1,10):
            self.boards.append(list(range((i-1)*9+1,(i*9)+1)))

    def set_o_next_move(self,x_last_move):
        # find xo sub board
        next_o_move_board = divmod(x_last_move, 9)[1]
        _my_from = self.boards[next_o_move_board-1][0]
        _my_to = self.boards[next_o_move_board-1][8]

        my_tmp_list = [i for i in range(_my_from, _my_to) if self.signs[i-1] == None]

        if len(my_tmp_list)>0:
            random.shuffle(my_tmp_list)
            o_move = my_tmp_list[0]
            # send GUI the board number in which it can make a move
            next_x_move_board = divmod(o_move, 9)[1]
            # print ('next_x_move_board=',next_x_move_board)

            self.signs[int(o_move-1)] = "o"

            locked_cells = [i for i in range(1,82)]
            _my_from = self.boards[next_x_move_board - 1][0]
            _my_to = self.boards[next_x_move_board - 1][8]
            for i in range(_my_from, _my_to + 1):
                locked_cells.remove(i)

            _my_from = self.boards[next_x_move_board - 1][0]
            _my_to = self.boards[next_x_move_board - 1][8]

        else:
            print('no room for a move in this sub-board')
            o_move = -1
            next_x_move_board = -1
            locked_cells = []

        #r_items = o_move, next_x_move_board, self.signs
        r_items = o_move, next_x_move_board, locked_cells
        return r_items

    def get_x_move(self):
        # get a move from the Gui
        items = self.cn.get_n()
        x_move = items[0]
        self.signs[int(x_move - 1)] = "x"
        x_move_board = divmod(x_move, 9)[1] + 1
        return x_move

    def winning_boards(self):
        board = [None]*9
        for i in range(1,10):
            for j in range(1,10):
                index = (i-1)*9 + j
                # board[index-1] = s

        # self.signs

from multiprocessing import Queue
def run_randomgame(threadname,queue):
    cn = conn.Con(81, threadname, queue)
    d = RandomGame(81,cn, threadname, queue)
    count = 0
    while(True):
        if True: # cn.get_n()==-1:
            x_move = d.get_x_move()
            if not x_move == -1:
                o_move, next_x_move_board, items = d.set_o_next_move(x_move)
                cn.set_n([o_move, next_x_move_board, items])
        count = count+1
        if(count > 100000000):
            print ('count = ', count, ' exiting...')
            exit(0)
