"""
Author: Shreck Ye
Date: June 16, 2019
Time complexity: O(log(N))

Let's think in the mathematical way. Obviously, the recursion formula represents a linear relationship.
By viewing it as a recursion formula of a single vector F_n = (f_n, f_{n + 1})' with a transition matrix M = (0, 1; 1, 1),
which is (f_{n + 1}, f_{n + 2})' = (0, 1; 1, 1) (f_n, f_{n + 1})' namely F_{n + 1} = M F_n,
we can get the result using matrix exponentiation and reduce the number of recursions.
"""
import copy

F_0 = [[0], [1]]
M = [[0, 1], [1, 1]]


def zero_matrix(m: int, n: int):
    rows = [None] * m
    row = [0] * n
    for i in range(m):
        rows[i] = copy.deepcopy(row)
    return rows


def matmul(A, B):
    # More checks of matrix shapes may be performed
    m = len(A)
    n = len(B)
    l = len(B[0])
    C = zero_matrix(m, l)
    for i in range(m):
        for j in range(l):
            sum = 0
            A_i = A[i]
            for k in range(n):
                sum += A_i[k] * B[k][j]
            C[i][j] = sum
    return C


def eye(size: int):
    E = zero_matrix(size, size)
    for i in range(size):
        E[i][i] = 1
    return E


def matrix_power(A, n: int):
    size = len(A)
    if n == 0:
        return eye(size)
    elif n == 1:
        return copy.deepcopy(A)
    else:
        A_pow_half_n = matrix_power(A, n // 2)
        A_pow_n = matmul(A_pow_half_n, A_pow_half_n)
        if n % 2:
            A_pow_n = matmul(A_pow_n, A)
        return A_pow_n


class Solution:
    def fib(self, N: int) -> int:
        return matmul(matrix_power(M, N), F_0)[0][0]


# Test cases
s = Solution()
print(s.fib(0), s.fib(1), s.fib(2), s.fib(3), s.fib(4), s.fib(5))
