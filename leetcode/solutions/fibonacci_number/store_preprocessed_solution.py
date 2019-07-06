"""
Author: Shreck Ye
Date: June 15, 2019
Complexity: O(1)

We can notice a very interesting condition in the question description, that the input range for N is [0, 30], which is very small.
Therefore we can first compute all the results needed and then just feed what's needed.
This is the fastest solution for this specific question.

For problems with bigger input ranges for which results are to big to store, this method still works,
as we can store results at a certain interval according to the given memory size, and calculate needed with respect to the closest preprocessed result(s).
Let I denote the interval, the time complexity can be reduced to O(I) in this way.
This is a very common technique used in ACM/ICPC contests.
"""
fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
        46368, 75025, 121393, 196418, 317811, 514229, 832040]


class Solution:
    def fib(self, N: int) -> int:
        return fibs[N]
