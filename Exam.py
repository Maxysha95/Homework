def valuesunion(*dicts):
    s = set()
    for d in dicts:
        for k,v in d.items():
            s.add(v)
    return s
print(valuesunion({1: 2, 4: 8}))
print(valuesunion({1: 2, 4: 8}, {'a': 'b'}, {}, {}))


def popcount(n):
    return bin(n).count('1')

print(popcount(0))
print(popcount(1))
print(popcount(10))
print(popcount(1023))


from functools import reduce
fib = lambda n:reduce(lambda x,y:(x[0]+x[1],x[0]),[(1,1)]*(n-2))[0]
