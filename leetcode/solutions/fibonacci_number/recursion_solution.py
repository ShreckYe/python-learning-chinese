"""
Author: Shreck Ye
Date: June 13, 2019
Time complexity: O(fib(N)) = O(((1 + sqrt(5)) / 2) ^ N)
"""


class Solution:
    def fib(self, N: int) -> int:
        return N if N <= 1 else self.fib(N - 2) + self.fib(N - 1)
