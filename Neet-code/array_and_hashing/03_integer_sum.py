from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for index, num in enumerate(nums):
            if target - num in num_to_index:
                return [num_to_index[target - num], index]
            num_to_index[num] = index


# Input: 
# nums = [3,4,5,6], target = 7
# Output: [0,1]


# Input: nums = [4,5,6], target = 10
# Output: [0,2]


# Input: nums = [5,5], target = 10
# Output: [0,1]

