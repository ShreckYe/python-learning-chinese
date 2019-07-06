"""
Author: Shreck Ye
Date: June 10, 2019
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        return x_string == x_string[::-1]


# Test cases
s = Solution()
print(s.isPalindrome(121), s.isPalindrome(-121), s.isPalindrome(10))
