
class GameStat:
    """Class for game statistics"""
    def __init__(self):
        self.wins=[0,0,0] # [x,o,draws]

    def inc_wins(self,sign):
        if sign=='x': self.wins[0]+=1
        elif sign=='o': self.wins[1]+=1
        else: self.wins[2]+=1

    def get_wins(self):
        return self.wins

    def get_stat(self):
        temp=100/sum(self.wins)
        return [x*temp for x in self.wins]