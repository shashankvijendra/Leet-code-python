from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True
    
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for i in nums:
            if i in new_set:
                return False
            new_set.add(i)
        return True
    
# Input: nums = [1, 2, 3, 3]
# Output: true


# Input: nums = [1, 2, 3, 4]
# Output: false
