import random
import xo

def get():
    return(random.randint(1,17))


def get2(): return [get() for i in range(10)]


def get3(): return [get2() for i in range(50)]

d=get3()
def is_in(n): return [a for a in d if n in a]
l=is_in(7)
d2 = [d.index(x) for x in l]
print("d2:",d2, "\nL:",l)
#for i in l: print(i)


a=[1,2,3]
def f(a):
    b=a
    b=[1]
    return b
print(f(a))

d = {1:[1,2,3], 2:[4,5,6]}
print(d[1][2])

l= [x for x in range(20)]
l = ['aa','ads','sasa']
d = {l[i]:i for i in range(len(l))}

print(d)
v=[False,True,False,False]
if True in v[1:4]:
    print("WOW!")
    print(v.index(True))
v=[True]*20
print(v)
# k={i:i**2 for i in range(10)}
# # for i in k.values(): print(i)
#
# a="*"*50
# print(a)
# a=[False for i in range(10)]
# print(a)
# print("x"=='x')
# d=["a","b","c","d"]
# print('a' in d)
# print(d[1:4])
# print('a'+'b')

print(xo.dic)
