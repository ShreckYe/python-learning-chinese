"""
Author: Shreck Ye
Date: June 13, 2019
Time complexity: O(N)
"""


class Solution:
    def fib(self, N: int) -> int:
        f_n = 0
        f_np1 = 1
        for _ in range(N):
            f_np2 = f_n + f_np1
            # These 2 lines below are not interchangeable
            f_n = f_np1
            f_np1 = f_np2
        return f_n
