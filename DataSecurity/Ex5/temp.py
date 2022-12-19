import time
m1 = int(round(time.time() * 10000))
for i in range(30):
    pass
m2= int(round(time.time() * 10000))
print (m2-m1)

r = list(range(65,91))
t = list(range(97,123))
s = list(range(48,58))
for i in t:
    r.append(i)
for i in s:
    r.append(i)
ch=[]
for i in r:
    ch.append(chr(i))
print(ch)
