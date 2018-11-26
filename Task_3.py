import itertools

<<<<<<< HEAD
=======

>>>>>>> 9064605c4df70c502a0b11c40e15ec16f86cf266
def squares(a):
    for i in a:
        yield i**2


def repeatntimes(elems, n):
    for n in range(n):
        for i in elems:
            yield i


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
    return list(filter(lambda x: x.isdigit(), s))






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


    it = digitsumdiv(5)
    for i in range(6):
        print (next(it))


    assert list(extractnumbers('12345')) == ['1','2', '3', '4', '5']
    assert list(extractnumbers('a1b2c3d4e5')) == ['1', '2', '3', '4', '5']
    print( "extractnumbers is ok")
