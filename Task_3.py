def squares(a):
    for i in a:
        yield i**2


def repeatntimes(elems, n):
    for n in range(n):
        for i in elems:
            yield i


if __name__ == '__main__':
    assert list(squares([])) == []
    assert list(squares([1, 3, 5])) == [1, 9, 25]
    print("squares is ok")


    print(list(repeatntimes([1, 2, 3],0)))
