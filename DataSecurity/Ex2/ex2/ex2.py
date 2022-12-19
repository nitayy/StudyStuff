# Created by: Nitay Yehezkely

from Crypto.Cipher import AES
import os

"""
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = "The answer is no"
ciphertext = obj.encrypt(message)
print (ciphertext)
#'\xd6\x83\x8dd!VT\x92\xaa`A\x05\xe0\x9b\x8b\xf1'
obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
print (obj2.decrypt(ciphertext))
"""


# --------------- Functions -------------------------------------
def SIZE():
    return 16


def div_16(o):
    r = []
    for i in range(0, len(o), SIZE()):
        r.append(o[i:i + SIZE()])

    return r


def xor(o1, o2):
    return [ord(i) ^ ord(j) for i, j in zip(o1, o2)]


def cut(o):
    c = int(o[-1], SIZE())
    return o[:SIZE() - c]


def n_of_clip(str):
    t = str.replace("oceans_aes-audio=65000-video=370000-", "")
    return int(t)


def iv(i):
    if i > 16:
        return None
    b = str(bin(i)[2:])

    return "0" * (SIZE() - len(b)) + b


# ----------------------- The CBC Section ------------------------------
# -------------- Getting the key: ------------------
key = open("oceans.key", "rb")
key1 = key.read()
key.close()
obj = AES.new(key1, AES.MODE_ECB)

# --------------- Making list of .ts files: --------
t = os.listdir("./")
ts = []

for i in t:
    [temp, ex] = os.path.splitext(i)
    if ex == '.ts' and 'new' not in temp:
        ts.append(i)

# --------- Description each file: ---------------------


for i in ts:
    [num, ex] = os.path.splitext(i)
    f = open(i, 'rb')
    c = f.read()
    f.close()
    parts = div_16(c)
    dec = []
    print(parts)
    obj = AES.new(key1, AES.MODE_ECB)
    temp = obj.decrypt(parts[0])
    print(type(temp))
    print(temp)
    print(xor(iv(n_of_clip(num)), temp))
    dec.append(xor(iv(n_of_clip(num)), temp))
    for p in range(1, len(parts)):
        temp = obj.decrypt(parts[p])
        dec.append(xor(parts[p - 1], temp))

    for f in dec:
        print(f)
