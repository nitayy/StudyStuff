# Created by: Nitay Yehezkely

from Crypto.Cipher import AES
import os
import struct


# --------------- Functions -------------------------------------
def SIZE():
    return 16


def div_16(o):
    r = []
    for i in range(0, len(o), SIZE()):
        r.append(o[i:i + SIZE()])

    return r


def xor(o1, o2):
    return [ord(a) ^ ord(b) for a, b in zip(o1, o2)]


def cut(o):
    c = int(o[-1], SIZE())
    return o[:SIZE() - c]


def n_of_clip(str):
    t = str.replace("oceans_aes-audio=65000-video=370000-", "")
    return int(t)


def iv_hex(i):
    s = (hex(i)[2:].zfill(32))
    return s.decode('hex')

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

    #Doing the first step of decoding:
    temp = obj.decrypt(parts[0])
    dec.append(xor(iv_hex(n_of_clip(num)), temp))

    for p in range(1, len(parts)):
        dec.append(xor(parts[p - 1], obj.decrypt(parts[p])))

    # Removing the padding:
    for i in range(dec[-1][-1]):
        dec[-1].pop()

    name = 'new'+str(n_of_clip(num))+".ts"
    print(name)
    new = open(name,'wb')
    for i1 in dec:
        for i2 in i1:
            new.write(chr(i2))
    new.close()
