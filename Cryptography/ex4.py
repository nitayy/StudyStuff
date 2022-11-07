# Written by: Nitay Yehezkely

import math


def gcd(a, b):
    # From here: https://codereview.stackexchange.com/a/95523
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)


def div_list(a, b):
    """
    The function gets a,b (a<b) and returns the div list of the gcd algorithm.
    :param a: Integer
    :param b: Integer
    :return: a List
    """
    if gcd(a, b) != 1:
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


def bezout(a, n):
    """
    The function return the opposite number of a modulo n i.e. a^-1 mod n.
    :param a:
    :param n:
    :return:
    """
    d = div_list(a, n)
    s = [0, 1]
    s2 = [1, 0]
    for i in range(2, len(d) + 1):
        t = -d[i - 2] * s[i - 1] + s[i - 2]
        t2 = -d[i - 2] * s2[i - 1] + s2[i - 2]
        s.append(t)
        s2.append(t2)
    return [s[-1], s2[-1]]


def pollard(p):
    """
    Try to break p into small integers.
    :param p:
    :return:
    """
    a = 2
    for i in range(2, 11):
        a = pow(a, i) % p
        if (gcd(a - 1, p)) != 1:
            print("k is:", i)
            return gcd(a - 1, p)
    return None


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


def fermat_prime(num):
    """
    The function checks if num is prime or not.
    :param num: An integer.
    :return: T/F. True if prime, else - False.
    """
    return fermat(num)[2] == 1


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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Q1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# --------------- a: ---------------


n = 2237579
e = 17
one = 151405
two = 202315
ms = [one, two]
for i in ms:
    print(i ** e % n)

# --------------- b: ---------------
p = pollard(n)
q = n // p
print("The dividers of are:", p, q)

# --------------- c: ---------------
print(fermat(n))
# --------------- d: ---------------
phi_n = (p - 1) * (q - 1)  # = 2234400
d = find_opp(e, phi_n)
print(d)


# --------------- e: ---------------
# some functions for section e:


def to_bin(num):
    """Source: https://stackoverflow.com/a/699891/2013542"""
    return int("{0:b}".format(num))


def num_to_list(num):
    """
    The function gets a number and return it a as list - each element is a digit.
    :param num: The number.
    :return: list of the digits.
    """
    l = []
    while num > 0:
        l.append(num % 10)
        num = num // 10
    l.reverse()
    return l


def sam(num, p, m):
    """
    The function calculate num^p % m - by converting p to binary number.
    """
    l_p = num_to_list(to_bin(p))  # getting the number at binary.
    z = 1
    for i in l_p:
        z = z ** 2 % m
        if i == 1:
            z = z * num % m
    return z


# Now we will do all the calculations:


c = 1863490  # the encrypted message
m_p = q * find_opp(q, p)
m_q = p * find_opp(p, q)
d_p = d % (p - 1)
d_q = d % (q - 1)
c_p = c % p
c_q = c % q
y_p = sam(c_p, d_p, p)
y_q = sam(c_q, d_q, q)

x = (y_p * m_p + y_q * m_q) % n  # The result is: 40114

print(x)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Q2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Fermat method:
n2 = 38200901201
# Checking primality by Fermat:
print(fermat(n2), fermat_prime(n2))


# Rabin-Miller
def rabin_miller_base(num, a):
    """
    0 = probably prime. 1 = Not prime, else - not prime and the witness.
    :param num: The number.
    :param a: The base.
    :return:
    """
    k = pow_2(num - 1)
    r = (num - 1) // (2 ** k)
    b = sam(a, r, num)

    if b == 1 or b == num - 1:
        return 0
    for j in range(1, k):
        tb = b
        b = sam(b, 2, num)
        if b == 1:
            return tb
        if b == num - 1:
            return 0
    return 1


def rabin_miller(num):
    """
    The function make the Miller-Rabin Primality Test, and returns if the number is prime (probably) or not,
    or is witness.
    :param num: The number.
    :return: A string with the answer.
    """
    print('*' * 30, '\n', "Rabin-Miller Primality Test for ", str(num), ':')
    for a in range(2, 21):
        witness = rabin_miller_base(num, a)
        print("For base: ", str(a), end='\t')
        if witness == 1:
            print("Not prime")
        elif witness > 1:
            print("Not a prime number and " + str(witness) + " is a witness")
            print("The GCD of ",n2," and ",witness-1," (n-1) is: ", gcd(witness-1,n2))
        else:
            print("Probably prime")


rabin_miller(n2)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Q3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

n3 = 11413
e_a = 17
e_b = 129
c_a = 4772
c_b = 1495
print("\n\n\nThe gcd od c_a and c_b is: ", gcd(e_a, e_b))
bez = bezout(e_a, e_b)
print(bez)

# Calculations for finding the message:
c_as = sam(c_a, bez[0], n3)  # c_a ^s % n3
print(c_as)
print(find_opp(c_b, n3))  # Finding the opposit of c_b.
c_bt = sam(find_opp(c_b, n3), abs(bez[1]), n3)
print(c_bt)
print("The code for the copy machine is:")
print((c_as * c_bt) % n3)
