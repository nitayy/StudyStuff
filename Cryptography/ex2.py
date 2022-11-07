# EX2 by: Nitay Yehezkely
from numpy import array as ar
import numpy

# *********************************** DATA *******************************
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = lambda x: ABC.find(x)
m = lambda x,i: ABC[(ABC.find(x)+i) % (len(ABC))]

englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W':
2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15,
'X': 0.15, 'Q': 0.10, 'Z': 0.07}

#Making frequency vector of the ABC
eng=list(englishLetterFreq.keys())
eng.sort()
f_eng=[englishLetterFreq[i]/len(ABC) for i in eng]


q1_text = """WERXEOFBTKPKGBXUTPNIVFEGTRYWGXHVPGXFRJBHUKCMVNLQXOGCWIHGEAGRRKGDGYYGR
AKJRWXRIMRXUJMUVQETTKVZLVHTUGCTTPGCYQIKPMKFLRTNCCSINRGCMGORXGVFSCBPKC
AEKXGQEGWMGFERJAXFTGEAGIRTQVUCRKAGRXHPZQIAGICKXTJCXGQKFTKYFPSLOFTXGIW
PDFVYCJGKERTENZEXUNVAXIJVPIXZKZPVMKMEECZLIXZKYRBRYCGHTTWEAGIGHTRRGGHH
RJVHTZRWFUKFPMEICPMGKFTXPTPNIVZMCTPURWXTVTTKUZLVWGTPNIVZMCMJVBTMCZJTW
QGCGTVZMCHHRAXIJVPXLEFLIKQCJTWDFRWUAKFTTNXMGBVYKPGFZLTTEYGCLVRLRXDPYZ
XAKFTDGPGHTUVAGXVZBTTNCWZGQNLDGNPRDMJVADFOLLXVCERHNULYAEARQWHTKQIKKEE
DYEYYGTEKCGLYYGRAKJLTXFVBIHFVAGRRKRWXEZNWXTKCMMHFPBTNCWPVTPNIHUPQIXOZ
QIAGFPSXTVBABUKMUXNVKTGVJMUYKEGIXRFQHBDCCEECZLIXZKQUBPZRTIQJQXUNVANIJ
VPIXZKQUBPZRTIQJQXUNVITRURLSMJVCCVTPNIBQEYCWFVAGRRKGDGCCEDKKKFBLYYGRA
EFPGXUGMCWVFCPVJBCNDGPQPKGZKEHTKYCMDFRWYQIKPENPYCWKEYRMWRJEKCTRXVGRQR
BRYCGLYZRWHWKTPKKRZAXMVWHVCEZTMTZTXTNCWQKQBCCPKKFDGNPRWXMEMLEGUETHHKF
TVKGFTKWJCSTPUYGXVYCGXHFPTNUVJTLUFPTOGEADNPKCGITFBJVVZTTYQIKDLVGSGIQJCH"""


M1 = "GCKAMBYBUSJLYTDJUQLUQUUGUNLFHYZBLJUF"
M2 = "HRQVKWTMOHVUTYHOYTGDURYVZUVULHYMVOYQ"
M3 = "LNSTWODMCLTYDELCEDQFYNETZYTYRLEMTCES"
M4 = "GOMNFYNTIHDBPPZPONSJGBKVPFDBMEPYPDHO"

# ********************************* Vigener Code ********************************
# -------------------------------------------------------------------------------------
def rot(s,i):
    """
    The function gets string s and rotate it at i steps.
    get the idea from here: https://www.geeksforgeeks.org/string-slicing-python-rotate-string/
    :param s: The string.
    :param i: How much to rotate.
    :return: String s rotated
    """
    return s[len(s)-i:]+s[0:len(s)-i]

# --------------------------------------------------------------------------------------
def find_match(s1,s2):
    """
    The function gets two strings and returns how many characters are same at place i.
    :param s1: The first string.
    :param s2: The second string.
    :return: How many characters fits. -1 it the length of the strings are not equal.
    """
    if len(s1)!=len(s2):
        return -1
    else:
        sum=0
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                sum+=1
        return sum

# --------------------------------------------------------------------------------------
def cou(s):
    """
    The function generates a list with the frequency of the letters at s.
    :param s:
    :return:
    """
    r = []
    for c in ABC:
        r.append([s.count(c), c])
    r.sort(reverse=True)
    return r

# --------------------------------------------------------------------------------------
def div_to_blocks(text,v):
    """
    Divided texts to blocks of size v.
    :param text: The text.
    :param v: integer > 1
    :return: A list of blocks
    """
    text=text.replace("\n","")
    if v < 1:
        return None
    b=[]
    [m,n]=divmod(len(text),v)
    for i in range(m):
        b.append(text[v*i:v*(i+1)])
    return b

# --------------------------------------------------------------------------------------
def take_i(blks,i):
    """
    The function get a list of strings (size equaled) and return a list if the i's
    of each.
    :param blks: list of blocks.
    :param i: integer > 0
    :return:
    """
    b=[]
    for k in blks:
        b.append(k[i-1])
    return b
# --------------------------------------------------------------------------------------

def freq_vec(v):
    """
    The function builds a frequency vector of v.
    :param v: A text of ABCD...
    :return: Vector with numbers.
    """
    f=[]
    n=len(v)
    for le in ABC:
        f.append((v.count(le)/n))
    return f



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Q1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# - Answer for Q1 - first method:
ma=[]
for i in range(2,7):
    ma.append(find_match(q1_text,rot(q1_text,i)))
print(ma)
"""
As we can see the output is: [30, 38, 31, *53*, 48], So  the 
length of the key is 5.
Now we will take each char at block
"""
key_len=5
q1_t=q1_text.replace("\n","")
b=div_to_blocks(q1_text,key_len)
the_key=[]



for i in range (1,key_len+1): # For each letter in the block.
    the_i_cell=take_i(b,i) # Takes the 'i' letter at each block.
    freq=freq_vec(the_i_cell) # build frequency vector
    sum_v=[]
    for k in range(len(ABC)):
        r = rot(f_eng,k)
        r=ar(r)
        freq = ar(freq)
        sum_v.append(sum(r*freq))
    the_key.append(sum_v.index(max(sum_v)))
key_word=[ABC[x] for x in the_key]

def dec(let,place):
    """

    :param let:
    :param place:
    :return:
    """
    m = place % key_len
    temp=(n(let) - the_key[m]) % len(ABC)
    return ABC[temp]

d_text = [dec(x,i) for x,i in zip(q1_t,range(len(q1_t)))]

def q1():
    key_word="".join(key_word)
    d_text="".join(d_text)
    print("The key word is: ",key_word,"\nAnd the Plaintext is: \n",d_text)
#q1()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Q2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SIZE=len(ABC)
# --------------------------------------------------------------
def move_s(s,move):
    """
    Moving string s at n moves at the ABC.
    :param s: A string.
    :param move: An integer.
    :return: The moved string.
    """
    return "".join([m(x,move) for x in s])

# ---------------------------------------------------------------

def sub_str(s1,s2):
    """
    The function gets two strings and sub between each letter at the i place of both.
    We assuming that the strings are length equal.
    :param s1:
    :param s2:
    :return: A list of integers.
    """
    return [n(s1[i])-n(s2[i]) for i in range(len(s1))]



#Now we will try to find which string encoded by moving encryption.
def freq_m2m3():
    for mn in M2,M3:
        print("~"*50)
        print(cou(mn))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Q2-B ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

l_m2="YVUH"
l_m3="TEYL"
# ---------------------------------------------------------------
def ck_diff(msg):
    """
    The function gets two groups of letters and returns the differences 
    between them
    :param msg: The most common letters in a message.
    :return: A vector of differences
    """
    d=[]
    for l in msg:
        for le in "ETAO":
            if n(l) != n(le):
                d.append((-(n(l)-n(le))) % SIZE)
    return d
# ---------------------------------------------------------------
def find_sub_msg():
    d2 = ck_diff("YVUH")
    d3 = ck_diff("TEYL")
    print("Now we checking M2:")
    for i in d2:
        print(i,'\t',move_s(M2,i))
    print('*'*50,"\nNow we checking M3:")
    for i in d3:
        print(i,'\t',move_s(M3,i))

# ---------------------------------------------------------------
find_sub_msg()

text = "ACHILDSBRAINSTARTSFUNCTIONINGATBIRTH"

# ~~~~~~~~~~ Q2-M2 - Affine code ~~~~~~~~~~
de = lambda x: (21*(x - 7)) % SIZE # Encryption function.
e = lambda x: (5 * x  + 7) % SIZE # Description function.

def ein(msg):
    for i in msg:
        temp=e(ABC.find(i))
        print(ABC[temp],end='')
# Output: HRQVKWTMOHVUTYHOYTGDURYVZUVULHYMVOYQ

def des(msg):
    for i in msg:
        temp = de(ABC.find(i))
        print(ABC[temp], end='')
# Output: ACHILDSBRAINSTARTSFUNCTIONINGATBIRTH


# ~~~~~~~~~~ Q2 - Vigener code ~~~~~~~~~~
def diff(s1,s2):
    """

    :param s1:
    :param s2:
    :return:
    """
    d=[]
    for i in range(len(s1)):
        d.append(((n(s2[i])-n(s1[i])) % SIZE))
    w = [ABC[x] for x in d]
    return w

for mn in [M1,M4]:
    print(diff(text,mn))

# Finding the key for description
# The key is: GADSBY
v_key = "GADSBY"
def find_des_key(key):
    for ke in key:
        print(ABC[(-(n(ke)) % SIZE)],end='')

find_des_key(v_key)
#UAXIZC
print('\n')

# ~~~~~~~~~~ Q2 - Hill code ~~~~~~~~~~

# Now we will find block of 4 at plaintext that we can put at the
# matrix - we need that ab-bc will have an opposite number.
def find_hill_block():
    t_blocks=div_to_blocks(text,4)
    for i in t_blocks:
        print(i, ((n(i[0])*n(i[2]))-(n(i[2])*n(i[1]))) % 26)
    print(div_to_blocks(text,4))
    print(div_to_blocks(M4,4))

for i in "ITRHPHDO":
    print(i,n(i))

print('\n')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Q3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def m5(nums,l):
    for i in range(l):
        nums.append((nums[i]+nums[i+1]+nums[i+4]) % 2)
    return nums

# First try, checking if given the provided series.
print(m5([1,1,1,1,0],17))

d_msg=[]
for i in "01100010101110011101010001000110001010111001110101":
    d_msg.append(int(i))

k_m5=m5([1,1,1,1,0],50)

# Checking the cycle of the recursive formula:
print("".join(str(i) for i in k_m5))

# get the original message:
def org_mes():
    p_m5=[(i+j) % 2 for i,j in zip(d_msg,k_m5)]
    org_msg="".join(str(i) for i in p_m5)
    print(org_msg)
org_mes()

cyc = "100100100100100100100100101"
print(len(cyc))
