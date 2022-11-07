import pygame
import sys
import copy
import random
import time


black = (0,0,0)
light_gray = (200,200,200)
gray = (100,100,100)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
light_gray_green = (230,255,230)
gray_green = (130,155,130)

#******************** Non Graphics Classes ***********************************************************************8

class Cell(object):
    """basic class for building boards"""

    def __init__(self):
        """initialize"""

        self.name = "Cell"
        self.color = gray
        self.edge_color = red
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.rect = [self.x, self.y, self.width, self.height]
        self.label = ""

class tttBoard(Cell):
    """standard tic-tac-toe board"""

    def __init__(self, x0, y0, c):
        """initialize"""

        self.name = 'ttt'
        self.x = x0
        self.y = y0
        self.width = 3 * c.width
        self.height = 3 * c.height
        self.rect = [self.x, self.y, self.width, self.height]
        self.color = gray

        self.cells = []
        for i in [0, 1, 2]:
            self.cells.append(copy.deepcopy(c))
            self.cells[i] = []
            for j in [0, 1, 2]:
                self.cells[i].append(copy.deepcopy(c))
                # locations of cells
                _x = x0 + i * c.width
                _y = y0 + j * c.height
                self.cells[i][j].x = _x
                self.cells[i][j].y = _y
                self.cells[i][j].rect = [_x, _y, c.width, c.height]
                if (i + j) % 2:
                    self.cells[i][j].color = gray
                else:
                    self.cells[i][j].color = light_gray

class utttBoard(tttBoard):
    """ULtimate tic-tac-toe board"""

    def __init__(self, x0, y0, ttt):
        """initialize"""

        self.name = 'uttt'
        self.x = x0
        self.y = y0
        self.width = 3 * ttt.width
        self.height = 3 * ttt.height
        self.rect = [self.x, self.y, self.width, self.height]
        self.color = None

        self.cells = []
        for i in [0, 1, 2]:
            self.cells.append(copy.deepcopy(ttt))
            self.cells[i] = []
            for j in [0, 1, 2]:
                self.cells[i].append(copy.deepcopy(ttt))
                # locations of cells
                _x = x0 + i * ttt.width
                _y = y0 + j * ttt.height
                self.cells[i][j].x = _x
                self.cells[i][j].y = _y
                self.cells[i][j].rect = [_x, _y, ttt.width, ttt.height]

    def get_cell_indeces(self, x, y):
        """extract indices by location"""

        _cell_width = self.width/9
        _cell_height = self.height/9

        for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            _tmp_x = i * _cell_width
            if x < _tmp_x:
                _ind_x = i-1
                break

        for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            _tmp_y = i * _cell_height
            if y < _tmp_y:
                _ind_y = i-1
                break

        # I,i = divmod(_ind_x,3)
        # J,j = divmod(_ind_y,3)

        return (_ind_x,_ind_y)
#******************** End Non Graphics Classes ***********************************************************************8

#******************** Graphics Classes *************************************************************************
#===============================================================================================================
#===============================================================================================================
#===============================================================================================================
#===============================================================================================================
class DrawUttBoard(object):
    """Draw Ulitmate tic-tac-toe board
    """
    def __init__(self, cn, threadname, queue):
        self.cell_width = 50
        self.screen_width = self.cell_width * 9
        self.screen_height = self.cell_width * 9
        self.args = (self.screen_width, self.screen_height)
        self.font = None
        # communication & queue:
        self.cn = cn
        self.threadname = threadname
        self.queue = queue
        # lists:
        self.X_LABELS = [""] * 81
        self.O_LABELS = [""] * 81
        self.UPPER_LEFT_CORNERS = [(0, 0), (3, 0), (6, 0), (0, 3), (3, 3), (6, 3), (0, 6), (3, 6), (6, 6)]
        self.X_LAST_LABEL = [""] * 81
        self.O_LAST_LABEL = [""] * 81
        self.TTT = [""] * 9
        self.ALOWED_CELLS = [True] * 81
        self.MOUSE_CELLS = [False]*81
        self.START = True
        self.LOCKED_CELLS = []

    def display_screen(self):
        screen = pygame.display.set_mode(self.args)
        myfont = pygame.font.Font('freesansbold.ttf', 24)
        return [screen,myfont]

    def get_occupied_cells(self,list, val):
        """always returns a list containing the indices of val in list
        """
        retval = []
        last = 0
        while val in list[last:]:
                i = list[last:].index(val)
                retval.append(last + i)
                last += i + 1
        return retval

    # drawing tools
    def draw_board(self, board, screen, c):
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                _x = board.cells[i][j].x
                _y = board.cells[i][j].y
                t = tttBoard(_x, _y, c)
                self.draw_ttt_board(t, screen,c)


    def draw_ttt_board(self, board, screen,c):
        x0 = board.x
        y0 = board.y
        color = board.color
        # print(board.x,board.y,board.width)

        tmp_board = utttBoard(0, 0, board)
        for i in [0,1,2]:
            for j in [0,1,2]:
                pygame.draw.rect(screen,  board.cells[i][j].color, board.cells[i][j].rect)
                pygame.draw.rect(screen, white, board.cells[i][j].rect,1)

        next_move_corner_list = self.get_occupied_cells(self.TTT, "x")

        _sign = "x"
        self.draw_move(x0, y0, board, tmp_board,screen,_sign)

        _sign = "o"
        self.draw_move(x0, y0, board, tmp_board, screen,_sign)

        pygame.draw.rect(screen, black , board.rect, 5)


        if len(next_move_corner_list) == 0:
            self.my_mouse(-1, board, screen)
        for next_move_corner in next_move_corner_list:
            _rect = [ divmod(next_move_corner, 3)[0] * board.width,divmod(next_move_corner, 3)[1]*board.height,
                      board.width, board.height]
            pygame.draw.rect(screen, green, _rect, 5)
            self.my_mouse(next_move_corner,board,screen)

    def draw_move(self,x0,y0,board,tmp_board,screen,sign):
        if sign == 'x':
            index = self.get_occupied_cells(self.X_LABELS, "x")
        if sign == 'o':
            index = self.get_occupied_cells(self.O_LABELS, "o")
        for ind in index:
            tmp_list = self.get_calc_nx_ny(ind)
            nx_calc, ny_calc = (tmp_list[0],tmp_list[1])
            if (divmod(nx_calc, 3)[0]) * board.width == x0 and (divmod(ny_calc, 3)[0]) * board.height == y0:
                _color = black
                self.player_move(tmp_board, screen, _color, sign, nx_calc, ny_calc)
                if sign == "x":
                    last_index = self.get_occupied_cells(self.X_LAST_LABEL, sign)
                if sign == 'o':
                    last_index = self.get_occupied_cells(self.O_LAST_LABEL, sign)
                for last_ind in last_index:
                    tmp_last_list = self.get_calc_nx_ny(last_ind)
                    last_nx = tmp_last_list[0]
                    last_ny = tmp_last_list[1]
                    if sign == "x":
                        _color = blue
                    if sign == 'o':
                        _color = red
                    if nx_calc == last_nx and ny_calc == last_ny:
                        self.player_move(tmp_board, screen, _color, sign, last_nx, last_ny)

    def my_mouse(self,next_move_corner,board,screen):
        index_mouse = self.get_occupied_cells(self.MOUSE_CELLS, True)
        if len(index_mouse) > 0:
            if index_mouse[0] < 81 and index_mouse[0] > -1:
                ind_tmp = index_mouse[0]
                nx_mouse, ny_mouse, I_draw, J_draw, i_draw, j_draw = self.get_calc_nx_ny(ind_tmp)
                # if self.ALOWED_CELLS[nx_mouse + ny_mouse * 9] == False:
                #     return
                n_test = nx_mouse + ny_mouse * 9
                if n_test in self.LOCKED_CELLS:
                    return
                _rect =  [nx_mouse * board.width/3, ny_mouse * board.height/3, board.width/3, board.height/3]
                if next_move_corner == -1:
                    pygame.draw.rect(screen, white, _rect)
                if I_draw == divmod(next_move_corner, 3)[0] and \
                                J_draw == divmod(next_move_corner, 3)[1]:
                    pygame.draw.rect(screen, white, _rect)


    def text_objects(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ NY $$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def nytai_index(self,nx,ny):
        ny_board = (divmod(ny,3)[0])*3 + divmod(nx,3)[0]+1
        ny_cell = (divmod(ny,3)[1])*3 + divmod(nx,3)[1]+1
        ny_index = (ny_board-1)*9 + ny_cell
        self.nx_ny_from_nytai(ny_index)
        return ny_index

    def nx_ny_from_nytai(self,ny_index):
        ny_board = divmod(ny_index-1,9)[0]+1
        corner = self.UPPER_LEFT_CORNERS[ny_board - 1]
        ny_cell = divmod(ny_index-1,9)[1]
        nx = corner[0]+divmod(ny_cell,3)[1]
        ny = corner[1] + divmod(ny_cell, 3)[0]
        return (nx,ny)
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ NY $$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # def player_move_click_generator(self,uttt,screen,cn,threadname,queue):
    def player_move_click_generator(self, uttt, screen):
        mouse = pygame.mouse.get_pos()
        x_mouse = mouse[0]
        y_mouse = mouse[1]
        nx_mouse, ny_mouse = uttt.get_cell_indeces(x_mouse, y_mouse)
        self.MOUSE_CELLS = [False]*81
        index_mouse = ny_mouse * 9 + nx_mouse
        self.MOUSE_CELLS[index_mouse] = True

        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            x = mouse[0]
            y = mouse[1]
            nx,ny = uttt.get_cell_indeces(x, y)

            n_test = nx + ny * 9
            if n_test in self.LOCKED_CELLS:
                nitay_index = self.nytai_index(nx,ny)
                print ("locked, Nitay index = ",nitay_index)
                return
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ NY $$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            n = self.nytai_index(nx, ny)
            # print ('=================================')
            # print ('clicked on cell no', n)
            set_list = [n]
            self.cn.set_n(set_list)
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ NY $$$$$$$$$$$$$$$$$$$$$$$$$$$$$

            # if START:
            if self.START:
                self.X_LABELS[ny * 9 + nx] = "x"
                for a in range (0,81):
                    self.X_LAST_LABEL[a] = ""

                self.X_LAST_LABEL[ny * 9 + nx] = "x"

                # mark opponent (change $$$ this with opponent move from Ny)
                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ NY $$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                tmp_list = self.get_calc_nx_ny(ny*9+nx)
                I = tmp_list[2]; J = tmp_list[3]; i = tmp_list[4]; j = tmp_list[5]
                I_o = i; J_o = j

                nx_o = I_o * 3 + 0
                ny_o = J_o * 3 + 0
                n = divmod(ny_o, 3)[0] * 3 + divmod(nx_o, 3)[0]  # upper left corner
                nx_o_corner, ny_o_corner = self.UPPER_LEFT_CORNERS[n]

                lb_items_list = self.members_of_large_box((nx_o_corner, ny_o_corner))
                random.shuffle(lb_items_list)
                nx_o, ny_o = lb_items_list[0]

                # assign here the nx_o,ny_o obtained with Ny index
                items = self.cn.get_n()
                ny_index = items[0]
                if ny_index == -1:
                    return
                nx_o,ny_o = self.nx_ny_from_nytai(ny_index)
                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ NY $$$$$$$$$$$$$$$$$$$$$$$$$$$$$

                self.O_LABELS[nx_o + ny_o * 9] = "o"

                for a in range (0,81):
                    self.O_LAST_LABEL[a] = ""

                self.O_LAST_LABEL[nx_o + ny_o * 9] = "o"

                for a in range(0,9):
                    self.TTT[a] = ""

                # mark my block
                tmp_list = self.get_calc_nx_ny(ny_o * 9 + nx_o)
                I = tmp_list[2]; J = tmp_list[3]; i = tmp_list[4]; j = tmp_list[5]
                II = i; JJ = j

                self.TTT[II * 3 + JJ] = "x"

                # locking for next x move
                locked_cells = items[2]
                self.LOCKED_CELLS = locked_cells
                # print('l=', len(self.LOCKED_CELLS), 'locked_cells = ', self.LOCKED_CELLS)
                count = -1
                for i in locked_cells:
                    count = count + 1
                    nx, ny = self.nx_ny_from_nytai(i)
                    self.LOCKED_CELLS[count] = nx + ny * 9

                x_temp_index = self.get_occupied_cells(self.X_LABELS, "x")
                for i in x_temp_index:
                    self.LOCKED_CELLS.append(i)
                o_temp_index = self.get_occupied_cells(self.O_LABELS, "o")
                for i in o_temp_index:
                    self.LOCKED_CELLS.append(i)
                # print('temp_indexes:',x_temp_index,o_temp_index)

            time.sleep(0.5)

        # ========================================================================================
    def get_calc_nx_ny(self,ind):

        for jj in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                for ii in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                    ind_calc = jj * 9 + ii
                    if ind == ind_calc:
                        I = divmod(ii,3)[0]; i = divmod(ii,3)[1]
                        nx_calc = 3*I + i
                        J = divmod(jj, 3)[0]; j = divmod(jj, 3)[1]
                        ny_calc = 3*J + j
        return nx_calc,ny_calc,I,J,i,j

    def members_of_large_box(self,left_corner):
        i, j = left_corner
        items1 = [(i, j), (i + 1, j), (i + 2, j)]
        items2 = [(i, j + 1), (i + 1, j + 1), (i + 2, j + 1)]
        items3 = [(i, j + 2), (i + 1, j + 2), (i + 2, j + 2)]
        items = items1 + items2 + items3
        return items

    def player_move(self,board,screen, color, label, nx,ny):
       # font and font size
       # if label == "x":
       #     color = blue
       # else:
       #     color = red

       myfont = self.font

       _x0 = board.x
       _y0 = board.y

       _cell_width = board.width/9
       _cell_height = board.height/9

       text_surf, text_rect = self.text_objects(label, myfont, color)
       # TextRect.center = ((x - width + nx * width / 3 + width / 6), (y - height + ny * height / 3 + height / 6))

       text_rect.center = _x0 + nx*_cell_width + _cell_width/2, _y0 + ny*_cell_width + _cell_width/2
       screen.blit(text_surf, text_rect)
       return

    # def drawing_loop(self,c,ttt,uttt,cn,threadname,queue):
    def drawing_loop(self, c, ttt, uttt):
        """runs the graphics loop
        """
        pygame.init()
        [screen,myfont] = self.display_screen()
        self.font = myfont

        while (True):
            # check for quit events
            # sys.exit() # comment this line for graphics
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit();
                    sys.exit();

            # erase the screen
            screen.fill(white)
            x0 = ttt.x
            y0 = ttt.y
            self.draw_board(uttt, screen, c)
            self.player_move_click_generator(uttt, screen)
            # update the screen
            pygame.display.update()

            # ===============================================================================================================
            # ===============================================================================================================
            # ===============================================================================================================
            # ===============================================================================================================
            # ******************** End Graphics Classes *************************************************************************

from multiprocessing import Queue
def run_gui(threadname,queue):
    import conn
    cn = conn.Con(81,threadname,queue)
    # initialize board clases
    cell = Cell()
    cell.x = 0
    cell.y = 0
    cell.width = 50
    cell.height = 50

    x0 = 0; y0 = 0
    ttt = tttBoard(x0,y0,cell)

    uttt = utttBoard(x0,y0,ttt)

    drawing_utt_board = DrawUttBoard(cn, threadname, queue) # cn is the Con object
    drawing_utt_board.drawing_loop(cell, ttt, uttt)

# run_gui()
