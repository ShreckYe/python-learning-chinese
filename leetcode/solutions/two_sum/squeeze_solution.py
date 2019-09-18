"""
Author: Shreck Ye
Date: June 8, 2019

Time complexity: O(n log(n))
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        indexed_nums = list(enumerate(nums))
        # Sort by num value
        indexed_nums.sort(key=lambda indexed_num: indexed_num[1])
        i = 0
        j = length - 1
        while i < j:
            index_i, num_i = indexed_nums[i]
            index_j, num_j = indexed_nums[j]
            s = num_i + num_j
            if s == target:
                return [index_i, index_j]
            elif s < target:
                i += 1
            else:
                j -= 1


# Test cases
print(Solution().twoSum([3, 2, 4], 6))
