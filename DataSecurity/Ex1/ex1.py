# ex1, written by: Nitay Yehezkely.

# ------------------------ Functions ---------------------------------------
def not_in_abc(str):
    n=[]
    for i in abc:
        if i.isalpha() and i not in str.lower():
            n.append(i)

    return n

def not_in_dic(dic):
    """
    Returns which 'abc' are not at the dic
    :param dic: Dictionary that keys are: 'a', 'b', 'c'.... 
    :return: A list.
    """
    n = []
    for i in abc:
        if i.isalpha() and i not in dic:
            n.append(i)

    return n

def print_key():
    print("The key is:")
    for i in dic:
        print(i," --> ",dic[i])

    print("- End of key -")

# ------------------------- Variables --------------------------------
# At 'pla' and 'cip' we can see that the words are at the same length if we go word by word.
pla = """
In cryptography, a substitution cipher is a method of encoding by which units of plaintext are replaced with ciphertext, according to a
"""
# Source: https://en.wikipedia.org/wiki/Substitution_cipher

cip = """
Vh bkgozjxkyosg, y ildizvzlzvjh bvosfk vi y cfzsjr jt fhbjrvhx dg psvbs lhvzi jt onyvhzfaz ykf kfonybfr pvzs bvosfkzfaz, ybbjkrvhx zj y 
"""

# The full encrypted text.
cip2 = """
Vh bkgozjxkyosg, y ildizvzlzvjh bvosfk vi y cfzsjr jt fhbjrvhx dg psvbs lhvzi jt onyvhzfaz ykf kfonybfr pvzs bvosfkzfaz, ybbjkrvhx zj y kfxlnyk igizfc; zsf "lhvzi" cyg df ivhxnf nfzzfki (zsf cjiz bjccjh), oyvki jt nfzzfki, zkvonfzi jt nfzzfki, cvazlkfi jt zsf ydjqf, yhr ij tjkzs. Zsf kfbfvqfk rfbvosfki zsf zfaz dg ofktjkcvhx yh vhqfkif ildizvzlzvjh.

Ildizvzlzvjh bvosfki byh df bjcoykfr pvzs zkyhiojivzvjh bvosfki. Vh y zkyhiojivzvjh bvosfk, zsf lhvzi jt zsf onyvhzfaz ykf kfykkyhxfr vh y rvttfkfhz yhr lilynng mlvzf bjconfa jkrfk, dlz zsf lhvzi zsfcifnqfi ykf nftz lhbsyhxfr. Dg bjhzkyiz, vh y ildizvzlzvjh bvosfk, zsf lhvzi jt zsf onyvhzfaz ykf kfzyvhfr vh zsf iycf ifmlfhbf vh zsf bvosfkzfaz, dlz zsf lhvzi zsfcifnqfi ykf ynzfkfr.

Zsfkf ykf y hlcdfk jt rvttfkfhz zgofi jt ildizvzlzvjh bvosfk. Vt zsf bvosfk jofkyzfi jh ivhxnf nfzzfki, vz vi zfkcfr y ivconf ildizvzlzvjh bvosfk; y bvosfk zsyz jofkyzfi jh nykxfk xkjloi jt nfzzfki vi zfkcfr ojngxkyosvb. Y cjhjynosydfzvb bvosfk lifi tvafr ildizvzlzvjh jqfk zsf fhzvkf cfiiyxf, psfkfyi y ojngynosydfzvb bvosfk lifi y hlcdfk jt ildizvzlzvjhi yz rvttfkfhz ojivzvjhi vh zsf cfiiyxf, psfkf y lhvz tkjc zsf onyvhzfaz vi cyoofr zj jhf jt ifqfkyn ojiivdvnvzvfi vh zsf bvosfkzfaz yhr qvbf qfkiy.

Yh fykng yzzfcoz zj vhbkfyif zsf rvttvblnzg jt tkfmlfhbg yhyngivi yzzybwi jh ildizvzlzvjh bvosfki pyi zj rvixlvif onyvhzfaz nfzzfk tkfmlfhbvfi dg sjcjosjhg. Vh zsfif bvosfki, onyvhzfaz nfzzfki cyo zj cjkf zsyh jhf bvosfkzfaz igcdjn. Lilynng, zsf svxsfiz-tkfmlfhbg onyvhzfaz igcdjni ykf xvqfh cjkf fmlvqynfhzi zsyh njpfk tkfmlfhbg nfzzfki. Vh zsvi pyg, zsf tkfmlfhbg rvizkvdlzvjh vi tnyzzfhfr, cywvhx yhyngivi cjkf rvttvblnz.

Ivhbf cjkf zsyh 26 bsykybzfki pvnn df kfmlvkfr vh zsf bvosfkzfaz ynosydfz, qykvjli ijnlzvjhi ykf fconjgfr zj vhqfhz nykxfk ynosydfzi. Ofksyoi zsf ivconfiz vi zj lif y hlcfkvb ildizvzlzvjh 'ynosydfz'. Yhjzsfk cfzsjr bjhivizi jt ivconf qykvyzvjhi jh zsf favizvhx ynosydfz; loofkbyif, njpfkbyif, loivrf rjph, fzb. Cjkf ykzvizvbynng, zsjlxs hjz hfbfiiykvng cjkf ifblkfng, ijcf sjcjosjhvb bvosfki fconjgfr psjnng vhqfhzfr ynosydfzi jt tyhbvtln igcdjni.

Yh vhzfkfizvhx qykvyhz vi zsf hjcfhbnyzjk. Hycfr ytzfk zsf oldnvb jttvbvyn psj yhhjlhbfr zsf zvznfi jt qvivzvhx rvxhvzykvfi, zsvi bvosfk bjcdvhfr y icynn bjrfdjjw pvzs nykxf sjcjosjhvb ildizvzlzvjh zydnfi. Jkvxvhynng zsf bjrf pyi kfizkvbzfr zj zsf hycfi jt vcojkzyhz ofjonf, sfhbf zsf hycf jt zsf bvosfk; vh nyzfk gfyki vz bjqfkfr cyhg bjccjh pjkri yhr onybf hycfi yi pfnn. Zsf igcdjni tjk psjnf pjkri (bjrfpjkri vh cjrfkh oyknyhbf) yhr nfzzfki (bvosfk vh cjrfkh oyknyhbf) pfkf hjz rvizvhxlvisfr vh zsf bvosfkzfaz. Zsf Kjiivxhjni' Xkfyz Bvosfk lifr dg Njlvi AVQ jt Tkyhbf pyi jhf; ytzfk vz pfhz jlz jt lif, cfiiyxfi vh Tkfhbs ykbsvqfi pfkf lhdkjwfh tjk ifqfkyn slhrkfr gfyki.
"""

abc = 'abcdefghijklmnopqrstuvwxyz'

dic = {}

# ---------------------------------- Main section ---------------------------------------------------


# Building the key:
for i in range(len(pla)):
    if (cip[i].isalpha()) and cip[i].lower() not in dic:
        dic[cip[i].lower()] = pla[i].lower()

n1 = not_in_abc(cip2)
n2 = []
for i in abc:
    if i not in dic and i not in n1:
        n2.append(i)
print("Those are not at the key but at the encrypted text: ",n2,'\n\n')

# We can see from above that we need to find the key for: 'm', 'q' and 'w' at the plaintext.
# From the word - fremuency (from the result of the output) - we can understand that m->q,
# from the word - attacws ( " ) - we can understand that w->k,
# and from the word - receiqer ( " ) - we can understand that q->v.
# *When I write "from the output" I mean from the output without this additions below...*
# So we will add it manually:
dic['m'] = 'q'
dic['w'] = 'k'
dic['q'] = 'v'

#And now the key is completed!

# Printing the key:
print_key()

# Printing the plaintext:
for i in cip2:
    if i.isalpha() and i.lower() in dic:
        if i.islower():
            print(dic[i], end='')
        else:
            print(dic[i.lower()].upper(),end='')
    else:
        if (i=='e' or i=='u'):
            print(i+'##',end='')
        else:
            print(i, end='')
