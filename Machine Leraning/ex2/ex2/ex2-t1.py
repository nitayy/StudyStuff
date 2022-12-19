import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def randrange(n, vmin, vmax):
    return 3 #(vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
fig.suptitle("HGello")
n = 100
xs=[]
ys=[]
zs=[]
for c, m, zl, zh in [('r', 'o', -50, -25)]:
    xs.append(randrange(n, 23, 32))
    ys.append(randrange(n, 0, 100))
    zs.append(randrange(n, zl, zh))
    print("A")

print(len(xs),len(ys),len(zs))
print(xs,"\n\n\n", ys,"\n\n\n" ,zs)
print(type(xs))
ax.scatter(xs, ys, zs)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
