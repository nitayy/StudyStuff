# written by: Nitay Yehezkely

from numpy import array as ar


# ---------- Basic functions: ----------------------

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = lambda x: ABC.find(x)  % 26


def mod_num(v1,v2,num):
    """
    The function gets two vectors and calculate v1[i]+v2[i] % num.
    :param v1:
    :param v2:
    :param num:
    :return:
    """
    return [(v1[i] + v2[i]) % num for i in range(len(v1))]


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

def back_to_letters(vec):
    v=[]
    for i in vec:
        v.append(ABC[i])
    return "".join(str(i) for i in v)

str_to_int = lambda v: [n(i) for i in v]

# --------- Basic Data: -----------------------------
plain_text = "INITTESTOFMETHOD"
IV = [n(i) for i in "INIT"]
hill = ar([[3,4,2,1],[3,2,3,4],[1,5,2,3,],[4,1,2,1]])

# ~~~~~~~~~~~~~~~~~~ Q3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


P = div_to_blocks(plain_text,hill.itemsize)
P = [str_to_int(i) for i in P]
C = [IV] #C = [list(hill.dot(IV) % 26)] |  list(hill.dot(mod_num(IV,P[0],26)) % 26 )

# The encrypted text, each row is a block:
for i in range(1,len(P)):
    C.append(list(hill.dot(mod_num(C[i-1],P[i],26)) % 26))

# The encrypted message:
C=C[1:] # Because C[0] is "INIT" and we don't need it...

print("Q3: The encrypted text, each row is a block:")
for i in range(len(C)):
    print("C",i+1,':  ',C[i])

# Now we will bring it back to letters:
CM=[]
for vec in C:
    for i in vec:
        CM.append(ABC[i])
CM = "".join(i for i in CM)

print("The encrypted message of Q3 is:")
print(CM)

# ~~~~~~~~~~~~~~~~~~~~~ Q4 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V = [1,0,0,1,1]
for i in range(30):
    V.append((V[i+1]+V[i+2]+V[i+3]) % 2)

Vr="".join(str(i) for i in V[:7])

# Q4-b
# At v_q4 we will calculate the encrypted message:
e_msg = "".join(str(i) for i in V[:14]) # What we are going to add to the message.


v_q4="10110010100010100111"
msg_to_enc=[int(i) for i in v_q4]
# The encrypted message:
enc_msg_q4_b= "".join(str(i) for i in mod_num(msg_to_enc, V[:len(msg_to_enc)], 2))
print("\nThe encrypted message of Q4-b is:")
print(enc_msg_q4_b)


# For Q4-c:
# Checking if V2 will be equal to V [below].
V2=V
for i in range(30):
    V2.append((V2[i] + V2[i + 2] ) % 2)

print(V[:30])
print(V2[:30])
# Yes. It is...