"""
Author: Shreck Ye
Date: June 16, 2019
Time complexity: O(log(N))
Note: the solution does not run on LeetCode because importing NumPy is currently not supported by LeetCode.

Let's think in the mathematical way. Obviously, the recursion formula represents a linear relationship.
By viewing it as a recursion formula of a single vector F_n = (f_n, f_{n + 1})' with a transition matrix M = (0, 1; 1, 1),
which is (f_{n + 1}, f_{n + 2})' = (0, 1; 1, 1) (f_n, f_{n + 1})' namely F_{n + 1} = M F_n,
we can get the result using matrix exponentiation and reduce the number of recursions.
"""
import numpy as np

F_0 = np.array([0, 1])
M = np.array([[0, 1], [1, 1]])


class Solution:
    def fib(self, N: int) -> int:
        return np.matmul(np.linalg.matrix_power(M, N), F_0)[0]


# Test cases
s = Solution()
print(s.fib(0), s.fib(1), s.fib(2), s.fib(3), s.fib(4), s.fib(5))
