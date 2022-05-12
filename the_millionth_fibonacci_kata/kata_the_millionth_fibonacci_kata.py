def multiplicate_matrix(matrix1:list, matrix2:list) -> list:
    res = [[0] * len(matrix2[0]) for j in range(len(matrix2))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix1[0])):
                res[i][j] = res[i][j] + matrix1[i][k]*matrix2[k][j]
    return res


def fib(n):
    if n >= 0:
        I = [[1, 1], [1, 0]]
        k = 1
    else:
        I = [[0, -1], [-1, 1]]
        n *= -1
        k = 1 - 2*(n%2)
    factor = n
    f = [[0], [1]]
    while n>0:
        if n%2!=0:
            f = multiplicate_matrix( I, f )
        I = multiplicate_matrix(I, I)
        n >>= 1
    return (k**factor)*f[0][0]


if __name__ == '__main__':
    print(fib(-95))