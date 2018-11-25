def unique(e):
    list(e)
    a = []
    for i in e:
        if i not in a:
            a.append(i)
    b = sorted(a)

    return b


def mex(e):
    i = 1
    while True:
        if i not in e:
            return i
        i += 1


def transposeDict(d):
    res = {}
    for k, v in d.items():
        res[v] = k
    return res


def frequencyDict(s):
    res = {}
    for i in s:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    return res
