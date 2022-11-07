# for  a human player

import tools

class human:
    def get_sqr(self,sqrs):
        """

        :param sqrs:
        :return:
        """
        good = False
        while (not good):
            s = input("Please enter a number: ")
            s=int(s)
            if (s in sqrs): good=True
            else: print("This square is empty!")

        return s