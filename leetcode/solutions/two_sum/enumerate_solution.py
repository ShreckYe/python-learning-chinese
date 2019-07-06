"""
Author: Liu He
Instructor: Shreck Ye
Date: June 8, 2019

Time complexity: O(n^2)
Note: the solution may result in Time Limit Exceeded
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i == j:
                    continue
                if num + num2 == target:
                    return [i, j]
