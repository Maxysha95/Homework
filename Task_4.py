import math
import itertools
#way 1
def factorial(n):
  if n < 2:
      return 1
  return n* factorial(n -1)

#way 2
def factorial(n):
    return math.factorial(n)


def fibonacci(n):
    if n < 2:
        return n
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))


def recurrent(n):
    if n < 2:
        return n
    elif n % 2 == 0:
        return recurrent(n/2)
    else:
         return recurrent((n - 1)/2) + recurrent((n - 1)/2 + 1)


def digitsum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def reversestring(s):
    return ''.join(reversed(s))


def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m -1, 1)
    return ackermann(m - 1, ackermann(m, n-1))


def istwopower(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return istwopower(n // 2)
    return False


def concatnumbers(a, b):
    if b // 10 == 0:
        return a * 10 + b
    else:
        return concatnumbers(a, b // 10) * 10 + b % 10

def abacaba(n):
    if n == 1:
        return [1]
    return abacaba(n-1) + [n] + abacaba(n-1)


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

"""def drawborders(n):
def genbinarystrings(n):
def parentheses(s):
def mergesort(a): - ??? """


if __name__ == '__main__':

    assert factorial(0) == 1
    assert factorial(2) == 2
    assert factorial(4) == 24
    print("factorial is ok")

    assert fibonacci(1) == 1
    assert fibonacci(4) == 3
    assert fibonacci(10) == 55
    print("fibonacci is ok")

    assert recurrent(2) == 1
    assert recurrent(3) == 2
    assert recurrent(5) == 3
    assert recurrent(7) == 3
    print("recurrent is ok")

    assert digitsum(0) == 0
    assert digitsum(123) == 6
    assert digitsum(192837465) == 45
    print("digitsum is ok")


    assert reversestring('') == ''
    assert reversestring('1') == '1'
    assert reversestring('asdf') =='fdsa'
    assert reversestring('abacaba') =='abacaba'
    print("reversestring is ok")

    assert ackermann(0, 10) == 11
    assert ackermann(1, 1) == 3
    assert ackermann(2, 2) == 7
    assert ackermann(2, 5) == 13
    assert ackermann(3, 3) == 61
    print("ackermann is ok")

    assert istwopower(-5) == False
    assert istwopower(0) == False
    assert istwopower(1) == True
    assert istwopower(2) == True
    assert istwopower(4) == True
    assert istwopower(67) == False
    assert istwopower(1024) == True
    print("istwopower is ok")

    assert concatnumbers(1, 2) == 12
    assert concatnumbers(55, 88) == 5588
    assert concatnumbers(123, 789) == 123789
    assert concatnumbers(1000, 2) == 10002

    assert abacaba(1) == [1]
    assert abacaba(2) == [1, 2, 1]
    assert abacaba(3) == [1, 2, 1, 3, 1, 2, 1]
    assert abacaba(4) == [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]
    print("abacaba is good")

    assert gcd(1, 5) == 1
    assert gcd(4, 6) == 2
    assert gcd(18, 12) == 6
    assert gcd(283918822, 595730520) == 22
    print("gsd is ok")
