import tools


class io:
    
    def __init__(self,size):
        self.size=size
        self.units=[False for i in range(self.size)] #The units, always begins at false!
    # *****************************************************************************************************#
    def __getitem__(self, item):
        return self.units[item]
    # *****************************************************************************************************#
    def turn_on(self,num):
        """
        Turn-on a unit
        :param num:
        :return:
        """
        self.units[num]=True
    # *****************************************************************************************************#
    def reset(self):
        """
        Turn-on a unit
        :param num:
        :return:
        """
        self.units = [False for i in range(self.size)]
    # *****************************************************************************************************#
    def show(self):
        tools.p_list(self.units)