import pygame
import sys
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


class DrawUttBoard(object):
    """Draw Ulitmate tic-tac-toe board
    """
    def __init__(self, cn, threadname, queue):
        self.cell_width = 50
        self.cell_height = 50
        self.screen = None
        self.screen_width = self.cell_width * 9
        self.screen_height = self.cell_height * 9
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
        # self.TTT = [""] * 9
        # self.ALOWED_CELLS = [True] * 81
        self.last_x_move = 5
        self.last_o_move = 33
        self.next_x_board = -1
        self.locked_cells = []

        self.MOUSE_CELLS = [False]*81

        self.x0 = 0
        self.y0 = 0

    def display_screen(self):
        screen = pygame.display.set_mode(self.args)
        myfont = pygame.font.Font('freesansbold.ttf', 24)
        self.screen = screen
        self.font = myfont
        return [screen, myfont]

    def get_occupied_cells(self, list, val):
        """always returns a list containing the indices of val in list
        """
        retval = []
        last = 0
        while val in list[last:]:
            i = list[last:].index(val)
            retval.append(last + i)
            last += i + 1
        return retval

    def text_objects(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ NY $$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def get_nitay_index(self, nx, ny):
        ny_board = (divmod(ny, 3)[0]) * 3 + divmod(nx, 3)[0] + 1
        ny_cell = (divmod(ny, 3)[1]) * 3 + divmod(nx, 3)[1] + 1
        ny_index = (ny_board - 1) * 9 + ny_cell
        return ny_index

    def get_nx_ny_from_nitay(self, ny_index):
        ny_board = divmod(ny_index - 1, 9)[0] + 1
        corner = self.UPPER_LEFT_CORNERS[ny_board - 1]
        ny_cell = divmod(ny_index - 1, 9)[1]
        nx = corner[0] + divmod(ny_cell, 3)[1]
        ny = corner[1] + divmod(ny_cell, 3)[0]
        return (nx, ny)

    def get_nx_ny_for_nitay_board(self,ny_board):
        corner = self.UPPER_LEFT_CORNERS[ny_board - 1]
        nx = corner[0]
        ny = corner[1]
        return nx,ny
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ NY $$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def draw_cells(self):
        # draw cells
        for nitay_index in range(1, 82):
            nx, ny = self.get_nx_ny_from_nitay(nitay_index)
            _x = self.x0 + self.cell_width * nx
            _y = self.y0 + self.cell_height * ny
            _width = self.cell_width
            _height = self.cell_height
            rect = [_x, _y, _width, _height]
            if nitay_index % 2:
                color = gray
            else:
                color = light_gray
            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(self.screen, white, rect, 1)

    def draw_board_edges(self):
        # draw board edges
        for nitay_board in range(1, 10):
            nx, ny = self.get_nx_ny_for_nitay_board(nitay_board)
            _x = self.x0 + self.cell_width * nx
            _y = self.y0 + self.cell_height * ny
            _width = self.cell_width * 3
            _height = self.cell_height * 3
            rect = [_x, _y, _width, _height]
            pygame.draw.rect(self.screen, black, rect, 5)

    def player_move(self, color, label, nx,ny):
        screen = self.screen
        myfont = self.font
        _x0 = self.x0
        _y0 = self.y0
        _cell_width = self.cell_width
        _cell_height = self.cell_height
        text_surf, text_rect = self.text_objects(label, myfont, color)
        text_rect.center = _x0 + nx*_cell_width + _cell_width/2, _y0 + ny*_cell_width + _cell_width/2
        screen.blit(text_surf, text_rect)
        return

    def draw_signs(self):
        occupied_x = self.get_occupied_cells(self.X_LABELS, 'x')
        color = black
        # ========= x =========
        last_move_x_color = blue
        label = "x"
        for ind in occupied_x:
            if self.last_x_move == ind:
                draw_color = last_move_x_color
            else:
                draw_color = color
            nx, ny = self.get_nx_ny_from_nitay(ind)
            self.player_move(draw_color, label, nx, ny)
        # ========= o =========
        last_move_o_color = red
        label = "o"
        occupied_o = self.get_occupied_cells(self.O_LABELS, 'o')
        for ind in occupied_o:
            if self.last_o_move == ind:
                draw_color = last_move_o_color
            else:
                draw_color = color
            nx, ny = self.get_nx_ny_from_nitay(ind)
            self.player_move(draw_color, label, nx, ny)

    def draw_next_x_board_edge(self,color):
        next_x_board = self.next_x_board
        if not next_x_board == -1:
            nx, ny = self.get_nx_ny_for_nitay_board(next_x_board)
            _x = self.x0 + self.cell_width * nx
            _y = self.y0 + self.cell_height * ny
            _width = self.cell_width * 3
            _height = self.cell_height * 3
            rect = [_x, _y, _width, _height]
            pygame.draw.rect(self.screen, green, rect, 5)

    def get_cell_indeces(self, x, y):
        """extract indices by location"""
        _cell_width = self.cell_width
        _cell_height = self.cell_height
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
        return (_ind_x,_ind_y)

    def player_move_click_generator(self):
        mouse = pygame.mouse.get_pos()
        x_mouse = mouse[0]
        y_mouse = mouse[1]
        nx_mouse, ny_mouse = self.get_cell_indeces(x_mouse, y_mouse)
        self.MOUSE_CELLS = [False]*81
        index_mouse = ny_mouse * 9 + nx_mouse
        self.MOUSE_CELLS[index_mouse] = True
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            x = mouse[0]
            y = mouse[1]
            nx,ny = self.get_cell_indeces(x, y)
            n = self.get_nitay_index(nx, ny)
            print ("n = ",n)
            if n in enumerate(self.locked_cells):
                print ("got here")
                return
            if n > 0 and n < 82:
                set_list = [n]
                self.cn.set_n(set_list)
                self.X_LABELS[n] = "x"
                self.last_x_move = n

            items = self.cn.get_n()
            nitay_index = items[0]
            self.locked_cells = items[2]

            if nitay_index > 0 and nitay_index < 82:
                self.O_LABELS[nitay_index] = "o"
                self.last_o_move = nitay_index
                next_x_board = items[1]
                print ('next_x_board = ',next_x_board)
                if not next_x_board == -1:
                    self.next_x_board = next_x_board
            time.sleep(0.5)

    def draw_ttt_board(self):
        dum,dum = self.display_screen()
        self.draw_cells()
        self.draw_board_edges()
        self.draw_signs()
        self.draw_next_x_board_edge(green)

# ==============================================================================

from multiprocessing import Queue
def run_gui(threadname,queue):

    import conn
    cn = conn.Con(81,threadname,queue)
    # initialize board clases

    d = DrawUttBoard(cn, threadname, queue)

    pygame.init()
    [screen,myfont] = d.display_screen()

    while (True):
        # check for quit events
        # sys.exit() # comment this line for graphics
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit();
        d.draw_ttt_board()
        # erase the screen
        screen.fill(white)

        d.draw_ttt_board()
        d.player_move_click_generator()
        # update the screen
        pygame.display.update()


