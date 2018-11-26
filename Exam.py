def valuesunion(*dicts):
    s = set()
    for d in dicts:
        for k,v in d.items():
            s.add(v)
    return s


    assert valuesunion({1: 2, 4: 8}) == {2, 8}
    assert valuesunion({1: 2, 4: 8}, {'a': 'b'}, {}, {}) == {2, 8, 'b'}
    print("valuesunion works")

def popcount(n):
    return bin(n).count('1')


    assert popcount(0)== 0
    assert popcount(1) == 1
    assert popcount(10) == 2
    assert popcount(1023) == 10
    print("popcount works")

def powers(n, m):
    result = {}
    for i in range(1, n+1):
        result[i] = i**i % m
    return result


    assert powers(3, 1000000000) == {1: 1, 2: 4, 3: 27}
    assert powers(4, 50) == {1: 1, 2: 4, 3: 27, 4: 6}
    assert powers(1, 1) == {1: 0}
    print("powers work")


def subpalindrome(s):
    max_len = 0
    result = " "

    def is_palindrome(s):
        if len(s) == 0:
           return True
        else:
            for i in range(0, len(s) // 2):
                if s[i] != s[-1 -i]:
                    return False
        return True

        for i in range(len(s)):
            for j in range(i + 1, len(s) +1):
                if is_palindrome(s[i: j]):
                    if len(s[i:j]) > max_len:
                        max_len = len(s[i: j])
                        result = s[i,j]
                    elif len(s[i, j]) == max_len:
                        if s[i: j] < result:
                            result = s[i: j]
        return result

    assert subpalindrome('abc') == 'a'
    assert subpalindrome('aaaa') == 'aaaa'
    assert subpalindrome('abaxfgf') == 'aba'
    assert subpalindrome('abacabad') == 'abacaba'
    print("subpalindrome works")




from functools import reduce
fib = lambda n:reduce(lambda x,y:(x[0]+x[1],x[0]),[(1,1)]*(n-2))[0]
