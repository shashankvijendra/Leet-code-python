"""Longest Consecutive Sequence
Solved 
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time."""


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = set(nums)
        temp = {}
        lenght = 0
        for i in nums:
            if i-1 in data:
                continue
            l = i+1
            longest = 1
            temp[i] = [i]
            while l in data:
                temp.setdefault(i, []).append(l)
                l+=1
                longest+=1
            lenght = max(lenght, longest)
        print(temp)
        return lenght
    
    

# Input: nums = [2,20,4,10,3,4,5]
# Output: 4

# Input: nums = [0,3,2,5,4,6,1,1]
# Output: 7

Solution().longestConsecutive([0,3,2,5,4,6,1,1])
    