from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = 1
        for i in nums:
            if i!=0:
                temp *= i
        if 0 in set(nums):
            c = 0
            res = []
            for i in nums:
                if i==0:
                    c+=1
                    res.append(temp)
                else:
                    res.append(0)
                if c>1:
                    return [0]*len(nums)
            return res

        return [temp//i for i in nums]

# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]


# Input: nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]

