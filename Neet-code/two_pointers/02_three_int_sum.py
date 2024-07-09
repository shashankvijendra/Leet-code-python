"""Three Integer Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], 
nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k 
are all distinct.

The output should not contain any duplicate triplets. 
You may return the output and the triplets in any order."""


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        data = set(nums)
        res = set()
        for i in range(len(nums)):
            for j in nums[i+1:]:
                if i+j in data:
                    res.add((nums[i], j, i+j))    
        
        return set(res)

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))