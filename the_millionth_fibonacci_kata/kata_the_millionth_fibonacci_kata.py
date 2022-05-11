import numpy as np

def fib(n):
    I = np.array([[1, 1], [1, 0]])
    R = np.array([1, 0])
    while n>0:
        if n%2!=0:
            R = R.dot(I)
        I = I.dot(I)
        n >>= 1 #Уменьшаем степень вдвое
    return R[1]

if __name__ == '__main__':
    print(fib(1000000))