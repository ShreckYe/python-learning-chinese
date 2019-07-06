"""
Author: Shreck Ye
Date: June 10, 2019
"""

INT32_MIN = -1 << 31
INT32_MAX = (1 << 31) - 1


class Solution:
    def reverse(self, x: int) -> int:
        x_string = str(x)
        reversed_x = int(x_string[::-1]) if x >= 0 else -int(x_string[:0:-1])
        return reversed_x if (INT32_MIN <= reversed_x <= INT32_MAX) else 0


# Test cases
s = Solution()
print(s.reverse(12345))
print(s.reverse(12300))
print(s.reverse(-123))
print(s.reverse(-1563847412))
