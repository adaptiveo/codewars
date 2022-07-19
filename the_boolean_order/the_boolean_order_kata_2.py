import itertools
import time
from typing import Set

s = "ttftff"
op = "|&^&&"
matrix = []

operators = ['&', '|', '^']
forbiden = ['(t)', '(f)', '(&)', '(|)', '(^)', 't(', ')t', 'f(', ')f', ')(']
combinations: Set[list] = set()

def prepare_matrix(s:str):
    matrix = [[0] * len(s) for i in range(len(s))]
    for i in range(len(s)):
        if s[i] == 't':
            matrix[i][i] = 1
    return matrix

def solve_matrix(s:str, op:str, matrix:list):
    n = len(s)
    for m in range(1, n + 1):
        for i in range(n - m):
            j = i + m
            r_max = 0
            for k in range(i, j):
                print(f'{r_max} + m[{i}][{k}] {matrix[i][k]} {op[k]}  {matrix[k + 1][j]} m[{k + 1}][{j}]')
                if op[k] == '&':
                    r_max = r_max + ( matrix[i][k] & matrix[k+1][j] )
                elif op[k] == '|':
                    r_max = r_max + ( matrix[i][k] | matrix[k + 1][j] )
                elif op[k] == '^':
                    r_max = r_max + ( matrix[i][k] ^ matrix[k + 1][j] )
                print(r_max)
            matrix[i][j] = r_max
    print(matrix)
    return matrix[0][n-1]

def solve(s:str, ops:str):
    ...








if __name__ == '__main__':
    matrix = prepare_matrix(s)
    solve_matrix(s, op, matrix)




