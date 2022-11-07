"""For return a sqaure stat"""

import players

class color:
    """Class for presenting color"""
    def __init__(self,col):
        self.color=col


color = {'active':'green', 'block':'white', 'win_o':'blue', 'win_x':'red','sign':'black', 'last_x':'C1', 'last_o':'C2'}

def get_col(str):
    return color[str] if str in color else 'pink'

class Sqr:
    def __init__(self,data,col,lock, last_move):
        """
        :param data: 'x' or 'o' 
        :param col: A string from 'color'.
        :param lock: True or False.
        :param marked: T/F
        """
        self.d=data
        self.l=lock
        self.m = True if data=='x' or data=='o' else False # If marked.
        self.c=col

        # sign_col is only relevant if the square marked
        if (data=='x' and last_move):
            self.sign_col = color['last_x']
        elif (data=='o' and last_move):
            self.sign_col = color['last_o']
        elif self.m:
            self.sign_col = color['sign']

    def get_sqr_dic(self):
        """
        :return: The parameters as dictionary  
        """
        return {'data':self.d, 'color':self.c, 'locked':self.l, 'marked':self.m }

    def get_sqr_list(self):
        return [self.d,self.c,self.l,self.m]
