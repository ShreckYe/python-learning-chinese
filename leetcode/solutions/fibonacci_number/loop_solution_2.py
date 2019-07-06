"""
Author: Shreck Ye
Date: June 15, 2019
Time complexity: O(N)
"""


class Solution:
    def fib(self, N: int) -> int:
        fn, fnp1 = 0, 1
        for _ in range(N):
            fn, fnp1 = fnp1, fn + fnp1
        return fn
