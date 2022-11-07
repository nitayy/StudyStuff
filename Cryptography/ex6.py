# Ex6: By Nitay Yehezkely

import math

# ------------------ Functions ---------------
primes=[2,3,5,7]
B = 8


def l_of_primes(b):
    l={}
    for i in primes:
        if i<=b:
            l[i]=0
    return l


def div_to_primes(num,b):
    dic=l_of_primes(b)
    temp=num
    i = 0
    while num > 1 and i<len(primes):
        p=primes[i]
        if num % p == 0:
            num = num // p
            dic[p]+=1
        else:
            i+=1
    if num == 1:
        return dic
    else:
        return -1

# ----------------------- Q1 - a -----------------
n = 96
print(div_to_primes(n,B))
p = [2,3]

for a in range(2,8):
    for j in p:
        print(a,(a**(n//j)) % (n+1))


# ----------------------- Q1 - c -------------------
def modn(t, po):
    return (t**po) % n


b = 31

lp = [2,3,5,7]
n=97
k = [4,13,21,25,27,34,48,52,66,72,78,83]
k_pow = [modn(5,i) for i in k]

k_eq = [div_to_primes(modn(5,i),B) for i in k]
for i in range(len(k)):
    if k_eq[i]!=-1:
        print(k[i],k_pow[i],k_eq[i])

print("Now we will try to find r:")
for i in range(2,10):
    temp=(b*pow(5,i)) % n
    d=div_to_primes(temp,B)
    if d != -1:
        print(i,d)

# ----------------------- Q1 - d -------------------
# Some variables taken from the previous section.
print("\nBaby steps - Giant steps:")


def div_list(a, b):
    """
    The function gets a,b (a<b) and returns the div list of the gcd algorithm.
    :param a: Integer
    :param b: Integer
    :return: a List
    """
    if math.gcd(a, b) != 1:
        return None
    divs = []
    while a > 0:
        divs.append(b // a)
        temp = a
        a = b % a
        b = temp
    return divs


def find_opp(a, n):
    """
    The function return the opposite number of a modulo n i.e. a^-1 mod n.
    :param a:
    :param n:
    :return:
    """
    d = div_list(a, n)
    s = [0, 1]
    for i in range(2, len(d) + 1):
        t = -d[i - 2] * s[i - 1] + s[i - 2]
        s.append(t)
    return s[-1] % n


def bsgs(a,b,n):
    """
    The function calculate x of a^x=b (mod n)
    :param a:
    :param b:
    :param n:
    :return:
    """
    m = math.ceil(math.sqrt(n))
    l_ipow = [(5**i) % n for i in range(m)]
    am = pow(5,n-m-1) % n
    print(am)
    y=b
    for j in range(m):
        if y in l_ipow:
            print(j,i,m)
            return m*j+l_ipow.index(y)
        else:
            y=(y*am) % n


print("x is: ",bsgs(5,31,97))

# ----------------------- Q2 - d -------------------

print("\nQ2-d:", find_opp(62, 71))
print("The a of Alice is: ",(find_opp(62, 71)*68)%71)


# ----------------------- Q3 -----------------------

n = 25217
p = 151
q = 167
r = [15919,15704,4681]


def find_root(b,p):
    """Works only if p = 3 % 4"""
    if (p % 4) != 3:
        return None
    else:
        return pow(b,(p+1)//4) % p


def sol_for_roots(root,p):
    sp=[]
    if root==0:
        sp.append(0)
    else:
        if pow(root, 2) % p == i % p:
            sp.append(root), sp.append(-root)
        else:
            neg = (p-root) % p
            if pow(root,2) == neg:
                sp.append(neg)
    return sp


print("\n\nHere is the solution for Q3:")
print(p % 4, q%4," - Both p and q are = 3 (mod 4)")
for i in r:
    print("-"*40)
    print("{0} % {1} = {2} |\t{0} % {3} = {4}: ".format(i,p,i%p,q,i%q))
    # Here we will make the b^((p+1)/4):
    rp=find_root(i%p,p)
    rq=find_root(i%q,q)
    sp = sol_for_roots(rp,p)
    sq = sol_for_roots(rq,q)
    print("The roots are: ",sp,sq)
    print("Now we will find the solutions for the roots:")
    if sp == [] or sq ==[]:
        print("There are no roots!")
    else:
        for ip in sp:
            for iq in sq:
                x = (ip*(find_opp(q,p))*q+iq*(find_opp(p,q))*p) % n
                print("The solution for p*q=n is:", x,",x^2=r? ",pow(x,2)%n == i)
