from itertools import tee, count, starmap

def squares(a):
    for i in a:
        yield i**2


def repeatntimes(elems, n):
    for item in tee(elems, n):
        yield from item



def evens(x):
    if x % 2:
        x+=1
    while True:
        yield x
        x += 2


def digitsumdiv(p):
    for i in itertools.count(p):
        def sum_digits(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        t = sum_digits(i)
        if t % p == 0:
            yield i


def extractnumbers(s):
    return filter(lambda x: x.isdigit(), s)


def changecase(s):
    return map(lambda x: x.swapcase(), s)


def productif(elems, conds):
    return reduce(lambda x, y: x * y, map(lambda x: x[0] if x[1] is True else
                                          1, zip(elems, conds)), 1)


if __name__ == '__main__':

    assert list(squares([])) == []
    assert list(squares([1, 3, 5])) == [1, 9, 25]
    print("squares is ok")


    assert list(repeatntimes([1], 5)) == [1, 1, 1, 1, 1]
    assert list(repeatntimes([1, 2, 3], 3)) == [ 1, 2, 3, 1, 2, 3, 1, 2, 3]
    assert list(repeatntimes([1, 2], 0)) == []
    print("repeatntimes is ok")

    it = evens(3)
    for i in range(9):
        print (next(it))

print(list(repeatntimes(map(lambda x: x**2, range(3)), 2)))
