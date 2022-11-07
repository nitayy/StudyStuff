M1 = 'hnermzkarmfhkrwfpvuzvneorxerr'
M2 = 'molyfsnbyfumnyrugizsiolxyalyy'


def c_code(s, n):
    for i in s:
        t = ord(i) + n
        if t > 122:
            t -= 26
        print(chr(t), end='')
    print('\n')


def cou(s):
    r = []
    for c in 'abcdefghijklmopqrstuvwxyz':
        r.append([s.count(c), c])
    r.sort(reverse=True)
    return r


for i in range(26):
    c_code(M1, i)
print('----------------------------------------------')
for i in range(26):
    c_code(M2, i)

# For questions 3(c):
print("q3-c:")
n = 12
e = lambda x: (5 * x + 4) % n
for i in range(n):
    if (i != e(i)):
        print(i, e(i))
    else:
        print(i, e(i), '***')

# For question 4(b):
print("q4-b:")
n=26
for i in range(n):
    if (i*i) % n == 1:
        print(i)

print('\n\n\n')
n = 26
e = lambda x: (25 * x + 1) % n
for i in range(n):
    if (i != e(e(i))):
        print(i, e(e(i)))
    else:
        print(i, e(e(i)), '***')

# For question 5:
# print("q5:")
g=[1,3,5,7,9,11,15,17,19,21,23,25]
for i in g:
    for j in g:
        if (i*j) % n not in g:
            print(i,j,i*j)

# For Q. 6:
print("Q6:")
n=37
d = lambda x: 15*(x - 11) % n # Encryption function.
e = lambda x: (5 * x + 11) % n # Description function.
abc = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ "
e_msg = "OH7F86BB46R3627O266BB9"
for i in e_msg:
    t = d(abc.find(i))
    print(abc[t],end='')
