import numpy as np

def getdimension(a):
    return a.ndim


def getdiagonal(a):
    return np.diagonal(a)


def cutarray(a, minvalue, maxvalue):
    return np.clip(a, minvalue, maxvalue)


def getmoments(a):
    lst = ( np.mean(a), np.var(a) )
    return lst


def getdotproduct(a, b):
    return np.dot(a, b)


def checkequal(a, b):
    return np.equal(a , b)


def comparewithnumber(a, bound):
    return a < bound


def matrixproduct(a, b):
    return np.matmul(a,b)


def matrixdet(a):
    return np.linalg.det(a)


def getones(n, k):
    return np.eye(n, k=k)


if __name__ == '__main__':
    assert getdimension(np.array([1, 2, 3])) == 1
    assert getdimension(np.array([[1], [2], [3]])) == 2
    assert getdimension(np.array([[[[1]]]])) == 4
    print("getdimension is ok")

    print(getdiagonal(np.array([[1, 2], [3, 4]])))

    print(cutarray(np.array([1, 2, 3, 4]), 2, 3))


    assert getmoments(np.array([2, 1, 9])) == (4.0, 12.666666666666666)
    print("getmoments is ok")

    assert getdotproduct(np.array([1, 2, 3]), np.array([4, 5, 6])) == 32
    print("getdotproduct is ok")

    print(checkequal(np.array([1, 2, 3]), np.array([1, 5, 3])))

    print(comparewithnumber(np.array([[1, 2], [3, 4]]), 4))


    assert np.array_equal(matrixproduct(np.array([[1, 2], [3, 4]]),
                                        np.array([[5, 6], [7, 8]])),
                          np.array([[19, 22], [43, 50]]))
    assert np.array_equal(matrixproduct(np.array([[1, 2]]),
                                        np.array([[3], [4]])),
                          np.array([[11]]))
    print("matrixproduct is ok")


    print(matrixdet(np.array([[5, 6], [7, 8]])))
    print(matrixdet(np.array([[123]])))



    print(getones(3, 1))
    print(getones(3, 9))
