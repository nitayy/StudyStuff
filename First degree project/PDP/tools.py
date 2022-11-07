#Some useful functions....

import xo
import copy
import random



# ***************************************************************************************
# -----------------------------Lists-----------------------------------------------------
# ***************************************************************************************
# ---------------------------------------------------------------------------------------

def first_true(l):
    """
    The function get a list of booleans and return the number of the first element is true. 
    If all False it's return -1.
    :param l: List of booleans.
    :return: Index (int)
    """
    for i in l:
        if i:
            return l.index(i)
    return -1


# ----------------------------------------------------------------------------------------
def sub_list(l,idx):
    """
    The function get a list (l) and array (or list) of indexes and returns the the list l only with the indexes
    that are at idx.
    :param l: The list.
    :param idx: The indexes.
    :return: The new list.
    """
    return [l[x] for x in idx]
# ----------------------------------------------------------------------------------------


def in_arr_list(lists,o):
    """
    The function gets an lists of lists and object and return all the lists from "lists" with "o"
    :param lists: The lists of the lists. 
    :param o: The object.
    :return: List of lists
    """
    l=[]

def all(l,s):
    """
    The function gets a list and a sign and return True if all the list is sign.
    :param l: The list.
    :param s: The sign.
    :return: True or False
    """

    for i in l:
        if (i != s):
            return False
    return True

# ----------------------------------------------------------------------------------------

def at_lists(ls,o):
    """
    The function get a list of lists (ls) and object "o" - and return a list with all the lists from
    ls that have o
    :param ls: 
    :param o: 
    :return: List l 
    """
    return [x for x in ls if o in x]

# ----------------------------------------------------------------------------------------

def two_at_list(l,s1,s2):
    """
    
    :param l: 
    :param s1: 
    :param s2: 
    :return: 
    """
    return ((s1 in l) and (s2 in l))
# ----------------------------------------------------------------------------------------


def p_list(l):
    """
    The function gets a list and print the *int* value of the objects at the list.
    :param l: The list.
    :return: None
    """
    for i in (l):
        print(int(i),end=' ')


# ----------------------------------------------------------------------------------------

def a_from_b(l):
    """
    The function gets a list 'l' and returns one object randomly from it. 
    :param l: The list.
    :return: and object from the list.
    """
    if (len(l)==0):
        return None
    s = random.randint(0, len(l) - 1)
    return l[s]

# ***************************************************************************************
# -----------------------------XO boards-------------------------------------------------
# ***************************************************************************************
def optional_moves(bo, sign):
    """
    The function return a vecor of optional moves.
    :param sign: The sign that we want to put.
    :return:
    """
    key= {}
    for i in bo.empty:
        temp_bo=copy.deepcopy(bo)
        temp_bo.ins(i,sign)
        key[i]=temp_bo

    return key
# ----------------------------------------------------------------------------------------


def flip(b):
    """
    The function gets board b, and replaces all the '.' at sign 'º'.
    :param b: The board.
    :return: Tne new board.
    """
    new = []
    for i in b:
        new.append('º' if i=='.' else i)
    return new

# ----------------------------------------------------------------------------------------


def flip_back(b,s):
    """
    The function gets board b, and replaces all the s at '.'.
    :param b: The board.
    :param s: the sign.
    :return: Tne new board.
    """
    new = []
    for i in b:
        new.append('.' if i==s else i)
    return new


# -------------------------------------- Transforms For u_xo-----------------------------
def to_2n(n):
    """
    The fun ction get a square between 1-81.
    :param n: The square.
    :return: A list [b,s], where b is the board and s is the square.
    """
    if (n%9 != 0):
        return([(n//9)+1,(n % 9)])
    else:
        return([(n//9),9])
# --------------------------------------------------------------------------------

def to_1n(b,s):
    """
    The function gets a board and a square and returns the the square at overall.
    :param b: The board.
    :param s: The square.
    :return: A integer between 1 to 81 (the square)
    """
    return ((b-1)*9 + s)
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
