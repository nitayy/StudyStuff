# Written by: Nitay Yehezkely

import random


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


# ----------- Q1 ----------------------
# Alice side:
p = 433;
g = 5;
x = 111;
y = sam(g, x, p);
m = 314;
z = sam(m, x, p)

# Bob side:
a = 419;
b = 79

# -------------- a --------------------
c = (sam(m, a, p) * sam(g, b, p)) % p
q = 187
s1 = (c * sam(g, q, p)) % p;
s2 = sam(s1, x, p)

# Alice checks if a,b define c:
print(c == (sam(m, a, p) * sam(g, b, p)) % p)

# Bob checking:
print(s1 == (c * sam(g, q, p)) % p, s2 == (sam(z, a, p) * sam(y, b + q, p)) % p)

# ------------- b -----------------
# Bob side:
x = 234;
y = sam(g, x, p);
z = sam(m, x, p)  # The new sign. We need to calculate y,z again...

k = 10;
s = 3;
b = 295

v1 = (pow(m, s) * pow(g, b)) % p;
v2 = (pow(z, s) * pow(y, b)) % p
# v1,v2 were sent to Alice.

# Alice checks if the signature is OK:
print("v2=v1^x", v2 == sam(v1, x, p))


# The output was True...


def hash_f(r, i):
    # Alice calculate hash:
    return sam(5, r * i, p)


i = random.randint(0, p - 1);
r = 232
# Alice sends Bob:
alice_h = hash_f(r, i)

"""
Now Alice can use b, but it will be the same as above...
Now we will check the hash:
"""
bob_h = hash_f(r, s)
print("Bob hash = Alice hash:", bob_h == alice_h)
# Iff i=3 the output will be "True".

# ------------------- Q3 -----------------
# Q3-a:
p = 19


def find_sr(a, p):
    """
    The function find the roots of a mod p iff p=3 mod 4.
    :param a:
    :param p:
    :return:
    """
    if a >= p:
        return None
    if p % 4 == 3:
        x = pow(a, (p + 1) // 4, p)
        if pow(x, 2, p) == a:
            return x % p
        else:
            return (p - x) % p
    else:
        return None


def is_sr(a, p):
    if a >= p:
        return None
    if p % 4 == 3:
        x = pow(a, (p + 1) // 4, p)
        if pow(x, 2, p) == a:
            return True
        else:
            return False
    else:
        return None


def elp(x):
    return (pow(x, 3, p) + 2 * x + 3) % p


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


def daa(num, p, m):
    """
    The function calculate num*p % m - by converting p to binary number.
    """
    l_p = num_to_list(to_bin(p))  # getting the number at binary.
    z = 0
    for i in l_p:
        z = (z + z) % m
        if i == 1:
            z = (z + num) % m
    return z


# A class of  a point:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        """Adds other to the point and return the new point"""
        if other != self:
            m = ((other.y - self.y) % p) * find_opp((other.x - self.x) % p, p)
        else:
            m = (((3 * pow(self.x, 2, p) + 2) % p) * (find_opp(2 * self.y, p))) % p
        new_x = (pow(m, 2, p) - self.x - other.x) % p
        new_y = (m * (self.x - new_x) % p - self.y) % p

        return Point(new_x, new_y)

    def mul_n(self, n):
        # l_p = num_to_list(to_bin(n))  # getting the number at binary.
        # z = Point(0,0)
        # for i in l_p:
        #     z = (z + z)
        #     if i == 1:
        #         z = (z + self)
        # return
        z = self
        for i in range(n - 1):
            z += self
        return z


# A class of the Elliptic Curve given mod 19.
class ElpCrv:
    points = []

    def __init__(self):
        for x in range(p):
            y = elp(x)
            if is_sr(y, p):
                y = find_sr(y, p)
                temp = Point(x, y)
                self.points.append(temp)
                if y != 0:
                    temp = Point(x, (p - y))
                    self.points.append(temp)

    def get_points(self):
        return self.points


# ------------------- Q3 - a  -----------------


print("The points are:")
ec = ElpCrv()
for i in ec.points:
    print(i)
print("Total of points:", len(ec.points))

# ------------------- Q3 - b  -----------------

po = Point(1, 5)
points = [po]
for i in range(2, 20):
    points.append(po.mul_n(i))

flag = True
for i in ec.points:
    if i not in points:
        print("The point ", i, "is not at the last group of points.")
        flag = False
if flag:
    print("The point (1,5) create Z19!")
