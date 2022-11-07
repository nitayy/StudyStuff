class Con:
    def __init__(self,lim):
        """
        :param lim: the range of the squares - between 1 to lim.
        """
        self.lim=lim
        self.n = -1
        self.active = False
        self.items={} # A dictionary of objects.

    def set_n(self,x):
        if x in range(1,self.lim+1):
            self.n=x
            self.active = True
        else:
            self.n = -1

    def get_n(self):
        self.active = False
        k = self.n
        self.n=-1
        return k

    def add_item(self,name,obj): self.items[name]=obj

    def get_item(self,name): return self.items[name]


"""
הסבר קצר על המחלקה הנ"ל:
המחלקה הזאת באה לחבר בין הממשק הגרפי לחלק האלגוריתמי.
היא מחזירה את המהלך הבא.

n:
זהו המהלך הבא

בנוסף, ישנו דגל - active - שמעדכן האם נלקח או הושם ערך במשתנה.
אפשר להשתמש בו בתור מנועל 
"""