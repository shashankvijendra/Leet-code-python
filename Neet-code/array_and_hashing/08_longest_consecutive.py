from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = set(nums)
        temp = {}
        lenght = 0
        for i in nums:
            if i-1 in data:
                continue
            else:
                l = i+1
                longest = 1
                temp[i] = [i]
                while l in data:
                    temp.setdefault(i, []).append(l)
                    l+=1
                    longest+=1
                lenght = max(lenght, longest)
        return lenght
    
    

# Input: nums = [2,20,4,10,3,4,5]
# Output: 4

# Input: nums = [0,3,2,5,4,6,1,1]
# Output: 7
    
    