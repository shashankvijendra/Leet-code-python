from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> list[int]:
        d = {}
        for i, n in enumerate(nums):
            if target-n in d:
                return [d[target-n], i]
            d[n] = i


# Input: 
# nums = [3,4,5,6], target = 7
# Output: [0,1]


# Input: nums = [4,5,6], target = 10
# Output: [0,2]


# Input: nums = [5,5], target = 10
# Output: [0,1]

