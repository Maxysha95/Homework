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
        return recurrent(n//2)
    else:
         return recurrent((n - 1)//2) + recurrent((n - 1)//2 + 1)


def digitsum(n):
    if n // 10 == 0:
        return n
    else:
        return n % 10 + digitsum(n // 10)


def reversestring(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reversestring(s[0:-1])



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


def parentheses(s):
    if len(s) <= 2:
        return '(' + s + ')'
    return '(' + s[0] + parentheses(s[1:-1]) + s[-1] + ')'

def mergesort(a):
    if len(a) > 1:
        middle= len(a) // 2
        left = a[:middle]
        right = a[middle:]
        left = mergesort(left)
        right = mergesort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    return a



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


    assert parentheses('example') == '(e(x(a(m)p)l)e)'
    assert parentheses('odd') == '(o(d)d)'
    assert parentheses('even') == '(e(ve)n)'
    print('parentheses is ok')


    assert mergesort([]) == []
    assert mergesort([100]) == [100]
    assert mergesort([1, 3, 2]) == [1, 2, 3]
    assert mergesort([1, 3, 5, 4, 2]) == [1, 2, 3, 4, 5]
    print('mergesort is ok')
