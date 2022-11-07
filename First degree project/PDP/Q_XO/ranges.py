"""For the ranges of Q_xo"""


size=4


def jmp(f,j,s=size): return [x*j+f for x in range(s)]
"""
f - The first element in the list.
j - The number to add each jump.
s - How many times to jump.
"""
# -------------------------------------------------


def get_lines(l,j1,j2):
    lines=[]
    if len(l)!= size: return None
    else:
        for a in l:
            l1=jmp(a,j1)
            for b in l1:
                lines.append(jmp(b,j2))
    return lines
# ---------------------------------------------------


def get_diags(l,j1,j2):
    diags=[]
    if len(l)!= size: return None
    else:
        for a in l:
            diags.append(jmp(a,j1))
            diags.append(jmp(a+3,j2))
    return diags

def base_r():
    return [jmp(1,4),jmp(1,16)]

# ------------------Horizontal---------------------
def rows_h(l): return get_lines(l,4,1)
def cols_h(l): return get_lines(l,1,4)
def diags_h(l): return get_diags(l,5,3)
# ------------------Vertical---------------------
def rows_v(l): return get_lines(l,16,1)
def cols_v(l): return get_lines(l,1,16)
def diags_v(l): return get_diags(l,17,15)
# ------------------------------------------------

def get_all():
    v,h=base_r()
    all=[]
    t=[rows_h(h), cols_h(h), diags_h(h), rows_v(v), cols_v(v), diags_v(v)]
    for x in t:
        all.extend(x)
    return all

# print(base_r())
def fix(l):
    """
    Source: https://www.codecademy.com/en/forum_questions/50c4df2cd7bd621707004664#answer-51b52b7b7c82ca607c01d5dc
    :param l: The list
    :return: 
    """
    new=[]
    for x in l:
        if x not in new: new.append(x)
    return new


all_lines = fix(get_all())
# print(len(all_lines), len(get_all()))
# print(base_r())
# for i in all_lines:
#     print(i)
