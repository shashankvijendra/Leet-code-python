"""Products of Array Discluding Self
Solved 
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n)
O(n) time without using the division operation?"""


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
    
def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    output = [1] * n

    # Step 1: Prefix product
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    # Step 2: Postfix product (from right to left)
    postfix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]

    return output
    

# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]


# Input: nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]

