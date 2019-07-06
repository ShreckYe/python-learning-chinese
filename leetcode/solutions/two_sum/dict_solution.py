"""
Author: Shreck Ye
Date: June 5, 2019

Time complexity: best case and most cases O(n), worst case O(n^2)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = dict()
        for index, num in enumerate(nums):
            supplement_index = num_indices.get(target - num)
            if supplement_index is not None:
                return [supplement_index, index]
            num_indices[num] = index
