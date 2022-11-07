import tools


class Detection:
    def __init__(self,size):
        self.units=[False]*size
        self.size=size

    def __getitem__(self, item): return self.units[item]
    # *****************************************************************************************************#
    def turn_on(self,i):
        if (i in range(self.size)):
            self.units[i] = True
            return True
        else:
            self.units[i]=True

    # *****************************************************************************************************#
    def turn_off(self,i):
        if i in range (self.size):
            self.units[i]=False
            return True
        else:
            return False

    # *****************************************************************************************************#
    def show(self):
        tools.p_list(self.units)
