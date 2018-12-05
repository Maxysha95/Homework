import itertools

def valuesunion(*dicts):
    s = set()
    for d in dicts:
        for k,v in d.items():
            s.add(v)
    return s


def popcount(n):
    return bin(n).count('1')


def powers(n, m):
    result = {}
    for i in range(1, n+1):
        result[i] = i**i % m
    return result


def subpalindrome(s):
    max_len = 0
    result = " "

    def is_palindrome(s):
        if len(s) == 0:
           return True
        else:
            for i in range(len(s) // 2):
                if s[i] != s[-1 -i]:
                    return False
        return True

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(s[i: j]):
                if len(s[i:j]) > max_len:
                    max_len = len(s[i: j])
                    result = s[i: j]
                elif len(s[i, j]) == max_len:
                    if s[i: j] < result:
                        result = s[i: j]
        return result


def isIPv4(s):
    for ch in s:
        if not ch.isdigit() and ch != '.':
            return False
    if len(s.split(".")) != 4:
        return False
    for part in s.split("."):
        if int(part) < 0 or int(part) > 255:
            return False
    for part in s.split("."):
        if part[0] == 0 and len(part) != 1:
            return False

    return True


def pascals():
    prev = []
    currnet = []
    for i in itertools.count():
        if i == 0:
            current = [1]
        elif i == 1:
            current = [1, 1]
        else:
            current = [1]
            for i in range(len(prev) - 1):
                current.append(prev[i] + prev[i + 1])
            current += [1]
        prev = current
        yield tuple(current)



from functools import reduce

def fibonacci(n):
    return reduce(lambda x,n: [x[1], x[0]+x[1]], range(n), [0,1])[0]




if __name__ == '__main__':

    assert valuesunion({1: 2, 4: 8}) == {2, 8}
    assert valuesunion({1: 2, 4: 8}, {'a': 'b'}, {}, {}) == {2, 8, 'b'}
    print("valuesunion works")

    assert popcount(0)== 0
    assert popcount(1) == 1
    assert popcount(10) == 2
    assert popcount(1023) == 10
    print("popcount works")

    assert powers(3, 1000000000) == {1: 1, 2: 4, 3: 27}
    assert powers(4, 50) == {1: 1, 2: 4, 3: 27, 4: 6}
    assert powers(1, 1) == {1: 0}
    print("powers work")

    assert subpalindrome('abc') == 'a'
    assert subpalindrome('aaaa') == 'aaaa'
    assert subpalindrome('abaxfgf') == 'aba'
    assert subpalindrome('abacabad') == 'abacaba'
    print("subpalindrome works")

    assert isIPv4('192.168.0.15') == True
    assert isIPv4('255.255.255.255') == True
    assert isIPv4('555.555.555.555') == False
    assert isIPv4('190+2.168.0.0') == False
    assert isIPv4('abacaba') == False
    assert isIPv4('') == False
    print("isIPv4 works")


    it = pascals()
    for i in range(7):
        print(next(it))

    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    print("fibonacci - OK")


    print(subpalindrome('zabacj'))
