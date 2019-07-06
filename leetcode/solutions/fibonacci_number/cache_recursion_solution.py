"""
Author: Shreck Ye
Date: June 15, 2019
Time complexity: O(N)
"""

fibs = [0, 1] + [None] * 29


class Solution:
    def fib(self, N: int) -> int:
        fib = fibs[N]
        if fib is not None:
            return fib
        else:
            fib = self.fib(N - 2) + self.fib(N - 1)
            fibs[N] = fib
            return fib
