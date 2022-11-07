# Written by: Nitay Yehezkely

import math
import itertools

def gcd(a, b):
    # From here: https://codereview.stackexchange.com/a/95523
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)


def pow_2(num):
    """
    The function gets a number and return how many 2's he had.
    like: 40 = 2^3 *5 so the function will return 3.
    :param num:
    :return:
    """
    k = 0
    while num % 2 == 0:
        k += 1
        num //= 2
    return k


# ------------------------------ Q1 ----------------------------


n = 168163
e = 17
d = 59057
ed = e * d  # 1003969
k = pow_2(ed - 1)
r = (ed - 1) // (2 ** k)
print(k, r, 2 ** k * r, '\n')
for i in range(2, 30):
    if i ** r % n != 1:
        if (i ** r) ** 2 % n == 1:
            print(i, (i ** r - 1) % n, gcd(i ** r - 1, n))
print('\n')
print(2 ** r % n, (2 ** r) ** 2 % n)

# ------------------------------ Q2 ----------------------------

print('\n\nQ2: \nThe rho function result: ')


def g(x):
    return (x ** 2) + 1


def rho(num):
    x = y = 2
    drho = 1
    while drho == 1:
        x = g(x)
        y = g(g(y))
        drho = math.gcd(abs(x - y), num)
    if drho == num:
        return -1
    else:
        return drho


p = rho(n)
print(p)
print("So n =", p, '*', n // p)

# ------------------------------ Q3 ----------------------------


def p1(num):
    B = 10
    a = 2
    for k in range(2, B + 1):
        a = (a ** k) % n
        d = math.gcd(a - 1, num)
        if 1 < d < n:
            return [d,k]
    return -1


print("\nThe result for Q3 is:")
print(p1(n)[0]," and for: ",p1(n)[1],"!")

# ------------------------------ Q4 ----------------------------


def fermat(num):
    """
    The function makes Fermat's factorization method.
    :param num: An integer.
    :return: a list that includes - how may steps we did, s+d, s-d, s^2-d^2.
    """
    s = math.ceil(math.sqrt(num))
    print("s is",s)
    steps = 0  # How many steps we need to do.
    d = math.sqrt(s ** 2 - num)
    while d != math.ceil(d) and s < num:
        s += 1
        steps += 1
        d = math.sqrt(s ** 2 - num)
    return [steps, s + d, s - d, s ** 2 - d ** 2]


print("\nThe answer to Q4 is:")
print(fermat(n))

# ------------------------------ Q5 ----------------------------
primes=[2,3,5,7,11,13,17,19,23,27,31,37,41,43]
B = 44


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


def all_even(di):
    """Checks if all the powers are even"""
    for i in di.values():
        if i % 2 == 1:
            return False
    return True


def mul_to_num(di):
    num=1
    for i,j in zip(di.keys(),di.values()):
        num*=i**j
    return num


def print_dic(di):
    for i in di:
        if (di[i]>0):
            print(i,"^",di[i],end=';')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Getting the sqrt of n
sn=math.sqrt(n)
sn = math.ceil(sn)

# looking for the numbers
gr=[]
for i in range(sn,sn+30):
    gr.append((i**2)%n)

print("\n\n\nThe answer to Q5 is: \nThe numbers below dividing n:")

# com includes all the combinations of those numbers at size 2.
com=itertools.combinations(gr,2)
for i in com:
    m1=((i[0]*i[1])**2) % n
    s_m1 = (i[0]*i[1]) % n # The first root.
    m2 = (i[0]**2 * i[1]**2) % n
    temp = div_to_primes(m1,B)
    if temp != -1 and all_even(temp):
        for i in temp: # Here we are making the second root.
            temp[i]=temp[i]//2
        s_m2=mul_to_num(temp)
        temp = math.gcd(n,abs(s_m1-s_m2))
        if temp != 1 and temp!=n:
            print(temp)


# ------------------------------ Q6 ----------------------------

n=3837523
q6_t = [3077,8077,9398,1964,7078,19095,14262]
q6 = [(i**2) %n for i in q6_t]


# Getting the sqrt of n
sn=math.sqrt(n)
sn = math.ceil(sn)

# looking for the numbers
# gr=[]
# for i in range(sn,sn+30):
#     gr.append((i**2)%n)

print("\n\n\nThe answer to Q6 is: \nThe numbers below dividing n:")
for i in q6:
    print(i,"\t",div_to_primes(i,B))

"""
The output (with editing):
38    {2: 1, 3: 0, 5: 0, 7: 0, 11: 0, 13: 0, 17: 0, 19: 1, 23: 0, 27: 0, 31: 0, 37: 0, 41: 0, 43: 0}
59375 {2: 0, 3: 0, 5: 5, 7: 0, 11: 0, 13: 0, 17: 0, 19: 1, 23: 0, 27: 0, 31: 0, 37: 0, 41: 0, 43: 0}
19773 {2: 0, 3: 2, 5: 0, 7: 0, 11: 0, 13: 3, 17: 0, 19: 0, 23: 0, 27: 0, 31: 0, 37: 0, 41: 0, 43: 0}
54340 {2: 2, 3: 0, 5: 1, 7: 0, 11: 1, 13: 1, 17: 0, 19: 1, 23: 0, 27: 0, 31: 0, 37: 0, 41: 0, 43: 0}
15925 {2: 0, 3: 0, 5: 2, 7: 2, 11: 0, 13: 1, 17: 0, 19: 0, 23: 0, 27: 0, 31: 0, 37: 0, 41: 0, 43: 0}
"""
print("\n\n\n")
q = [1964,14262] # checking if 1964^2=19773 and 14262^2 = 15952 (mod n of course)
for i in q:
    print((i**2) % n)
# Yes, they are!

a=17745
b=math.sqrt((q[0]*q[1])**2)
print("The GCD is:")
p = int(gcd(n,abs(a-b)))
print(p)
q=n//p
print(q)
print(p*q)