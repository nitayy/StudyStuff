a = """
Vh bkgozjxkyosg, y ildizvzlzvjh bvosfk vi y cfzsjr jt fhbjrvhx dg psvbs lhvzi jt onyvhzfaz ykf kfonybfr pvzs bvosfkzfaz, ybbjkrvhx zj y kfxlnyk igizfc; zsf "lhvzi" cyg df ivhxnf nfzzfki (zsf cjiz bjccjh), oyvki jt nfzzfki, zkvonfzi jt nfzzfki, cvazlkfi jt zsf ydjqf, yhr ij tjkzs. Zsf kfbfvqfk rfbvosfki zsf zfaz dg ofktjkcvhx.
"""

b = """
In cryptography, a substitution cipher is a method of encoding by which units of plaintext are replaced with ciphertext, according to a fixed system; the "units" may be single letters (the most common), pairs of letters, triplets of letters, mixtures of the above, and so forth. The receiver deciphers the text by performing.
"""

print(len(a))
abc = 'abcdefghijklmnopqrstuvwxyz'

for i in a:
    if i.isalpha() and i not in abc:
        print(i)