from multiprocessing import Queue
class Con:
    def __init__(self,lim,threadname,queue):
        """
        :param lim: the range of the squares - between 1 to lim.
        """
        self.lim=lim
        self.threadname = threadname
        self.queue = queue

    def set_n(self,items):
        n = items[0]
        if n in range(1,self.lim+1):
            self.queue.put([items])
            if (self.threadname == "Gui"):
                print("========================")
            # print("set", self.threadname, "\t", items)
            print("set", self.threadname, "\t", items[0])
        else:
            n = -1
            items[0] = n
            self.queue.put([items])
            print("set", self.threadname, "\t", items[0])

    def get_n(self):
        [items] = self.queue.get()
        # n = items[0]
        print("get", self.threadname, "\t", items[0])
        return items
