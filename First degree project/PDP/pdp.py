
# ------------------------Imports-----------------------------
import io_network as io
import detection_network as dn
import math
import xo
import tools
import copy


def first_empty(l):
    return l.index('.')


def look_free(board,i):
    """
    The function get a board and a index of a list and returns the first free square on th elist.
    :param board: 
    :param i: 
    :return: 
    """
    l=[board.board[x] for x in xo.dic[i-1]]
    print(l)
    return xo.dic[i-1][first_empty(l)]+1


def diff(l1, l2):
    if len(l1) != len(l2): return -1
    d = []
    for i in range(len(l1)):
        if l1[i]!=l2[i]:
            d.append(i)
    return d


def size(s=9):
    return s


class Pdp:
    # ***********************#
    """"The enemy is 'x' the friendly is 'o' """

    # ***********************#
    # Those boards are just for the preview:
    eb = xo.board()  # The enemy board
    fb = xo.board()  # The friend board.
    def __init__(self,sign='x',pr=True):
        self.f_sign = sign
        self.e_sign = xo.opp_sign(sign)
        self.s = size()
        self.k = int(2 * math.sqrt(self.s) + 2)
        self.pr=pr

        # self.enemy_input = io.io(self.s)
        # self.friend_input= io.io(self.s)
        # self.output = io.io(self.s)
        # self.sin_ene=dn.Detection(self.k)
        # self.sin_fri = dn.Detection(self.k)
        # self.dub_ene = dn.Detection(self.k)
        # self.dub_fri = dn.Detection(self.k)
        # self.empty = dn.Detection(self.k)
        # for i in range(self.k):
        #     self.empty.turn_on(i)

        def arr(s,b): return [b]*s
        self.enemy_input = arr(size(),False)
        self.friend_input = arr(size(),False)
        self.output = arr(size(),False)
        self.sin_ene = arr(self.k,False)
        self.sin_fri = arr(self.k,False)
        self.dub_ene = arr(self.k,False)
        self.dub_fri = arr(self.k,False)
        self.empty = arr(self.k,True)

        self.d_net=[self.sin_ene,self.dub_ene,self.sin_fri,self.dub_fri,self.empty]
        self.d_str=["Enemy Singleton:    ", "Enemy doubleton:    ", "Friendly Singleton: ","Friendly doubleton: ",
                   "Empty lines:  "]

    def count_pieces(self):
        return [self.friend_input.count(True),self.enemy_input.count(True)]

    def reset(self):
        self.__init__(self.f_sign)

    # --------------------------------------------------------------------------------------------------------------
    # --------------------------- Functions for the Heuristics functions -------------------------------------------
    # --------------------------------------------------------------------------------------------------------------
    def free(self,s):
        """
        The function get a square and return if it's free or not.
        :param s: The square no. 1-9.
        :return: T/F (True = free).
        """
        if not self.friend_input[s-1] and not self.enemy_input[s-1]:
            return True
        else:
            return False

    def free_sqrs(self):
        """
        The function return a list of the empty squares.
        :return: List
        """
        f=[]
        for i in range(1,10):
            if self.free(i):
                f.append(i)
        return f

    def at_free(self,l):
        """
        The function get a list and return the index of ot the first item that in the free squares.
        If none of the items is like this - it's return -1.
        :param l: The list of the squares.
        :return: An integer.
        """
        f = self.free_sqrs()
        for i in l:
            if i in f:
                return i #l.index(i)
        return -1

    def count_empty(self,sqr,sign):
        """
        The function gets a square number (1-9) and sign and return how many empty (or only with the sign) lines there
        are from the square.
        :param sqr: The square.
        :param sign: The sign.
        :return: 
        """
        sum=0
        k = tools.at_lists(xo.wins,sqr)
        for i in k:
            p = xo.wins.index(i)
            if (self.empty[p] or not self.sin_ene[p]):
                sum += 1
        return sum

    def only_dub(self,sign,q):
        """
        The function get a sign and a list of squares q, returns a square that follow by:
        1. It makes a dub_friendly WITH NO opp_sign at the third square (it must be empty!).
        2. The empty square is not q.
        :param sign: The sign.
        :param q: A list of squares.
        :return: An int (1-9) of a square.
        """
        f = self.free_sqrs()
        for w in xo.wins:
            i=xo.wins.index(w)
            if self.sin_fri[i] and not self.sin_ene[i]:
                for s in w:
                    if s not in q:
                        self.set_output(s)
                        return
        return -1

    def find_fork(self):
        f = self.free_sqrs()
        q=[]
        for i in f:
            new_pdp = copy.deepcopy(self)
            new_pdp.set_input(i,self.e_sign)
            d = diff(self.dub_ene,new_pdp.dub_ene)
            # print("D is:  ",d)
            if len(d) == 2:
                for j in d:
                    if True not in tools.sub_list(self.friend_input, xo.n_wins[j]) :
                        # print("DDD",j, xo.n_wins[j], tools.sub_list(self.friend_input, xo.n_wins[j]))
                        if i not in q: q.append(i)
        # print("Q is:",q)
        if len(q)==0:
            return -1  # There are no forks!
        if len(q)==1:
            self.set_output(q[0])
            return
        # print("IN FIND FORK!")
        d = [x for x in f if x not in q]
        # print("D iS: ",d)
        for i in d:
            new_pdp = copy.deepcopy(self)
            new_pdp.set_input(i, self.f_sign)
            for j in range(len(new_pdp.dub_fri)):
                # print(j, xo.wins[j], tools.sub_list(self.enemy_input,xo.n_wins[j]), "AAABBB")
                e = tools.sub_list(new_pdp.friend_input,xo.n_wins[j])
                e2 = e.index(False)
                e2 = xo.wins[j][e2]
                if new_pdp.dub_fri[j] and not self.sin_ene[j] and e2 not in q and \
                                True not in tools.sub_list(self.enemy_input,xo.n_wins[j]):
                    # print("PUT IN FORK")
                    self.set_output(i)
                    return
        return -1



    # ---------------------------------------------------------------------------------------------------------
    # ------------------------ Heuristics Functions -> -> -> -> -> ->------------------------------------------
    # ---------------------------------------------------------------------------------------------------------
    def hur2(self): #For Checking
        t = self.free_sqrs()[0]
        self.set_output(t)

    # ---------------------------------------------------------------------------------------------------------
    def hur1(self):
        f = self.free_sqrs()

        def ret_true(li): return [i for i in range(len(li)) if li[i]]

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        def find_sqr():
            if self.pr:
                print("Options for winning:")
            max = [0, f[0]]
            for i in f:
                t = self.count_empty(i, self.f_sign)
                if self.pr:
                    print("(", i, '\t', t, ")")
                if t > max[0]:
                    max = [t, i]
            self.set_output(max[1])
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        def find_dub(dub,str):
            w = ret_true(dub)
            # print(str, w)
            for i in w:
                l = xo.wins[i]
                # print("L is:",l, "at", str)
                emp = self.at_free(l)
                if emp != -1:
                    # print("emp", emp)
                    self.set_output(emp)
                    return True
                else:
                   pass # print("NOT EMP")
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        if find_dub(self.dub_fri, "Dub-Fri"): return
        if find_dub(self.dub_ene, "Dub-Ene"): return
        if self.find_fork() is not -1:
            return
        find_sqr()







    # ---------------------------------------------------------------------------------------------------------


    def set_input(self, num, sign):
        """
        :return:
        """
        # if (sign==self.e_sign):
        #     self.enemy_input.turn_on(num-1)
        #     self.eb.ins(num,sign)
        # elif (sign==self.f_sign):
        #     self.friend_input.turn_on(num-1)
        #     self.fb.ins(num,sign)

        if (sign==self.f_sign):
            self.friend_input[num-1]=True
        else:
            self.enemy_input[num-1]=True


        for w in xo.n_wins:
            i = xo.n_wins.index(w)
            t_f = tools.sub_list(self.friend_input,w)
            f = t_f.count(True)
            t_e = tools.sub_list(self.enemy_input,w)
            e = t_e.count(True)
            # print("SUM", w,t_f,t_e,f,e)
            if f == 1: self.sin_fri[i] = True; self.empty[i] = False
            if f == 2: self.dub_fri[i] = True
            if e == 1: self.sin_ene[i] = True; self.empty[i] = False
            if e == 2: self.dub_ene[i] = True





    def set_output(self,out):
        # print("OUTPUT IS (set output):", out)
        self.output = [False]*size()
        self.output[out-1]=True

    def get_move(self):
        # print("OUTPUT UNITS", self.output)
        t = self.output.index(True)+1
        return t

    def show_d(self):
        print("Here are the detectors networks:")
        for i,j in (zip(self.d_net,self.d_str)):
            print(j,end='')
            tools.p_list(i)
            print()

    def show_io1(self):
        """
        The function shoes the the I/O networks as a *row*
        :return:
        """
        print("Here are the I/O networks:")
        print("The enemy pieces:    ",end=' ')
        tools.p_list(self.enemy_input)
        print("\nThe friendly pieces: ", end=' ')
        tools.p_list(self.friend_input)
        print("\nThe output:          ", end=' ')
        tools.p_list(self.output)

    def show_pdp1(self):
        """Show the PDP as rows (of all the networks)"""
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        self.show_io1()
        print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        self.show_d()

