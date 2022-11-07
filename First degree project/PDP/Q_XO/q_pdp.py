import Q_XO.ranges as r
import xo
import tools


SIZE=64
SIZE2=len(r.all_lines)
STAT = ["e", "x", "xx", "xxx", "xo", "o", "oo", "ooo"]


def next_stat(stat,sign):
    """
    The function gets an element from STAT and a sign and return the "next" STAT.
    :param stat: The STAT
    :param sign: the sign.
    :return: Element from STAT.
    """
    if stat==STAT[0]: return sign
    if (stat in STAT[1:4] and sign=='o') or (stat in STAT[5:8] and sign == 'x')  or stat==STAT[4]: return 'xo'
    else:
        if len(stat)<3 :
            return stat+sign
    return stat


# ---------------------------- Functions ---------------------------------
def is_in(l,o): return [a for a in l if o in a]
def get_nums(s,items): return [s.index(x) for x in items]
# -------------------------------------------------------------------------

class QPDP:
    def __init__(self,f_sign='o'):
        self.f_sign=f_sign # Friendly sign
        self.e_sign=xo.opp_sign(f_sign)
        self.in_f = [False]*SIZE
        self.in_e = [False]*SIZE
        self.out = [False]*SIZE
        self.det_unit = { x:[True if x == STAT[0] else False]*SIZE for x in STAT}

    def is_free(self,i):
        """
        The function get a square (1-64) and return if it's free or not.
        :param i: Ind between 1-64.
        :return: T/F
        """
        if i not in range(1,65): return False
        if not self.in_e[i-1] and not self.in_f[i-1]:
            return True
        else:
            return False

    def free_sqrs(self):
        """
        The function return a list of all the free squares.
        :return: A list.
        """
        f = []
        for i in range(1,65):
            if self.is_free(i): f.append(i)

        return f

    def update_det_unit(self,i,sign):
        """
        The function get index of a and a sign and update the "det_units".
        :param i: The index of the det_unit.
        :param sign: The sign.
        :return: T/F
        """
        size=len(STAT)
        if i not in range(1,65) or sign not in ['x','o']:
            return False
        stat=0
        while not self.det_unit[STAT[stat]][i-1]:
            stat+=1
        self.det_unit[STAT[stat]][i-1]=False
        new=next_stat(STAT[stat],sign)
        new=STAT.index(new)
        self.det_unit[STAT[new]][i-1]=True

    def update_in(self,i,sign):
        """
        The function updates the input units.
        :param i: 
        :param sign: 
        :return: 
        """
        if sign==self.f_sign:
            self.in_f[i-1]=True
        else:
            self.in_e[i - 1] = True

    def update_output(self,i):
        """
        
        :param i: 
        :return: 
        """
        self.out = [False] * SIZE
        self.out[i - 1] = True


    def ins_move(self,i,sign):
        """
        Inserting a square
        :param i: The square [1,64]
        :param sign: The sign
        :return: T/F
        """
        self.update_in(i,sign)
        with_i = is_in(r.all_lines,i)
        for j in with_i:
            idx=r.all_lines.index(j)
            self.update_det_unit(idx,sign)


    def show(self):
        print("Friendly input: ",end=' ')
        tools.p_list(self.in_f)
        print("\nEnemy input: ", end=' ')
        tools.p_list(self.in_e)
        print("\nOutput unit (only when the enemy make move): ", end=' ')
        tools.p_list(self.out)
        print("\n"+"*"*70)
        # Printing the det. units:
        for k in STAT:
            print(k+":      ",end=' \t')
            print(tools.p_list(self.det_unit[k]))


    def hur1(self):
        """
        This heuristic function trying to make a draw. 
        :param sign: The sign of the pdp
        :return: 
        """
        f = self.free_sqrs()

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        def look_free_sqr(i):
            """
            Th function gets and item from ranges and return the first free square from it.
            :param i: 
            :return: An index (1-64)
            """
            for s in r.all_lines[i+1]:
                if s in f:
                    return s

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        for x in ['ooo','xxx','oo','x']:
            if True in self.det_unit[x]:
                t = self.det_unit[x].index(True)
                if t != None:
                    u = look_free_sqr(t)
                    if u in f:
                        self.update_output(u)
                        return

        self.update_output(f[0])

    def hur2(self):
        f = self.free_sqrs()
        self.update_output(f[0])


    def get_move(self):
        return self.out.index(True)+1



