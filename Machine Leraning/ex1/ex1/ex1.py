# Yehezkely Nitay 021976808
# ex1.py

import scipy as sp
import matplotlib.pyplot as plt
import scipy.spatial.distance as sd
import math
import random as r
import numpy as np


#--------------------CONSTANTS declarations------------------

epsilon = math.ldexp(1.0, -20)
idx = [2,5,10,25,50,100,500,1000]
D = 1000
ker = sp.arange(0.02, 1.00, 0.02)


#                     -  FUNCTIONS / CLASSES declarations  -
#-----------------------------------------------------------------------------------


def discrete_gauss(n, g=[0.5, 0.5]):
    """
    discrete_gauss(n, g=[0.5, 0.5])

    Estimates the discrete Gaussian distribution (probability mass function)
    by multiple convolutions with a minimal kernel g.

    :param n: scalar.
           the number of elements of the result (n = 2..1000).
           the functions performs n-2 convolutions to create the result.

     :param g: 1-D array.
           the minimal kernel. Default value is [0.5, 0.5].
           Other kernels of the form [a, 1-a],
           where 0 > a > 1.0 are possible, but they are less effective:
           1. a larger n should be used to be as similar to a Gaussian.
           2. the peak of the result is not centered.

    :return: 1-D array.
          f, the discrete estimate of Gaussian distribution.
         f has n elements.
     """

    #Checks if the kernel is good and if n and g are good:
    if ((g[0]<=0 or g[1]>=1) or (n not in range(2,1001)) or (sum(g)!= 1.0)):
        return None
    f=g
    #We have already 2 elements in f.
    for i in range (n-2):
        f=sp.convolve(f,g)
    #checks if the sum is 1
    num=0
    for i in f:
        num+=i
    if (num <= epsilon):
        return None
    else:
        return f

# -----------------------------------------------------------------------------------
#----------------------Functions for Question 1--------------------------------------
#------------------------------------------------------------------------------------


def show_discrete_gauss(f):
    """

     :param f: 1-D array.
           the array for showing the bar graphs.

    :param save: If save the figures automatically. (Defult: True = yes).

    :return: The function plot the bar graph.
    """
    N = len(f)
    x = range(N)

    title = repr(N) + " Bars"
    fig = plt.figure()
    fig.suptitle(title, fontsize=20)
    N = len(f)
    x = range(N)
    plt.bar(x, f, bottom=0, color="blue", alpha=0.7)
    plt.show()
#-----------------------------------------------------------------------------------


def move_peak_to_center(f):
    """
    The Function get a 1-D vector f and moves the peak to the center,
    by cutting where needed...
    The function will work only in case that the maximum is at the right side (or at the center).
    The length of the vector must be odd!!!
    :param f: The 1-D array.
    :return: The new array.
    """
    f=list(f)
    p=f.index(max(f))
    l=len(f)-1
    if(p==len(f)//2):
        return f #In case the maximum is at the center.
    m=min(p,l-p)
    if (m==p):
        return (f[0:2*p+1])
    else:
        return (f[l-2*(l-p):len(f)])


#-----------------------------------------------------------------------------------


def move_peak_to_center_add(f):
    """
    The Function get a 1-D vector f and moves the peak to the center,
    by adding values.
    Because we are using it just for 999, so I assume there is ONLY one maximum.
    (In other words - The length of the vector must be odd!!!)
    :param f: The 1-D array.
    :return: The new array.
    """

    #finding the place of the max element in f (f.object() doesn't work here!)
    f = list(f)
    p = f.index(max(f))
    if(p==len(f)//2):
        return f #In case the maximum is at the center.

    #For case we have more then one element with the max value


    #finding the maximum, and other needed parameters:
    l=len(f)-1
    diff=max(p,l-p)
    temp=[]
    for i in range(abs(l-2*p)):
        temp.append(0.0)
    new_f=[]
    if (diff==p):
        return(f[0:len(f)]+temp)
    else:
        return(temp+f[0:len(f)])

#-----------------------------------------------------------------------------------
def crop(f,n):
    """
    The function gets vector f with g=[0.5,0.5] and crop it to size of n.
    :param f: the 1-D vector.
    :param n: the size of the vector.

    :return: The new vector at size n.
    """

    if (n>len(f)):
        return f
    f = list(f)
    p = f.index(max(f))
    if (n % 2 == 0):
        new_f = f[p - n//2:p + n//2]
    else:
        new_f = f[p - n//2:p + n//2 +1] #The +1 is becuase we want the other maximum
    return new_f
#-----------------------------------------------------------------------------------
def add(f,n):
    """
    Same action as crop doing, but by adding elements (0.0's).
    :param f: The vector we want to increase.
    :param n: The new size.
    :return: The vector f at the new size.
    """
    if (len(f)>=n):
        return f

    d1=len(f)
    d=abs(d1-n)//2
    f=list(f)
    temp=[]
    for i in range(d):
        temp.append(0.0)
    return (temp+f+temp)

#-----------------------------------------------------------------------------------
def diff_vecs(v1,v2):
    """
    The function returns the difference between v1 and v2 by by v1-v2.
    :param v1: The first vector
    :param v2: the second vector.
    :return: the difference.
    """
    if (len(v1)!=len(v2)):
        return None

    sum=0
    for i in range(len(v1)):
       sum+=abs(v1[i]-v2[i])
    return sum

# -----------------------------------------------------------------------------------
#----------------------Functions for Question 2--------------------------------------
#------------------------------------------------------------------------------------


def dice():
    """
    :return: A random number between 1-6
    """
    r.seed()
    return r.randint(1,6)

#------------------------------------------------------------------------------------
def rolls(n=D):
    """
    :return: 1-d vector of rolling n dices rolls.
    """
    d=[]
    for i in range(n):
        d.append(dice())
    return d

#------------------------------------------------------------------------------------


def sum_rolls(n):
    """
    The function making n rolls and return the sum of the rolls.
    :param n: the number of the rolls.
    :return: array rolls that each cell contains the sum of the roll until the specific roll.
    """
    rolls = []
    sum_of_rolls = 0
    for i in range(n):
        sum_of_rolls += dice()
        rolls.append(sum_of_rolls)
    return rolls
#-----------------------------------------------------------------------------------


def avg_rolls(n):
    """
    Same as make_rolls, but it returns the average of the rolls at each cell.
    :param n: the number of the rolls.
    :return: Vector with the average of the rolls
    """

    d=sum_rolls(n)
    for i in range(len(d)):
        d[i]=d[i]/(i+1)

    return d


#-----------------------------------------------------------------------------------
#-----------RUNING the solution to the exercise-------------------------------------
#-----------------------------------------------------------------------------------


#------------Question 1c------------------------------------------------------------


def q1c():
    for i in idx:
        f=discrete_gauss(i)
        show_discrete_gauss(f)

q1c()

# ------------Question 1d------------------------------------------

def q1d():
    for i in idx:
        f=discrete_gauss(i,[0.1,0.9])
        show_discrete_gauss(f)

q1d()

# ------------Question 1e-----------------------------------------
def q1e():
    res = []
    res2 = []
    for i in ker:
        size = 999
        f = discrete_gauss(size, [i, 1 - i])
        f = list(f)
        f = move_peak_to_center(f)
        f1 = discrete_gauss(size)
        f1 = crop(f1, len(f))
        f = list(f)
        f1 = (list(f1))
        res.append(sd.cosine(f, f1))
        res2.append(diff_vecs(f, f1))

    plt.plot(ker, res, 'b*-')
    plt.title("The Cosine distance - crop method")
    plt.xlabel("The kernel a [a,1-a]")
    plt.ylabel("The distance")
    plt.show()
    plt.plot(ker, res2, 'r.-')
    plt.title("The abs(v1-v2) distance - crop method")
    plt.xlabel("The kernel a [a,1-a]")
    plt.ylabel("The distance")
    plt.show()

q1e()


# ------------Question 1f-----------------------------------------
def q1f():
    res = []
    res2 = []
    for i in ker:
        size = 999
        f = discrete_gauss(size, [i, 1 - i])
        f = list(f)
        f = move_peak_to_center(f)
        f1 = discrete_gauss(size)
        f1 = crop(f1, len(f))
        f = list(f)
        f1 = (list(f1))
        res.append(sd.cosine(f, f1))
        res2.append(diff_vecs(f, f1))
    plt.plot(ker, res, 'b*-')
    plt.title("The Cosine distance - add method")
    plt.xlabel("The kernel a [a,1-a]")
    plt.ylabel("The distance")
    plt.show()
    plt.plot(ker, res2, 'r.-')
    plt.title("The abs(v1-v2) distance - add method")
    plt.xlabel("The kernel a [a,1-a]")
    plt.ylabel("The distance")
    plt.show()

q1f()

#------------Question 2d------------------------------------------

def q2d():
    d = np.arange(1, D + 1)
    s = sum_rolls(D)
    for i in range(D):
        s[i] = s[i] / (i + 1)
    plt.title("Roll vs. the mean of the rolls")
    plt.xlabel("The roll")
    plt.ylabel("The mean of the rolls")
    plt.plot([0, D], [3.5, 3.5], 'r', d, s, 'b')
    plt.show()

q2d()

#------------Question 2e------------------------------------------

q2d()

#------------Question 2f-------------------------------------------
def q2f():
    a = []
    exp = []
    var = []
    d = np.arange(1, D + 1, 1)
    for i in range(100):
        a.append(avg_rolls(D))
    for i in range(D):
        temp = []
        for j in a:
            temp.append(j[i])
        exp.append((np.mean(temp)))
        var.append((np.cov(temp)))

    plt.plot(d, var, 'b')
    plt.title("The average variance")
    plt.xlabel("The roll")
    plt.ylabel("The variance of the mean")
    plt.show()
    plt.title("The average expectation")
    plt.xlabel("The roll")
    plt.ylabel("The expectation of the mean")
    plt.plot(d, exp, 'g')
    plt.show()

q2f()
#-------------------------END OF FILE-----------------------------------