import pdp

class UPdp:
    def __init__(self):
        self.main_p=pdp.Pdp()
        self.pdps={i:pdp.Pdp() for i in range(1,10)}

    def ins(self,i,b,s):
        """
        Enter a sign s to board b at square i.
        :param i: 
        :param b: 
        :param s: 
        :return: T/F if succeeded 
        """
        if s not in ['x','o'] or s not in range(1,10) or b not in range(1,10):
            return False
        else:
            self.pdps[b].set_input(i,s)
            return True

    def ins_main(self,s,i):
        if s not in ['x', 'o'] or i not in range(1, 10):
            return False
        else:
            self.main_p.set_input(i,s)

    def show_main(self):
        self.main_p.show_pdp1()

    def show_borad(self,i):
        if i in range(1,10):
            self.pdps[i].show_pdp1()

    def show(self):
        print("The main board:")
        self.show_main()
        print("The other boards:")
        for i in range(1,10):
            print("="*75)
            print("Board no.",i)
            self.show_borad(i)
            print("="*75)
