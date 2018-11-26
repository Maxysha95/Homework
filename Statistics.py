import random, math


def istehere_substring(a, b, k):
    s1 = set([a[i : i + k] for i in range(len(a) - k+1)])
    s2 = set([b[i : i + k] for i in range(len(b) - k+1)])
    common = s1 & s2
    if len(common)>0:
        return common.pop()
    else:
        return ''


def lsubstring(a,b):
    l = min(len(a),len(b))
    minl = 0
    maxl = l
    while maxl>minl+1:
        t = (maxl+minl)//2
        if istehere_substring(a,b,t) == '':
            maxl = t
        else:
            minl = t
    if istehere_substring(a,b,maxl) == '':
        return istehere_substring(a,b,minl)
    else:
        return istehere_substring(a,b,maxl)


def rand_dna(n):
    res=''
    for i in range(n):
        res+=random.choice('CGTA')
    return res

x = rand_dna(1000)
raz = 0
for i in range(10000):
    y = rand_dna(1000)
    if len(lsubstring(x,y)) >= 8:
        raz += 1

print (raz/10000.0)

for i in range(25):
    k = 0
    for j in range(1000):
        y = rand_dna(1000)
        if len(lsubstring(x,y)) >= 25 - j:
            k += 1
            if k/10000 > 0.05:
                break
            print (25 - i +1)
