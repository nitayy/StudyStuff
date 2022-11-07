import random
import tools


def get_sqr(sqrs):
    """
    Same as at the class.
    :param sqrs:
    :return:
    """
    if (len(sqrs)==0):
        return None
    s = random.randint(0, len(sqrs) - 1)
    return sqrs[s]


class randcomp:
    """A random comp class"""

    def get_sqr(self,sqrs):
        """

        :param sqrs:
        :return:
        """
        if len(sqrs)==0: return None
        s = random.randint(0, len(sqrs)-1)
        return sqrs[s]