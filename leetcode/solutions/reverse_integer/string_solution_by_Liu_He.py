"""
Author: Liu He
Instructor: Shreck Ye
Date: June 10, 2019
"""


class Solution(object):
    def reverse(self, x: int) -> int:
        x_string = str(x)
        if x >= 0:
            rev = int(x_string[::-1])
            if rev < 2 ** 31:
                return rev
            else:
                return 0
        else:
            rev = -int(x_string[:0:-1])
            if rev >= -2 ** 31:
                return rev
            else:
                return 0
